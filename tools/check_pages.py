# -*- coding: utf-8 -*-
"""Verify the generated pages: HTML well-formedness, internal links, metadata.

    python tools/check_pages.py

Exits non-zero if anything fails, so it can be used as a pre-deploy gate.
"""

import io
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr", "path", "circle", "rect",
        "line", "polygon", "polyline", "ellipse", "stop", "use"}
# Tags the HTML spec lets you leave open; we do close them, but be lenient.
OPTIONAL = {"html", "head", "body", "li", "p", "dt", "dd", "option", "tr", "td", "th"}

failures = []
warnings = []


def fail(page, msg):
    failures.append("%s: %s" % (page, msg))


def warn(page, msg):
    warnings.append("%s: %s" % (page, msg))


class Balance(HTMLParser):
    def __init__(self, page):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.page = page
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        while self.stack:
            t, line = self.stack.pop()
            if t == tag:
                return
            if t not in OPTIONAL:
                fail(self.page, "<%s> opened at line %d closed by </%s>" % (t, line, tag))
                return
        fail(self.page, "stray </%s>" % tag)

    def finish(self):
        for t, line in self.stack:
            if t not in OPTIONAL:
                fail(self.page, "<%s> opened at line %d never closed" % (t, line))


def html_files():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "tools", "assets")]
        for fn in filenames:
            if fn.endswith(".html"):
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, ROOT).replace("\\", "/")
                if rel == "index.html":
                    continue  # the SPA is not ours to validate here
                out.append((rel, full))
    return sorted(out)


def resolves(href):
    """Does an internal href point at something that exists on disk?"""
    path = href.split("#")[0].split("?")[0]
    if path in ("", "/"):
        return os.path.isfile(os.path.join(ROOT, "index.html"))
    path = path.lstrip("/")
    cand = os.path.join(ROOT, path)
    if os.path.isfile(cand):
        return True
    if os.path.isfile(os.path.join(cand, "index.html")):
        return True
    return False


