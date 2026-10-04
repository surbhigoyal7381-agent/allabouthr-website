# -*- coding: utf-8 -*-
"""SEO audit across every HTML file, including the single-page index.html.

    python tools/seo_audit.py            # table + gap summary
    python tools/seo_audit.py --verbose  # per-page detail

This reports; it does not fix. check_pages.py is the pass/fail gate for the
generated pages — this is the wider picture, and it deliberately includes
index.html, which check_pages.py skips.
"""

import io
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERBOSE = "--verbose" in sys.argv


def files():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "tools", "assets", "__pycache__")]
        for fn in filenames:
            if fn.endswith(".html"):
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, ROOT).replace("\\", "/")
                out.append((rel, full))
    return sorted(out)


def text_of(html):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", html)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def ld_types(html):
    out = []
    for m in re.finditer(r'(?is)<script[^>]*application/ld\+json[^>]*>(.*?)</script>', html):
        try:
            data = json.loads(m.group(1).strip())
        except Exception:
            out.append("INVALID-JSON")
            continue
        def walk(node):
            if isinstance(node, list):
                for n in node:
                    walk(n)
            elif isinstance(node, dict):
                t = node.get("@type")
                if t:
                    out.extend(t if isinstance(t, list) else [t])
                for v in node.values():
                    if isinstance(v, (dict, list)):
                        walk(v)
        walk(data)
    return [t for t in out if t]


def audit(rel, html):
    r = {"page": rel}
    r["title"] = (re.search(r"<title>([^<]*)</title>", html) or [None, ""])[1] \
        if re.search(r"<title>([^<]*)</title>", html) else ""
    m = re.search(r"<title>([^<]*)</title>", html)
    r["title"] = m.group(1) if m else ""
    m = re.search(r'<meta name="description" content="([^"]*)"', html)
    r["desc"] = m.group(1) if m else ""
    r["canonical"] = bool(re.search(r'rel="canonical"', html))
    r["og"] = len(re.findall(r'property="og:', html))
    r["og_image"] = bool(re.search(r'property="og:image"', html))
    r["twitter"] = bool(re.search(r'name="twitter:', html))
    r["charset"] = bool(re.search(r"(?i)<meta charset", html))
    r["viewport"] = bool(re.search(r'name="viewport"', html))
    r["doctype"] = bool(re.search(r"(?i)<!doctype html>", html))
    r["lang"] = bool(re.search(r"<html[^>]*\blang=", html))
    r["h1"] = len(re.findall(r"<h1[ >]", html))
    r["h2"] = len(re.findall(r"<h2[ >]", html))
    r["ld"] = ld_types(html)
    imgs = re.findall(r"<img [^>]*>", html)
    r["imgs"] = len(imgs)
    r["img_no_alt"] = sum(1 for i in imgs if 'alt=' not in i)
    r["img_no_dim"] = sum(1 for i in imgs if 'width=' not in i or 'height=' not in i)
    r["int_links"] = len(set(re.findall(r'href="(/[^"#][^"]*)"', html)))
    r["words"] = len(text_of(html).split())
    r["kb"] = len(html.encode("utf-8")) / 1024.0
    return r


ISSUES = []


def flag(page, sev, msg):
    ISSUES.append((sev, page, msg))


