# -*- coding: utf-8 -*-
"""Hub pages: /clients/ and /testimonials/.

These did not exist on the old site, and they are not in Google's index. They
are here because without them the five client pages and the three testimonial
pages are orphans — nothing links to them except each other's "where to next"
cards, which is a poor signal to a crawler and makes them hard to find for a
human too.

Both hubs are linked from the footer of every page, so everything recovered is
now reachable in two clicks from anywhere on the site.
"""

from content import HOME, add

# --- /clients/ --------------------------------------------------------------

CLIENT_GROUPS = [
    ("Manufacturing, engineering &amp; industrial", [
        ("/nahar-group-of-companies/", "Nahar Group of Companies",
         "A large manufacturing group. Accounts and finance placements among the work."),
        ("/jcbl/", "JCBL",
         "An established manufacturing and engineering group in north India."),
        ("/amit-engineers-mohali/", "Amit Engineers, Mohali",
         "A growing engineering business, local to us in Mohali."),
    ]),
    ("Education &amp; training", [
        ("/shoolini-university/", "Shoolini University",
         "A leading private university in Himachal Pradesh."),
        ("/r-b-university-mohali/", "Rayat Bahra University, Mohali",
         "A large private university in Punjab, also listed as R B University."),
    ]),
]


def group_html(groups):
    out = []
    for title, rows in groups:
        cards = "".join(
            '<a class="card hov" href="%s"><h4>%s</h4><p>%s</p>'
            '<p class="go">Read more &rarr;</p></a>' % (href, name, blurb)
            for href, name, blurb in rows)
        out.append('      <h2>%s</h2>\n      <div class="nextrow" style="margin-bottom:26px">%s</div>'
                   % (title, cards))
    return "\n".join(out)