def main():
    pages = html_files()
    if not pages:
        raise SystemExit("no pages found — run tools/build_pages.py first")

    titles, canons = {}, {}
    all_internal = set()

    for rel, full in pages:
        text = io.open(full, encoding="utf-8").read()

        # Script bodies are raw text: entities and braces are legal in there.
        bare = re.sub(r"(?is)<script[^>]*>.*?</script>", "<script></script>", text)

        # 1 — template artifacts
        for bad in ("%s", "%d", "%r"):
            if bad in bare:
                fail(rel, "template artifact %r left in output" % bad)
        if re.search(r"\bNone\b", bare):
            fail(rel, "literal 'None' left in output")

        # 2 — well-formedness
        b = Balance(rel)
        b.feed(text)
        b.finish()

        # 3 — required metadata
        for pat, label in (
            (r"<title>([^<]+)</title>", "title"),
            (r'<meta name="description" content="([^"]+)"', "description"),
            (r'<link rel="canonical" href="([^"]+)"', "canonical"),
            (r'<meta property="og:title" content="([^"]+)"', "og:title"),
        ):
            m = re.search(pat, text)
            if not m:
                fail(rel, "missing %s" % label)
            elif label == "title":
                titles.setdefault(m.group(1), []).append(rel)
            elif label == "canonical":
                canons.setdefault(m.group(1), []).append(rel)

        m = re.search(r'<meta name="description" content="([^"]+)"', text)
        if m and not (50 <= len(m.group(1)) <= 185):
            warn(rel, "description is %d chars (aim 50-185)" % len(m.group(1)))
        m = re.search(r"<title>([^<]+)</title>", text)
        if m and len(m.group(1)) > 70:
            warn(rel, "title is %d chars (aim <=70)" % len(m.group(1)))

        # 3b — double-escaped entities: h1/lede pass through esc(), so an HTML
        # entity written in those fields renders as literal "&ldquo;" text.
        for m in re.finditer(r"&amp;[a-zA-Z]{2,8};", bare):
            fail(rel, "double-escaped entity %s — use the real character in h1/lede"
                 % m.group(0))

        # 4 — exactly one h1
        n = len(re.findall(r"<h1[ >]", text))
        if n != 1:
            fail(rel, "%d <h1> elements (want exactly 1)" % n)

        # 5 — structured data present (the 404 carries WebPage only, by design)
        want = 1 if rel == "404.html" else 2
        if text.count('application/ld+json') < want:
            fail(rel, "expected %d JSON-LD block(s), found %d"
                 % (want, text.count('application/ld+json')))
        if rel == "404.html" and 'content="noindex' not in text:
            fail(rel, "404 must be noindex")

        # 6 — internal links resolve
        for href in re.findall(r'href="(/[^"]*)"', text):
            all_internal.add(href)
            if not resolves(href):
                fail(rel, "broken internal link %s" % href)
            # A hash route is a dead end for a crawler: Googlebot will not
            # follow /#/packages, so a page that links that way leaks every
            # bit of its internal linking. Every stream now has a real URL,
            # so there is no longer any reason to point at one.
            if href.startswith("/#/"):
                fail(rel, "link to hash route %s — use the real page URL" % href)

        # 7 — external links must be safe
        for a in re.findall(r"<a [^>]*href=\"https?://[^\"]+\"[^>]*>", text):
            if 'target="_blank"' in a and 'rel="noopener"' not in a:
                fail(rel, "target=_blank without rel=noopener: %s" % a[:70])

        # 8 — no raw ampersands that should be entities (outside script bodies)
        for m in re.finditer(r"&(?!#?\w{1,8};)", bare):
            fail(rel, "unescaped & at offset %d: %r"
                 % (m.start(), bare[m.start():m.start() + 14]))

    # --- every class the pages use must actually have a rule in site.css ---
    # Caught a real bug: .tw / table / .ochecks / .exl live in index.html's second
    # <style> block, which site.css never carried, so tables rendered unstyled.
    css_path = os.path.join(ROOT, "assets", "site.css")
    if os.path.isfile(css_path):
        css = io.open(css_path, encoding="utf-8").read()
        used = set()
        for rel, full in pages:
            html = io.open(full, encoding="utf-8").read()
            for attr in re.findall(r'class="([^"]+)"', html):
                used.update(attr.split())
        # A class counts as covered if it appears as a selector anywhere in the
        # stylesheet — alone, compounded, or inside a descendant rule. Element
        # selectors are deliberately not checked: <dl> is styled through .facts,
        # so demanding a bare `dl` rule would be a false positive.
        for cls in sorted(used):
            if not re.search(r"\.%s(?![\w-])" % re.escape(cls), css):
                fail("assets/site.css", "class .%s is used but has no rule" % cls)

    for t, where in titles.items():
        if len(where) > 1:
            fail(", ".join(where), "duplicate <title>: %s" % t)
    for c, where in canons.items():
        if len(where) > 1:
            fail(", ".join(where), "duplicate canonical: %s" % c)

    # sitemap covers every page
    sm = os.path.join(ROOT, "sitemap.xml")
    if os.path.isfile(sm):
        smtext = io.open(sm, encoding="utf-8").read()
        for rel, _ in pages:
            if rel == "404.html":
                continue
            slug = rel[:-len("/index.html")]
            if "/%s/" % slug not in smtext:
                fail("sitemap.xml", "missing %s" % slug)

    print("Checked %d pages, %d distinct internal links.\n" % (len(pages), len(all_internal)))
    if warnings:
        print("WARNINGS (%d)" % len(warnings))
        for w in warnings:
            print("  ~ %s" % w)
        print("")
    if failures:
        print("FAILURES (%d)" % len(failures))
        for f in failures:
            print("  x %s" % f)
        return 1
    print("PASS — no failures.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
