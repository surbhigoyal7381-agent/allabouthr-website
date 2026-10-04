# AllAboutHR website — v1.1

**Single-page site built 24 August 2026 · 26 path-based pages added 4 October 2026**
**No build step to deploy · No dependencies**

## What this is

`index.html` is the main site. One file, ~570 KB, eight pages behind hash routes. It has
no build step, no framework, no npm install and nothing to configure. Open it in a browser
and it works — from a file, from a USB stick, from any host.

Everything in it is inlined: styles, scripts, structured data, and the logos and photos as
WebP data URIs. The only external request is to Google Fonts.

Alongside it sit **26 pages at real paths** (`/about-us/`, `/our-team/`, and so
on). These were indexed by Google from the previous WordPress site and were returning 404.
They share one small stylesheet and one logo file. See
[The recovered pages](#the-recovered-pages-v11) below.

## Deploying it

The site is on **Netlify**, serving from the repository root. Push and it deploys.

Any static host will do, though. Upload the whole directory; `index.html` is the root
document. No server-side code, so no runtime to patch and nothing to keep updated.

If you move off Netlify, the one thing that does not travel is `_redirects` — rewrite those
rules in whatever your host uses.

## The `index.html` head fix (4 October 2026)

The production file was missing its entire document head. It had **no doctype, no `<html>`
element, no `<meta charset>` and no `<meta name="viewport">`** — the file began at
`<title>`. Four lines were added at the top; the original 581,076 bytes are untouched
beneath them.

This was not cosmetic:

| Missing | What it caused |
|---|---|
| `<!doctype html>` | The browser rendered the whole site in **quirks mode** — a legacy layout mode with a different box model. |
| `<meta name="viewport">` | **The site was not responsive on phones.** Mobile browsers assumed a ~980px layout viewport, so none of the `@media (max-width: …)` rules ever fired and users got a zoomed-out desktop layout. All the mobile CSS was there; nothing was triggering it. |
| `<meta charset="utf-8">` | Apostrophes, em dashes and curly quotes rendered as `â€™`, `â€"`, `â€œ`. Live it looked fine **only because Netlify happens to send `charset=UTF-8` in the HTTP header** — open the file from disk, or move to a host that doesn't, and the text breaks. |
| `<html lang="en">` | No language declared, which matters to screen readers and to search engines. |

The file itself was always clean, valid UTF-8 — it was only ever the missing declaration.
If you see `â€` characters anywhere again, the cause is a server not sending the charset,
not corrupted content.

## Pages

### The single-page site — `index.html`

Routing is hash-based (`#/consulting`, `#/alvora`, …) so every page works from a single
file with no server rewrite rules.

| Route | Page |
|---|---|
| `#/` | Home — two engines, the three streams, the stream chooser |
| `#/consulting` | The Growth Loop, interactive by stage |
| `#/alvora` | The four platforms, the evidence chain, where AI sits |
| `#/kinexus` | Baseline, Foundation, Agents, and the agent guardrails |
| `#/packages` | All six packs |
| `#/about` | The story, the founders, the client wall |
| `#/contact` | Enquiry form |
| `#/review` | Leave a Google review |

**Hash routes are invisible to search engines.** Google only ever sees one URL, `/`. That
is the reason the recovered pages below matter for more than just fixing 404s — they are
the only indexable pages this site has.

### The recovered pages (v1.1)

Twenty real paths, each its own small HTML file. Every one of these was returning **404**
before this release; six of them were still in Google's index and appearing in search
results as dead links.

| Path | Page |
|---|---|
| `/about-us/` | About Us |
| `/our-team/` | Our Team — the two founders |
| `/why-choose-allabouthr/` | Why Choose AllAboutHR — the four promises |
| `/service-best-expert-solution/` | Our Services — the hub page |
| `/contact-us/` | Contact Us |
| `/jobs/` | Jobs — recruitment, for employers and candidates |
| `/job-openings/` | Job Openings — send your CV |
| `/training/` | Training |
| `/recruitxcel/` | RecruitXcel — the 20-day recruitment programme |
| `/nahar-group-of-companies/` | Client — Nahar Group of Companies |
| `/jcbl/` | Client — JCBL |
| `/amit-engineers-mohali/` | Client — Amit Engineers, Mohali |
| `/shoolini-university/` | Client — Shoolini University |
| `/r-b-university-mohali/` | Client — Rayat Bahra University, Mohali |
| `/pinky-bansal-an-accounting-candidate/` | Testimonial — Pinky Bansal |
| `/dinesh-garg/` | Testimonial — CA Dinesh Garg |
| `/bulbul-pachar-a-fresher-candidate/` | Testimonial — Bulbul Pachar |
| `/we-help-you-to-make-business-stratgey/` | Business strategy |
| `/we-provide-best-ideas-for-the-business-growth/` | Innovative HR ideas for growth |
| `/we-help-individuals-and-businesses-make-things-happen-for-their-dream/` | Individuals and businesses |
| `/clients/` | **New** — clients hub, links the five client pages |
| `/testimonials/` | **New** — testimonials hub, links the three testimonial pages |

`/clients/` and `/testimonials/` are **new** — they were never on the old site and are not in
Google's index. They exist because without them the five client pages and three testimonial
pages were **orphans**: nothing linked to them, which is a poor signal to a crawler and makes
them hard for a human to find. Both hubs sit in the footer of every page, so everything
recovered is now two clicks from anywhere.

The slugs are deliberately preserved exactly as they were, **typos included**
(`...business-stratgey`). Changing a slug would throw away the only thing of value these
URLs still have, which is their history in Google's index.

Four support files ship with them:

- **`404.html`** — a branded not-found page listing where everything now lives. Netlify
  serves this automatically. Marked `noindex`.
- **`robots.txt`** — the site had none, which is why nothing pointed crawlers anywhere.
  Points at the sitemap.
- **`sitemap.xml`** — all 21 URLs. The site had none of this either.
- **`_redirects`** — Netlify rules for addresses people type or link that never existed
  (`/about`, `/contact`, `/careers`, `/pricing`), plus hard 404s for the WordPress paths
  (`/wp-admin/*`, `/xmlrpc.php`) that otherwise burn crawl budget forever.

#### Where the content came from

The old site is gone and only its homepage was archived. The page list and the original
wording were recovered from:

- the Internet Archive capture of the old WordPress homepage
  (`web.archive.org/web/20250227103507/https://allabouthr.co/`), which carried the full
  navigation, the service summaries and all three testimonials in full; and
- the URLs still sitting in Google's index.

Figures (500+ placements, 50+ organisations, the founders' numbers) are taken from
`index.html` so the two halves of the site cannot drift apart. **The three testimonials are
reproduced word for word** — they are real quotes from real people and were not rewritten.

#### Editing them

Pages are generated. The copy lives in `tools/content.py` and `tools/content2.py`; the
chrome — header, breadcrumb, footer, call-to-action band — lives in `tools/shell.py`.

```
python tools/build_pages.py     # rewrites the 20 pages + the four support files
python tools/check_pages.py     # validates them; exit code 1 if anything is wrong
```

Editing a generated `index.html` by hand works fine, but the next build overwrites it — so
put real changes in `tools/`. `build_pages.py` never touches the main `index.html`.

`check_pages.py` verifies HTML well-formedness, exactly one `<h1>` per page, canonical and
Open Graph tags, unique titles and canonicals, title and description lengths, JSON-LD
presence, `rel="noopener"` on every new-tab link, unescaped ampersands, that every internal
link resolves to a file that exists, and that the sitemap covers every page. Run it before
you push.

## Running it locally

```
python tools/serve.py          # http://localhost:8777
python tools/serve.py 3000     # or any other port
```

Run it in its own terminal and leave it there; Ctrl+C stops it. If you lose the terminal,
`netstat -ano | findstr :8777` gives you the PID and `taskkill /PID <pid> /F` ends it.

Use this rather than `python -m http.server`. The built-in server ignores `_redirects`,
serves its own bare 404, and does not send a charset — so it tests none of the three things
this release actually changed. `tools/serve.py` mirrors Netlify: it applies the redirect
rules (including `/prefix/*` wildcards), serves `404.html` with a real 404 status, sends
`charset=utf-8` on text, and colour-codes every request by status so you can watch redirects
fire.

## What you must change before it goes live

1. **The contact email.** The form in `index.html` composes a `mailto:` to
   `hello@allabouthr.co`. Search for that address and replace it if it is wrong. If you want
   a real backend form, wire the `#cform` submit handler to Formspree, Netlify Forms or your
   own endpoint — the handler is at the bottom of the script block and is about fifteen
   lines. The recovered pages use the same address, set once in `tools/shell.py`.

1b. **The WhatsApp numbers.** Every call-to-action opens WhatsApp with a message already
   written for that page or package. Two numbers are in use:

   | Where | Goes to |
   |---|---|
   | Kinexus page — hero and all three offerings | **98767 01788** |
   | Everywhere else — packages, about, contact, all recovered pages | **76960 04555** |

   Search for `wa.me/` to find them. In the recovered pages the number is set once, in
   `tools/shell.py`.

   **A WhatsApp link can only ever open one chat.** There is no way to make a single tap
   message two numbers. If you want one button that reaches both of you, set up a
   **WhatsApp Business account with both people added as agents**, then replace every
   `wa.me/` number with that one. That is the only real solution, and it is free.

2. **The postal address.** The recovered pages say "Mohali, Punjab, India" and nothing more,
   because the old site's address (Sector 108) and the current Google Business Profile
   (Sector 70) disagree and I would not guess. **For local SEO this is worth fixing** — put
   the real street address into `tools/shell.py` (`footer()`) and `/contact-us/`, and add
   `LocalBusiness` structured data while you are there.

3. **The five client pages need your facts.** `/jcbl/`, `/nahar-group-of-companies/`,
   `/amit-engineers-mohali/`, `/shoolini-university/` and `/r-b-university-mohali/` state the
   relationship and describe the problems that are genuinely common in each sector. They
   contain **no invented outcomes, metrics or scopes of work**, because the old pages carried
   none and nothing should be made up about a named client. Send the real engagement facts —
   what the brief was, what changed, any number you are allowed to publish — and they become
   proper case studies. Get the client's sign-off first; a logo on a private profile deck and
   a named case study on a public site are not the same permission.

4. **One claim to confirm:** the recovered pages say candidates are **never charged a fee**.
   That comes from a client testimonial on your own old site ("best job options to capable
   candidates at zero charges"). If it is not an absolute policy, soften it in
   `tools/content.py`.

5. **Two dates disagree, and one of them is wrong.** The current `index.html` says
   **since 2019** (hero, `7+ yrs`, and `foundingDate: 2019-04` in the JSON-LD). Google's
   snippets of the *old* site say AllAboutHR was **founded in April 2023**. The recovered
   pages follow the current site and say 2019 throughout. Decide which is right — if it is
   2023, `since 2019`, `7+ yrs` and the JSON-LD on the main site all need correcting too.

6. **The old `/job-openings/` page listed real vacancies** (Google still has a snippet of a
   "Technical Support Executive, Karnal, 0–10 years, max 6 LPA"). The recovered page does not
   list roles — it explains how to send a CV instead, because a hard-coded list goes stale and
   I had no live mandates to put there. If you want vacancies back, add them in
   `tools/content.py` under the job-openings entry. **If you do, add `JobPosting` structured
   data too** — it is what gets a role into the Google Jobs box. Do not add `JobPosting`
   markup for roles that are not genuinely open.

7. **The canonical domain** in the JSON-LD block in `index.html` (`https://allabouthr.co`),
   and `SITE` at the top of `tools/shell.py` if that ever changes.

8. **The proof figures** in the hero — `7+ yrs`, `500+`, `50+`, `125+`. Make sure each is
   defensible; they are the first numbers a visitor reads, and the recovered pages repeat
   them.

9. **Nothing is priced on the site.** Prices were deliberately removed — every package and
   every Kinexus offering is quoted after a conversation. If you ever want prices back on the
   packages page, they go inside each `.pack` card above the outcome line.

## SEO (4 October 2026)

`python tools/seo_audit.py` audits every page — including `index.html`, which
`check_pages.py` skips. It reports; it does not fix. Current state: **0 high, 0 medium,
1 low**, down from 2 high / 6 medium / 8 low.

### What was wrong, and what changed

**`index.html` was the weakest page on the site** — the opposite of what you want, since it
is the only URL Google has ever indexed.

| Was | Now |
|---|---|
| `<title>AllAboutHR</title>` — 10 characters, no keywords | `AllAboutHR — HR Consulting and HR Software, Mohali` (also updated in the JS route table so the two agree) |
| Description 193 chars — truncated in results | 155 chars |
| No canonical | Self-referencing canonical |
| **Zero Open Graph tags** — every share rendered as a blank grey box | Full OG + Twitter card set with a real image |
| **Zero crawlable internal links** — Google landed on `/` and found nowhere to go | 11 real links in the footer |
| `Organization` schema only | `Organization` + `ProfessionalService` + `WebSite`, with address, phone, email, logo, `knowsAbout` and verified `sameAs` |
| 6 images with no dimensions | Intrinsic `width`/`height` on all of them |

### The share card

`assets/og-cover.png` (1200×630, 97 KB) is generated by `python tools/make_og_image.py` —
brand gradient, logo, headline, URL. Regenerate it if the positioning line changes.

This matters more than it looks: **WhatsApp is the business's main inbound channel**, and
until now every link shared there previewed as a blank box.

### Structured data

One linked entity graph rather than repeated loose copies. `index.html` defines
`#organization` and `#website`; every recovered page references them by `@id`.

| Type | Where |
|---|---|
| `Organization` + `ProfessionalService` | `index.html` — the business, with address, phone, `sameAs` |
| `WebSite` | `index.html` |
| `WebPage` + `BreadcrumbList` | every recovered page |
| `ProfilePage` + 2 × `Person` | `/our-team/` — the founders as entities |
| `ContactPage` + `ProfessionalService` | `/contact-us/` |

**`sameAs` points at two profiles recovered from the old site and confirmed live:**
`linkedin.com/company/allabouthumanresource` and `facebook.com/allabouthumanresource`. If
there are others (Instagram, a Google Business Profile URL), add them in the
`Organization` block — they are how Google ties the entity together.

**Deliberately not added: `FAQPage`.** Google restricted FAQ rich results to government and
health sites in August 2023, so the markup earns a business site nothing. The audit does not
check for it, and there is a comment in `seo_audit.py` saying why, so it doesn't get
cargo-culted back in.

### The four commercial pages (added)

Consulting, Alvora, Kinexus and Packages existed **only as hash routes**, which Google does
not treat as separate pages — so the four things the business actually sells had no URL
anyone could land on, link to or rank. They now have real paths:

| Path | Words | Schema |
|---|---|---|
| `/packages/` | 1,162 | `OfferCatalog` with all six packages as `Offer` → `Service` |
| `/consulting/` | 1,124 | `Service` + `OfferCatalog` for the five Growth Loop steps |
| `/kinexus/` | 1,008 | `Service` + `OfferCatalog` (Baseline, Foundation, Agents) |
| `/alvora/` | 767 | `ItemList` of four `SoftwareApplication` nodes |

They are **not copies of the SPA panels.** The facts are the same — `index.html` is the
source of truth — but each is written to stand alone and goes deeper than the panel it
corresponds to. The hash routes stay as the interactive version; these are the front doors.
There is no duplicate-content risk, because the hash routes were never separate URLs.

Three things changed with them:

- **Nav and footer across the whole site now point at the real pages**, not `/#/consulting`.
  The homepage went from 0 crawlable internal links to **15**.
- **The `_redirects` rules that pointed `/packages` → `/#/packages` were removed** — they
  would have shadowed the real pages. `/pricing`, `/hr-consulting`, `/hrms` and `/software`
  now redirect *to* them instead.
- `/packages/` carries `priority 1.0` in the sitemap. It is the highest-intent page on the
  site.

### Accepted as-is

`index.html` reports 8 `<h1>` elements — one per hash route, since all eight live in one
document and seven are `display:none`. Google renders JavaScript and sees only the active
one. Restructuring the SPA's headings would risk the live site for no real gain.

## Founding date corrected to 2023

The site said **2019** in four places and `foundingDate: 2019-04` in the structured data.
Google's snippets of the old site said **April 2023**. 2023 is correct, and everything now
says so: the hero eyebrow, the JSON-LD, the share card and every page that mentioned it.

**One number had to move with it.** The founder bio said *"twelve years inside corporate HR
teams before starting AllAboutHR"* alongside *"19+ years in HR"* — which added up only while
the founding year was 2019. With a 2023 founding, 12 + 3.5 = 15.5, not 19. The old site's own
wording was *"over 15 years of corporate experience"*, which reconciles exactly, so the bio
now reads **fifteen years** in corporate HR. 15.5 + 3.5 ≈ 19. **Worth confirming.**

The `7+ yrs / In business` hero stat is now **`3+ yrs`** (April 2023 → October 2026). It is a
weaker number, but it is the true one. If you would rather lead with something else there,
`500+ placements` or `50+ organisations` are both stronger and both already on the page.

## After deploying — tell Google

The pages exist now, but Google will not notice quickly on its own.

1. In **Google Search Console**, submit `https://allabouthr.co/sitemap.xml`.
2. Use **URL Inspection → Request indexing** on the six URLs that were already indexed and
   broken: `/about-us/`, `/our-team/`, `/job-openings/`, `/nahar-group-of-companies/`,
   `/amit-engineers-mohali/`, `/we-help-you-to-make-business-stratgey/`.
3. Check **Pages → Not found (404)** a week later. It should be emptying.

## What is built in

- **Brand tokens** straight from the house brand board — plum `#933686`, teal `#0174A0`,
  ink, slate, mist, canvas. Every colour is a CSS custom property; change the token and the
  whole site follows. `assets/site.css` reuses the token block from `index.html` verbatim,
  so the recovered pages cannot drift out of brand.
- **Light and dark**, handled in all three states: OS preference, explicit choice via the
  toggle, and the un-stamped default. The recovered pages follow OS preference — they have
  no toggle, because they carry no JavaScript at all.
- **Accessibility** — skip link, semantic landmarks, visible focus rings, ARIA on the tabs
  and the mobile menu, breadcrumbs with `aria-current`, and a full `prefers-reduced-motion`
  path that turns off every animation.
- **SEO** — per-page titles, meta descriptions, canonicals, Open Graph, `WebPage` and
  `BreadcrumbList` JSON-LD on every recovered page, plus `Organization` markup with the six
  package offers on the main site.
- **Performance** — the recovered pages are about 10 KB each and make three requests
  (document, one shared stylesheet, one shared 12 KB logo). No JavaScript, no layout shift.

## The illustrations

The six illustrations in `index.html` are **hand-drawn SVG, written specifically for this
site** — an evidence trail turning into a rating, scattered spreadsheets becoming one
system, three packages with one chosen, two people at a table, a message reaching a person,
and everything landing on one desk.

**They are not unDraw art, and here is why.** unDraw's licence expressly prohibits
"automated and non-automated ways to link, embed, scrape, search or download the assets"
without their consent, and the hosted preview also blocks images loaded from other sites.
Drawing them instead sidesteps the licence question entirely and gives a better result: they
use your exact brand colours as CSS variables, so they recolour themselves correctly in dark
mode, they weigh about 12 KB for all six, and they show your actual propositions rather than
a generic stock scene.

## The logo

The header and footer use a **horizontal lockup** — mark on the left, wordmark and tagline
on the right — composed from your existing stacked artwork.

This is worth keeping for one practical reason: in the stacked version, at the 32px height a
header allows, the words "ALL ABOUT HR" were an unreadable smudge. Horizontal, they are
legible at the same height.

`index.html` carries it as a data URI. The recovered pages share one file,
`assets/logo.webp` (1205×160, 12 KB), extracted from that data URI so it is cached once
across the whole site.

Because the source is raster, the lockup is too. If you get the vector original, the same
arrangement rebuilds in minutes and will be sharp at any size.

## The founders section

Two cards on the About page, and a fuller version at `/our-team/`. **Mahavir Singh
(Co-founder & CEO)** is drawn from the profile deck. **Surbhi Goyal (Co-founder & CTO)** is
drawn from kinexus.co.in and its portfolio page — the career to date, the 15 years at the
European HR platform, growing that India team from 1 to 150+ at under 2% attrition, ISO
27001 lead auditor, and the line about adoption being the deliverable.

## The client logos and the founder photos

Both came out of `AllAboutHR Profile 2K26.pdf` — client logos across eight sectors, plus the
portraits. They are embedded as WebP data URIs, so `index.html` still makes no outside
requests, but they are the reason the file is around 570 KB. That is still one request and
still fast; if you ever want it smaller, the client wall is where the weight is.

**Two things to check before this goes public.** Showing a client's logo on a private
profile deck and showing it on a public website are not quite the same thing — most clients
are happy, some have brand rules, and a few contracts say ask first. Worth a quick sweep,
and it matters more now that five of them have pages of their own. And **Kinexus appears as
a client in the deck**; it is left out of the wall, because listing your own company among
your clients reads oddly on your own site.

Logos are drawn from the deck at the resolution they were embedded at. A few are soft at
large sizes — if a client sends you a clean SVG or a high-resolution PNG, it drops straight
in.

## Known limits — read these

- **The logos are raster.** They are WebP conversions of the files in the Branding folder.
  They will look soft on a very high-density screen and cannot be recoloured. **Replace them
  with the SVG originals** when you get them — that is the single biggest quality upgrade
  available, and the brand kit already flags it as the first action.
- **Because the logo files have white backgrounds**, the site puts them on a small white
  plate in dark mode. With SVGs that plate can be removed.
- **The typeface is Poppins**, chosen to match the character of the wordmarks. It has not
  been confirmed against the original artwork — see the brand kit.
- **The theme choice does not persist** between the main site and the recovered pages. The
  toggle in `index.html` sets an attribute in memory and nothing is stored, so a recovered
  page always follows the operating system. Fixing it means writing the choice to
  `localStorage` and reading it back on every page.
- **No CMS.** Content is edited by editing the HTML, or `tools/` for the recovered pages.
  For a site this size that is usually a feature, not a limitation.
- **The stream chooser and the Growth Loop stages** hold their state in memory only. Nothing
  is stored and nothing is tracked.

---

**Powered by AllAboutHR.co**
