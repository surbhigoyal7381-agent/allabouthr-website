# -*- coding: utf-8 -*-
"""Check the deployed site. Run this straight after a Netlify deploy.

    python tools/verify_live.py                      # checks https://allabouthr.co
    python tools/verify_live.py https://xyz.netlify.app   # or a deploy preview

Verifies the things that were actually broken, so a green run means the deploy
did what it was supposed to:

  * the 20 URLs that were returning 404 now return 200
  * robots.txt and sitemap.xml exist (they did not before)
  * the homepage carries its doctype, charset and viewport
  * the share card and stylesheet are served
  * an unknown URL returns a real 404 with the branded page
  * the _redirects rules are live

Exit code 1 if anything fails, so it can gate a release.
"""

import sys
import urllib.error
import urllib.request

BASE = (sys.argv[1] if len(sys.argv) > 1 else "https://allabouthr.co").rstrip("/")
UA = {"User-Agent": "allabouthr-deploy-check/1.0"}

PAGES = [
    "/", "/consulting/", "/alvora/", "/kinexus/", "/packages/",
    "/about-us/", "/our-team/", "/clients/", "/testimonials/",
    "/why-choose-allabouthr/", "/service-best-expert-solution/", "/contact-us/",
    "/jobs/", "/job-openings/", "/training/", "/recruitxcel/",
    "/nahar-group-of-companies/", "/jcbl/", "/amit-engineers-mohali/",
    "/shoolini-university/", "/r-b-university-mohali/",
    "/pinky-bansal-an-accounting-candidate/", "/dinesh-garg/",
    "/bulbul-pachar-a-fresher-candidate/",
    "/we-help-you-to-make-business-stratgey/",
    "/we-provide-best-ideas-for-the-business-growth/",
    "/we-help-individuals-and-businesses-make-things-happen-for-their-dream/",
]
ASSETS = ["/robots.txt", "/sitemap.xml", "/assets/site.css",
          "/assets/og-cover.png", "/assets/logo.webp",
          # Lose this and Search Console silently un-verifies the property.
          "/googleb3f9b7b384b96ddd.html"]
REDIRECTS = [("/about", "/about-us/"), ("/contact", "/contact-us/"),
             ("/pricing", "/packages/"), ("/careers", "/job-openings/"),
             ("/reviews", "/testimonials/"), ("/our-clients", "/clients/"),
             ("/job-opportunities", "/job-openings/"),
             ("/sitemap_index.xml", "/sitemap.xml"),
             ("/we-help-you-to-make-business-strategy",
              "/we-help-you-to-make-business-stratgey/")]

fails = []


def get(path, redirect=True):
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None
    opener = urllib.request.build_opener() if redirect \
        else urllib.request.build_opener(NoRedirect)
    req = urllib.request.Request(BASE + path, headers=UA)
    try:
        r = opener.open(req, timeout=25)
        return r.getcode(), r.read(), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, (e.read() or b""), dict(e.headers)
    except Exception as e:
        return 0, str(e).encode(), {}


def main():
    print("Checking %s\n" % BASE)

    print("pages")
    bad = 0
    for p in PAGES:
        code, _, _ = get(p)
        if code != 200:
            bad += 1
            fails.append("%s returned %s (want 200)" % (p, code))
    print("  %d/%d return 200" % (len(PAGES) - bad, len(PAGES)))

    print("assets")
    for p in ASSETS:
        code, _, _ = get(p)
        mark = "ok" if code == 200 else "FAIL %s" % code
        print("  %-22s %s" % (p, mark))
        if code != 200:
            fails.append("%s returned %s" % (p, code))

    print("homepage head")
    code, body, hdrs = get("/")
    html = body.decode("utf-8", "replace")[:4000].lower()
    for needle, label in (("<!doctype html>", "doctype"),
                          ("<meta charset", "charset"),
                          ('name="viewport"', "viewport"),
                          ('rel="canonical"', "canonical"),
                          ('property="og:image"', "og:image")):
        ok = needle in html
        print("  %-12s %s" % (label, "ok" if ok else "MISSING"))
        if not ok:
            fails.append("homepage missing %s" % label)
    ctype = next((v for k, v in hdrs.items()
                  if k.lower() == "content-type"), "(none)")
    print("  %-12s %s" % ("content-type", ctype))

    print("404 handling")
    code, body, _ = get("/this-url-does-not-exist-xyz/")
    branded = b"That page has moved" in body
    print("  status %s, branded page: %s" % (code, "yes" if branded else "NO"))
    if code != 404:
        fails.append("unknown URL returned %s, want 404" % code)
    if not branded:
        fails.append("404 is not the branded page — check 404.html deployed")

    # The recovered pages used to link onward only via hash routes, which a
    # crawler cannot follow. Confirm the deployed copies do not.
    print("crawlable internal links")
    hashy = []
    for p in PAGES:
        if p == "/":
            continue  # the single-page site routes by fragment by design
        _, b, _ = get(p)
        if b'href="/#/' in b:
            hashy.append(p)
    print("  %d/%d pages free of hash-route links"
          % (len(PAGES) - 1 - len(hashy), len(PAGES) - 1))
    for p in hashy:
        fails.append("%s still links to a hash route" % p)

    print("redirects")
    for src, want in REDIRECTS:
        code, _, hdrs = get(src, redirect=False)
        loc = hdrs.get("Location", "")
        ok = code in (301, 302) and want in loc
        print("  %-12s %s %s %s" % (src, code, loc or "-", "ok" if ok else "FAIL"))
        if not ok:
            fails.append("%s did not redirect to %s (got %s %s)" % (src, want, code, loc))

    print("")
    if fails:
        print("FAILED (%d)" % len(fails))
        for f in fails:
            print("  x %s" % f)
        return 1
    print("PASS — the deploy looks correct.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