add(
    slug="clients",
    title="Our Clients — AllAboutHR",
    meta=("Fifty-plus organisations across fifteen industries have worked with AllAboutHR "
          "since 2023 — manufacturing, engineering, education, healthcare, IT and more."),
    eyebrow="Our clientele",
    h1="Fifty-plus organisations, across fifteen industries.",
    lede=("Manufacturing floors, hospitals, universities, chartered accountants, logistics "
          "yards. The problems rhyme more than most owners expect — which is why the same "
          "five steps work in all of them."),
    trail=[HOME, (None, "Clients")],
    content="""%s
      <h2>The full wall</h2>
      <p>The pages above are the clients who had their own page on our previous site. The
      complete list — fifty-plus organisations grouped by sector — is the wall above. How
      the house came together is on the <a href="/about-us/">about page</a>.</p>

      <div class="note">
        <h4>Ask for a reference, not a case study</h4>
        <p>We would rather put you in touch with an organisation in your own industry than
        send you something we wrote about ourselves. <a href="/contact-us/">Ask us</a> and we
        will arrange it.</p>
      </div>

      <h2>What clients say</h2>
      <p>Three accounts in full, from a chartered accountancy firm and two candidates, are on
      the <a href="/testimonials/">testimonials page</a>. There are 125+ five-star reviews on
      <a href="https://www.google.com/maps/place/?q=place_id:ChIJs49QZn_pDzkRCLf3CWTHPVo" target="_blank" rel="noopener">Google</a>.</p>""" % group_html(CLIENT_GROUPS),
    cards=[
        ("/testimonials/", "p", "Proof", "Testimonials",
         "What clients and candidates said, in their own words and in full.",
         "Read them"),
        ("/why-choose-allabouthr/", "p", "Promises", "Why choose AllAboutHR",
         "Four promises with numbers attached, and the step most HR firms skip.",
         "Read the promises"),
        ("/service-best-expert-solution/", "t", "Services", "Everything we do",
         "Consulting, Alvora software and Kinexus systems, in one place.",
         "See the services"),
    ],
    cta_h2="Want to speak to one of them?",
    cta_p=("Tell us your industry and we will put you in touch with a client in it. That is "
           "worth more than anything we could write ourselves."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20could%20I%20speak%20to%20a%20client%20reference%20in%20my%20industry%3F",
    cta_second=("/about-us/", "Read the company story"),
)

# --- /testimonials/ ---------------------------------------------------------

TESTIMONIALS = [
    ("/dinesh-garg/", "CA Dinesh Garg", "CEO, Chartered Accountants&rsquo; firm, Mohali",
     "They worked so hard and sent us approx 50+ resumes, out of which we chose approx 20 "
     "and after interviewing those candidates, we hired 5 appropriate candidates that were "
     "fit for the profile. Now I have a good team."),
    ("/pinky-bansal-an-accounting-candidate/", "Pinky Bansal", "An accounting candidate, "
     "placed at Nahar Group of Companies",
     "Wonderful HR consulting services in Mohali and Chandigarh. They are giving the best "
     "job options to capable candidates at zero charges."),
    ("/bulbul-pachar-a-fresher-candidate/", "Bulbul Pachar", "A fresher candidate",
     "Thank you for helping me identify my hidden talents and work towards pursuing my dream "
     "goals. A best-guiding and human resource consulting company."),
]

quotes = "".join(
    '      <blockquote>\n        <p>%s</p>\n        <cite>%s &mdash; %s &middot; '
    '<a href="%s">read it in full</a></cite>\n      </blockquote>\n'
    % (quote, name, role, href)
    for href, name, role, quote in TESTIMONIALS)

add(
    slug="testimonials",
    title="Testimonials — What Our Clients and Candidates Say — AllAboutHR",
    meta=("What clients and candidates say about AllAboutHR, in their own words — a Mohali CA "
          "firm, an accounting candidate and a fresher. Plus 125+ five-star Google reviews."),
    eyebrow="What our clients say",
    h1="In their own words.",
    lede=("Three accounts given to us over the years, reproduced exactly as they were written. "
          "Nothing here has been tidied up or shortened."),
    trail=[HOME, (None, "Testimonials")],
    content="""%s
      <div class="note">
        <h4>Reproduced word for word</h4>
        <p>These are real quotes from real people and have not been edited. Each name links to
        the full version with the background to it.</p>
      </div>

      <h2>125+ five-star reviews</h2>
      <p>Beyond these three, the businesses and candidates we have worked with since 2023 have
      left more than 125 five-star reviews on Google. You can
      <a href="https://www.google.com/maps/place/?q=place_id:ChIJs49QZn_pDzkRCLf3CWTHPVo" target="_blank" rel="noopener">read them</a>, or <a href="https://search.google.com/local/writereview?placeid=ChIJs49QZn_pDzkRCLf3CWTHPVo" target="_blank" rel="noopener">add your own</a>.</p>

      <h2>If it did not go well</h2>
      <p>If a project did not go the way you hoped, tell us first rather than the internet.
      <a href="/contact-us/">Send it straight to us</a> and one of the founders will reply.
      That offer is not decorative — the last step of how we work is checking whether what we
      did actually moved your numbers, and saying so when it did not.</p>""" % quotes,
    cards=[
        ("/clients/", "p", "Clients", "Our clients",
         "Fifty-plus organisations across fifteen industries, and the five with their own page.",
         "See the clients"),
        ("/job-openings/", "p", "Candidates", "Looking for a job?",
         "Send your CV. We are paid by the employer, never by you.",
         "Send your CV"),
        ("https://search.google.com/local/writereview?placeid=ChIJs49QZn_pDzkRCLf3CWTHPVo", "t", "Google", "Leave a review",
         "Worked with us? Two minutes, and it helps the next business choose well.",
         "Write a review"),
    ],
    cta_h2="Want this to be your experience?",
    cta_p=("Whether you are hiring or looking for a role, one message is enough to start. You "
           "will get a straight answer either way."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20read%20your%20testimonials%20and%20would%20like%20to%20talk.",
    cta_second=("https://www.google.com/maps/place/?q=place_id:ChIJs49QZn_pDzkRCLf3CWTHPVo", "Read the Google reviews"),
)
