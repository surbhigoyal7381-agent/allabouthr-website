# -*- coding: utf-8 -*-
"""Shared page shell for the recovered AllAboutHR path-based pages.

This file holds the chrome only — header, breadcrumb, footer, call-to-action
band. The page copy lives in content.py. Run tools/build_pages.py to write the
HTML files out.
"""

SITE = "https://allabouthr.co"
WA = "https://wa.me/917696004555"
PHONE_DISPLAY = "+91 76960 04555"
PHONE_HREF = "+917696004555"
MAIL = "hello@allabouthr.co"

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=Poppins:wght@300;500;600;800&amp;family=Source+Sans+3:ital,wght@0,400;0,600;1,400'
    '&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap">'
)

WA_ICON = (
    '<svg class="waicon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M17.5 14.4c-.3-.2-1.7-.9-2-1-.3-.1-.5-.2-.7.1s-.7 1-.9 1.2c-.2.2-.3.2-.6.1a8 8 0 0 1-2.4-1.5 9 9 0 0 1-1.7-2.1c-.2-.3 0-.5.1-.6l.5-.6.3-.5v-.5l-1-2.3c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3z"/>'
    '<path d="M12 2a10 10 0 0 0-8.5 15.2L2 22l4.9-1.4A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-2.9.8.8-2.8-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>'
)

NAV = [
    ("/", "Home"),
    ("/consulting/", "Consulting"),
    ("/alvora/", "Alvora"),
    ("/kinexus/", "Kinexus"),
    ("/packages/", "Packages"),
    ("/about-us/", "About"),
]