def main():
    rows = []
    for rel, full in files():
        html = io.open(full, encoding="utf-8").read()
        r = audit(rel, html)
        rows.append(r)
        p = rel
        is404 = rel == "404.html"

        if not r["title"]:
            flag(p, "HIGH", "no <title>")
        elif len(r["title"]) > 70:
            flag(p, "LOW", "title %d chars (>70 truncates)" % len(r["title"]))
        if not r["desc"]:
            flag(p, "HIGH", "no meta description")
        elif len(r["desc"]) > 165:
            flag(p, "LOW", "description %d chars (>165 truncates)" % len(r["desc"]))
        if not r["canonical"] and not is404:
            flag(p, "HIGH", "no canonical")
        if r["og"] < 4 and not is404:
            flag(p, "MED", "incomplete Open Graph (%d tags)" % r["og"])
        if not r["og_image"] and not is404:
            flag(p, "MED", "no og:image — link previews will be blank")
        if not r["twitter"] and not is404:
            flag(p, "LOW", "no twitter:card")
        for k, label in (("charset", "meta charset"), ("viewport", "meta viewport"),
                         ("doctype", "doctype"), ("lang", "html lang")):
            if not r[k]:
                flag(p, "HIGH", "no %s" % label)
        if r["h1"] != 1:
            # index.html is a single document holding 8 hash routes; seven are
            # display:none and Google's renderer only sees the active one.
            sev, note = ("LOW", " — SPA routes, only one is ever visible")                 if rel == "index.html" else ("HIGH", "")
            flag(p, sev, "%d <h1> (want 1)%s" % (r["h1"], note))
        if r["img_no_alt"]:
            flag(p, "MED", "%d <img> without alt" % r["img_no_alt"])
        if r["img_no_dim"]:
            flag(p, "LOW", "%d <img> without width/height (layout shift)" % r["img_no_dim"])
        if r["words"] < 300 and not is404:
            flag(p, "MED", "thin content (%d words)" % r["words"])
        if "BreadcrumbList" not in r["ld"] and not is404 and rel != "index.html":
            flag(p, "MED", "no BreadcrumbList")
        if r["int_links"] < 5 and not is404:
            flag(p, "MED", "only %d internal links out" % r["int_links"])

    # site-wide
    allld = Counter()
    for r in rows:
        allld.update(r["ld"])
    # LocalBusiness has subtypes; ProfessionalService is one and counts.
    LOCAL = ("LocalBusiness", "ProfessionalService", "EmploymentAgency")
    if not any(allld.get(t) for t in LOCAL):
        flag("(site)", "MED", "no LocalBusiness-type schema — local pack / maps eligibility")
    for want, why in [("Organization", "who the business is"),
                      ("Person", "founder entity / knowledge panel"),
                      ("WebSite", "sitelinks search box / brand entity")]:
        if not allld.get(want):
            flag("(site)", "MED", "no %s schema anywhere — %s" % (want, why))
    # Deliberately NOT checked: FAQPage. Google restricted FAQ rich results to
    # government and health sites in August 2023, so adding the markup to a
    # business site earns nothing. Don't cargo-cult it back in.

    for f in ("robots.txt", "sitemap.xml"):
        if not os.path.isfile(os.path.join(ROOT, f)):
            flag("(site)", "HIGH", "missing %s" % f)

    # report
    print("%-56s %5s %4s %3s %3s %5s %6s" % ("PAGE", "WORDS", "LINK", "H1", "OG", "LD", "KB"))
    print("-" * 92)
    for r in sorted(rows, key=lambda x: x["page"]):
        print("%-56s %5d %4d %3d %3d %5d %6.0f"
              % (r["page"][:56], r["words"], r["int_links"], r["h1"], r["og"],
                 len(r["ld"]), r["kb"]))
        if VERBOSE:
            print("      ld=%s" % (",".join(r["ld"]) or "none"))

    print("\nSCHEMA IN USE: %s" % (", ".join("%s x%d" % (k, v) for k, v in allld.most_common())
                                   or "none"))
    order = {"HIGH": 0, "MED": 1, "LOW": 2}
    ISSUES.sort(key=lambda x: (order[x[0]], x[1]))
    counts = Counter(s for s, _, _ in ISSUES)
    print("\nISSUES: %d high, %d medium, %d low\n"
          % (counts["HIGH"], counts["MED"], counts["LOW"]))
    for sev, page, msg in ISSUES:
        print("  [%-4s] %-50s %s" % (sev, page[:50], msg))
    return 0


if __name__ == "__main__":
    sys.exit(main())
