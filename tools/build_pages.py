# -*- coding: utf-8 -*-
"""Write out the recovered path-based pages, the 404, robots.txt and sitemap.xml.

    python tools/build_pages.py

Run from the repository root. Safe to re-run: it overwrites only the files it
owns (every <slug>/index.html listed in content.py / content2.py, plus 404.html,
robots.txt, sitemap.xml and _redirects). It never touches index.html.
"""

import datetime
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import shell  # noqa: E402
import content  # noqa: E402
import content2  # noqa: E402  (imported for its side effect of adding pages)
import content3  # noqa: E402  (ditto — the /clients/ and /testimonials/ hubs)
import content4  # noqa: E402  (ditto — the four commercial pages)

assert content2 and content3 and content4  # keep linters quiet

PAGES = content.PAGES
TODAY = datetime.date.today().isoformat()

# Hand-set crawl priorities. Anything not listed gets 0.6.
PRIORITY = {
    "packages": "1.0",
    "consulting": "0.9",
    "alvora": "0.9",
    "kinexus": "0.9",
    "about-us": "0.9",
    "service-best-expert-solution": "0.9",
    "contact-us": "0.9",
    "our-team": "0.8",
    "jobs": "0.8",
    "training": "0.8",
    "job-openings": "0.8",
    "recruitxcel": "0.8",
    "why-choose-allabouthr": "0.8",
    "clients": "0.8",
    "testimonials": "0.8",
}


def write(path, text):
    full = os.path.join(ROOT, path)
    d = os.path.dirname(full)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    with io.open(full, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return full, len(text.encode("utf-8"))


def build_page(p):
    cta_block = shell.cta(
        p["cta_h2"], p["cta_p"], p["wa"],
        p.get("cta_second", ("/#/packages", "See the packages")))
    html = shell.page(
        slug=p["slug"],
        title=p["title"],
        meta=p["meta"],
        eyebrow=p["eyebrow"],
        h1=shell.esc(p["h1"]),
        lede=shell.esc(p["lede"]),
        content=p["content"],
        trail=p["trail"],
        cards=p.get("cards"),
        cta_block=cta_block,
        active=p.get("active", ""),
        rule=p.get("rule", "streamrule"),
        extra_ld=p.get("extra_ld", ""),
    )
    return write("%s/index.html" % p["slug"], html)


# --- 404 --------------------------------------------------------------------

def build_404():
    links = "".join(
        '<li><a href="%s">%s</a></li>' % (h, shell.esc(t))
        for h, t in [
            ("/", "Home"),
            ("/about-us/", "About us"),
            ("/service-best-expert-solution/", "Our services"),
            ("/jobs/", "Jobs and recruitment"),
            ("/job-openings/", "Job openings — send your CV"),
            ("/training/", "Training"),
            ("/recruitxcel/", "RecruitXcel"),
            ("/our-team/", "Our team"),
            ("/why-choose-allabouthr/", "Why choose AllAboutHR"),
            ("/contact-us/", "Contact us"),
            ("/#/packages", "Packages and prices"),
        ])
    html = (
        shell.head("404", "Page not found — AllAboutHR",
                   "That page has moved. Here is where everything lives now.")
        .replace('<meta name="robots" content="index,follow,max-image-preview:large">',
                 '<meta name="robots" content="noindex,follow">')
        + shell.header()
        + """
  <section class="notfound">
    <div class="wrap narrow">
      <p class="code">Error 404</p>
      <div class="streamrule" style="margin-top:14px"></div>
      <h1>That page has moved.</h1>
      <p class="lede">We rebuilt this site in 2026 and a few old addresses changed. Nothing is
      lost &mdash; it is all still here, just somewhere slightly different.</p>
      <h2 style="font-size:clamp(1.2rem,2vw,1.5rem);margin-top:34px">Try one of these</h2>
      <ul>%s</ul>
      <div class="note" style="margin-top:26px">
        <h4>Looking for something specific?</h4>
        <p>Message us on <a href="%s?text=Hi%%20AllAboutHR%%20%%E2%%80%%94%%20I%%20was%%20looking%%20for%%20a%%20page%%20on%%20your%%20site%%20and%%20could%%20not%%20find%%20it.">WhatsApp</a>
        or email <a href="mailto:%s">%s</a> and we will send you the right link.</p>
      </div>
    </div>
  </section>""" % (links, shell.WA, shell.MAIL, shell.MAIL)
        + shell.footer())
    return write("404.html", html)


# --- robots.txt and sitemap.xml ---------------------------------------------

def build_robots():
    return write("robots.txt", """# AllAboutHR — https://allabouthr.co
User-agent: *
Allow: /

Sitemap: %s/sitemap.xml
""" % shell.SITE)


def build_sitemap():
    urls = [("", "1.0")] + [
        (p["slug"], PRIORITY.get(p["slug"], "0.6")) for p in PAGES]
    body = "".join(
        "  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n"
        "    <changefreq>monthly</changefreq>\n    <priority>%s</priority>\n  </url>\n"
        % (shell.canonical(slug), TODAY, prio)
        for slug, prio in urls)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           '%s</urlset>\n' % body)
    return write("sitemap.xml", xml)