FOOT = [
    ("Streams", [
        ("/consulting/", "AllAboutHR Consulting"),
        ("/alvora/", "Alvora Platforms"),
        ("/kinexus/", "Kinexus Systems"),
        ("/packages/", "Packages and pricing"),
        ("/service-best-expert-solution/", "All services"),
    ]),
    ("Talent, training, jobs", [
        ("/jobs/", "Jobs"),
        ("/job-openings/", "Job openings"),
        ("/training/", "Training"),
        ("/recruitxcel/", "RecruitXcel"),
    ]),
    ("Company", [
        ("/about-us/", "About us"),
        ("/our-team/", "Our team"),
        ("/clients/", "Our clients"),
        ("/testimonials/", "Testimonials"),
        ("/why-choose-allabouthr/", "Why choose AllAboutHR"),
        ("/contact-us/", "Contact us"),
    ]),
]


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def jstr(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def canonical(slug):
    slug = slug.strip("/")
    return SITE + "/" if not slug else "%s/%s/" % (SITE, slug)


def head(slug, title, meta, extra_ld=""):
    canon = canonical(slug)
    ld = (
        '<script type="application/ld+json">\n'
        '{"@context":"https://schema.org","@type":"WebPage","name":%s,"url":%s,'
        '"description":%s,'
        '"isPartOf":{"@id":"https://allabouthr.co/#website"},'
        '"publisher":{"@type":"Organization","name":"AllAboutHR","url":"https://allabouthr.co"}}\n'
        '</script>' % (jstr(title), jstr(canon), jstr(meta))
    )
    return """<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AllAboutHR">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="%s/assets/og-cover.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_IN">
<meta name="twitter:image" content="%s/assets/og-cover.png">
<meta name="twitter:card" content="summary">
%s
<link rel="icon" href="/assets/logo.webp" type="image/webp">
<link rel="stylesheet" href="/assets/site.css">
%s
%s
""" % (esc(title), esc(meta), canon, esc(title), esc(meta), canon, SITE, SITE,
       FONTS, ld, extra_ld)


def header(active=""):
    links = "".join(
        '<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == active else "", t)
        for h, t in NAV)
    return """<a class="skip" href="#main">Skip to content</a>
<header class="hdr">
  <div class="bar">
    <a class="brand" href="/" aria-label="AllAboutHR home"><img src="/assets/logo.webp" alt="AllAboutHR" width="1205" height="160"></a>
    <nav class="nav" aria-label="Main">%s<a class="btn btn-p cta" href="/contact-us/">Talk to us</a></nav>
  </div>
</header>
<main id="main">""" % links


def crumbs(trail):
    """trail is a list of (href or None, label); the last entry is this page."""
    items, ld = [], []
    for i, (href, label) in enumerate(trail):
        if href and "#" in href:
            raise ValueError(
                "breadcrumb %r points at a hash route; BreadcrumbList needs a real URL" % href)
        if href:
            items.append('<li><a href="%s">%s</a></li>' % (href, esc(label)))
            target = SITE + "/" if href == "/" else canonical(href)
            ld.append('{"@type":"ListItem","position":%d,"name":%s,"item":%s}'
                      % (i + 1, jstr(label), jstr(target)))
        else:
            items.append('<li aria-current="page">%s</li>' % esc(label))
            ld.append('{"@type":"ListItem","position":%d,"name":%s}' % (i + 1, jstr(label)))
    nav = ('<nav class="crumb" aria-label="Breadcrumb"><div class="wrap narrow"><ol>%s</ol></div></nav>'
           % "".join(items))
    script = ('<script type="application/ld+json">{"@context":"https://schema.org",'
              '"@type":"BreadcrumbList","itemListElement":[%s]}</script>' % ",".join(ld))
    return nav, script


def phead(eyebrow, h1, lede, rule="streamrule"):
    return """
  <section class="phead">
    <div class="wrap narrow">
      <div class="%s"></div>
      <p class="eyebrow">%s</p>
      <h1>%s</h1>
      <p class="lede">%s</p>
    </div>
  </section>""" % (rule, esc(eyebrow), h1, lede)


def body(html):
    return ('\n  <article class="body">\n    <div class="wrap narrow">\n%s\n'
            '    </div>\n  </article>' % html)


def nextrow(cards):
    c = "".join(
        '<a class="card hov" href="%s"><span class="tag %s">%s</span><h4>%s</h4>'
        '<p>%s</p><p class="go">%s &rarr;</p></a>'
        % (href, tone, esc(tag), esc(title), esc(txt), esc(cta_label))
        for href, tone, tag, title, txt, cta_label in cards)
    return ('\n  <section class="band alt">\n    <div class="wrap">\n'
            '      <div class="sechead"><p class="eyebrow">Where to next</p>'
            '<h2 style="font-size:clamp(1.3rem,2.2vw,1.7rem)">Keep reading.</h2></div>\n'
            '      <div class="nextrow">%s</div>\n    </div>\n  </section>' % c)


def cta(h2, p, wa_msg, second=("/#/packages", "See the packages")):
    return """
  <section class="band">
    <div class="wrap">
      <div class="ctaband">
        <p class="eyebrow" style="color:rgba(255,255,255,.8)">Talk to a person</p>
        <h2>%s</h2>
        <p>%s</p>
        <div class="acts">
          <a class="btn btn-w" href="%s?text=%s" target="_blank" rel="noopener">%sMessage us on WhatsApp</a>
          <a class="btn btn-o" href="%s">%s</a>
        </div>
      </div>
    </div>
  </section>""" % (esc(h2), esc(p), WA, wa_msg, WA_ICON, second[0], esc(second[1]))


def footer():
    cols = "".join(
        '<div><h4>%s</h4><ul>%s</ul></div>'
        % (esc(title), "".join('<li><a href="%s">%s</a></li>' % (h, esc(t)) for h, t in links))
        for title, links in FOOT)
    return """</main>
<footer class="site">
  <div class="wrap">
    <div class="fgrid">
      <div>
        <img src="/assets/logo.webp" alt="AllAboutHR" width="1205" height="160">
        <p style="font-size:.93rem;color:var(--slate);max-width:34ch">Talent, technology and transformation for Indian businesses. One house, three streams, one loop that closes.</p>
        <p style="font-size:.93rem;color:var(--slate)">Mohali, Punjab, India<br>
          <a href="mailto:%s">%s</a><br>
          <a href="tel:%s">%s</a></p>
      </div>
      %s
    </div>
    <div class="fbot">
      <span>&copy; 2026 AllAboutHR. Alvora and Kinexus Systems are AllAboutHR brands.</span>
      <span class="pw">Powered by AllAboutHR.co</span>
    </div>
  </div>
</footer>
</html>
""" % (MAIL, MAIL, PHONE_HREF, PHONE_DISPLAY, cols)


def page(slug, title, meta, eyebrow, h1, lede, content, trail,
         cards=None, cta_block="", active="", rule="streamrule", extra_ld=""):
    nav, ld = crumbs(trail)
    return (head(slug, title, meta, extra_ld + ld)
            + header(active)
            + nav
            + phead(eyebrow, h1, lede, rule)
            + body(content)
            + (nextrow(cards) if cards else "")
            + cta_block
            + footer())