# --- Netlify redirects ------------------------------------------------------

def build_redirects():
    rules = [
        ("# Old addresses that never existed as pages but get typed or linked.", None, None),
        ("/home", "/", "301"),
        ("/about", "/about-us/", "301"),
        ("/about-us.html", "/about-us/", "301"),
        ("/contact", "/contact-us/", "301"),
        ("/contact.html", "/contact-us/", "301"),
        ("/team", "/our-team/", "301"),
        ("/services", "/service-best-expert-solution/", "301"),
        ("/service", "/service-best-expert-solution/", "301"),
        ("/why-choose-us", "/why-choose-allabouthr/", "301"),
        ("/hot-jobs", "/job-openings/", "301"),
        ("/post-your-resume", "/job-openings/", "301"),
        ("/post-job-openings", "/jobs/", "301"),
        ("/careers", "/job-openings/", "301"),
        ("/pricing", "/packages/", "301"),
        ("/price", "/packages/", "301"),
        ("/hr-consulting", "/consulting/", "301"),
        ("/hrms", "/alvora/", "301"),
        ("/software", "/alvora/", "301"),
        ("/clients.html", "/clients/", "301"),
        ("/our-clientele", "/clients/", "301"),
        ("/testimonial", "/testimonials/", "301"),
        ("/reviews", "/#/review", "301"),
        ("/what-our-clients-say", "/testimonials/", "301"),
        ("/rb-university-mohali", "/r-b-university-mohali/", "301"),
        ("/nahar-group", "/nahar-group-of-companies/", "301"),
        ("", None, None),
        ("# WordPress leftovers — kill the crawl budget they waste.", None, None),
        ("/wp-admin/*", "/404.html", "404"),
        ("/wp-content/*", "/404.html", "404"),
        ("/wp-includes/*", "/404.html", "404"),
        ("/wp-json/*", "/404.html", "404"),
        ("/xmlrpc.php", "/404.html", "404"),
        ("/feed", "/", "301"),
        ("/comments/feed", "/", "301"),
    ]
    out = ["# Netlify redirects for allabouthr.co",
           "# Generated by tools/build_pages.py — edit the list in that file.",
           ""]
    for a, b, code in rules:
        if b is None:
            out.append(a)
        else:
            out.append("%-28s %-34s %s" % (a, b, code))
    return write("_redirects", "\n".join(out) + "\n")


def main():
    print("Writing %d recovered pages into %s\n" % (len(PAGES), ROOT))
    slugs = [p["slug"] for p in PAGES]
    dupes = set(s for s in slugs if slugs.count(s) > 1)
    if dupes:
        raise SystemExit("Duplicate slugs: %s" % ", ".join(sorted(dupes)))

    total = 0
    for p in PAGES:
        path, size = build_page(p)
        total += size
        print("  %-66s %6d bytes" % (p["slug"] + "/index.html", size))

    print("")
    for fn in (build_404, build_robots, build_sitemap, build_redirects):
        path, size = fn()
        total += size
        print("  %-66s %6d bytes" % (os.path.relpath(path, ROOT).replace("\\", "/"), size))

    print("\n%d pages + 4 support files, %.1f KB total." % (len(PAGES), total / 1024.0))


if __name__ == "__main__":
    main()
