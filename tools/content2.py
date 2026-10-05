# -*- coding: utf-8 -*-
"""Client pages, client testimonials and the three service posts.

IMPORTANT — on the five client pages: the old site carried these URLs but almost
no copy behind them (the archived homepage shows only the client name and the
word "Analysis"). Nothing here invents an outcome, a metric or a scope of work
for a named client. Each page states the relationship plainly, describes the
HR problems that are genuinely common in that sector, and offers a reference.
If you want these pages to carry real case-study detail, send the engagement
facts and they drop straight in — see README.md.

The three candidate and client testimonials ARE reproduced verbatim from the
archived site, because they are real quotes given by real people.
"""

from content import HOME, add, C_CLIENTS
from shell import esc

# --- clients ----------------------------------------------------------------

CLIENT_COMMON = """
      <h2>Working with us</h2>
      <p>Client engagements run through the five steps of our
      <a href="/consulting/">Growth Loop</a> — see what is true, shape the system, source
      the right people, strengthen them, and sustain it with evidence. Which steps apply
      depends entirely on what a health check finds, and we start there rather than arriving
      with a fixed answer.</p>

      <div class="note">
        <h4>Want to speak to a client directly?</h4>
        <p>We would rather put you in touch with an organisation in your own industry than send
        you a case study we wrote about ourselves.
        <a href="/contact-us/">Ask us for a reference</a> and we will arrange it.</p>
      </div>"""


def client(slug, name, title, meta, sector, lede, intro, problems, services,
           extra=""):
    prob = "".join("<li>%s</li>" % p for p in problems)
    serv = "".join("<li>%s</li>" % s for s in services)
    # "Manufacturing &amp; engineering" reads badly mid-sentence; spell it out.
    sector_prose = sector.replace("&", "and").lower()
    add(
        slug=slug,
        title=title,
        meta=meta,
        eyebrow="Client · %s" % sector,
        h1=name,
        lede=lede,
        trail=[HOME, ("/clients/", "Clients"), (None, name)],
        content="""      <dl class="facts">
        <div><dt>Client</dt><dd>%s</dd></div>
        <div><dt>Sector</dt><dd>%s</dd></div>
        <div><dt>Relationship</dt><dd>An AllAboutHR client &mdash; listed on our client wall</dd></div>
        <div><dt>Based</dt><dd>North India</dd></div>
      </dl>

%s

      <h2>What usually needs fixing in this sector</h2>
      <p>Across the organisations we work with in %s, the same handful of problems keep coming
      up. They are worth naming, because most owners assume theirs is unique:</p>
      <ul>%s</ul>

      <h2>Where we help</h2>
      <ul>%s</ul>
%s%s""" % (esc(name), esc(sector), intro, sector_prose, prob, serv, extra, CLIENT_COMMON),
        cards=C_CLIENTS,
        cta_h2="Facing the same problems?",
        cta_p=("Tell us what is going wrong. A thirty-minute call costs nothing, and you will "
               "leave it clearer about your actual problem than when you came in."),
        wa="Hi%20AllAboutHR%20%E2%80%94%20I%20saw%20your%20client%20page%20and%20would%20like%20to%20talk%20about%20my%20organisation.",
        cta_second=("/clients/", "See every client"),
    )


client(
    slug="nahar-group-of-companies",
    name="Nahar Group of Companies",
    title="Nahar Group of Companies — Client — AllAboutHR",
    meta=("Nahar Group of Companies is an AllAboutHR client. Recruitment and HR support for a "
          "large north Indian manufacturing group, including accounts and finance placements."),
    sector="Manufacturing & industrial",
    lede=("A large manufacturing group in north India, and one of the organisations on our "
          "client wall. Among the placements we have made there are accounts and finance "
          "roles."),
    intro="""      <p>Nahar Group of Companies is one of the fifty-plus organisations we have worked with
      since 2023, and sits in the manufacturing and industrial group on
      <a href="/clients/">our client wall</a>.</p>
      <p>One placement there is a matter of public record, because the candidate wrote about it
      herself:</p>
      <blockquote>
        <p>Placed at Nahar Group of Companies Mohali Punjab. Wonderful HR consulting services in
        Mohali and Chandigarh. They are giving the best job options to capable candidates at
        zero charges.</p>
        <cite>Pinky Bansal, an accounting candidate &mdash;
        <a href="/pinky-bansal-an-accounting-candidate/">read her full testimonial</a></cite>
      </blockquote>""",
    problems=[
        "<strong>Shop floor and office run on different rules.</strong> Attendance, overtime and "
        "leave are handled one way in the plant and another in the office, and nobody can "
        "produce one number for the group.",
        "<strong>Statutory exposure across multiple units.</strong> EPF, ESIC, contract labour "
        "and POSH obligations multiply with every unit and every contractor.",
        "<strong>Contractor workforce invisible to HR.</strong> A large share of the people on "
        "site are not on the payroll, so their papers, compliance and timesheets live in a "
        "different world.",
        "<strong>Appraisals that cannot be defended.</strong> With long-service staff and "
        "family-run decision making, increment season becomes a negotiation rather than a "
        "process.",
    ],
    services=[
        "<strong>Recruitment</strong> &mdash; accounts, finance, engineering and plant roles "
        "through <a href=\"/jobs/\">search and bulk hiring</a>, with background checks.",
        "<strong>Compliance you can prove</strong> &mdash; a record you could hand straight to "
        "an inspector, plus POSH end to end.",
        "<strong>Alvora HRMS</strong> &mdash; one system for records, leave, attendance, shifts "
        "and payroll across units.",
        "<strong>Alvora Gig</strong> &mdash; joining papers, compliance documents, timesheets "
        "and payments for contractor and vendor staff.",
    ],
)

client(
    slug="jcbl",
    name="JCBL",
    title="JCBL — Client — AllAboutHR",
    meta=("JCBL is an AllAboutHR client. HR and recruitment support for an established north "
          "Indian manufacturing and engineering group."),
    sector="Manufacturing & engineering",
    lede=("An established manufacturing and engineering group in north India, and one of the "
          "organisations on our client wall."),
    intro="""      <p>JCBL is one of the fifty-plus organisations we have worked with since 2023, and sits
      in the manufacturing, engineering and industrial group on
      <a href="/clients/">our client wall</a>.</p>""",
    problems=[
        "<strong>Skilled trades are hard to replace.</strong> Fabricators, welders, quality "
        "inspectors and maintenance engineers take months to find and days to lose to a "
        "competitor paying a little more.",
        "<strong>Nobody knows the real cost per job.</strong> Labour, rework and overtime are "
        "reconstructed at month-end, by which time it is far too late to change anything.",
        "<strong>Supervisors were promoted for technical skill.</strong> The best fabricator "
        "becomes the supervisor, and then nobody develops them as a manager.",
        "<strong>Training happens but is never measured.</strong> Safety and skills training is "
        "delivered and signed for, and no record connects it to whether anyone got better.",
    ],
    services=[
        "<strong>Recruitment</strong> &mdash; engineering, quality, production and plant HR "
        "roles via <a href=\"/jobs/\">search and bulk hiring</a>.",
        "<strong>Job levels and honest rating scales</strong> so two supervisors score the same "
        "person the same way.",
        "<strong><a href=\"/training/\">Manager development</a></strong> for supervisors "
        "promoted on technical strength.",
        "<strong>Kinexus Systems</strong> &mdash; a <a href=\"/kinexus/\">Baseline</a> that "
        "counts the hours lost re-typing information between the shop floor and the office.",
    ],
)

client(
    slug="amit-engineers-mohali",
    name="Amit Engineers, Mohali",
    title="Amit Engineers Mohali — Client — AllAboutHR",
    meta=("Amit Engineers, Mohali is an AllAboutHR client. HR, compliance and recruitment "
          "support for a growing engineering business in Punjab."),
    sector="Engineering",
    lede=("An engineering business in Mohali, Punjab, and one of the organisations on our "
          "client wall."),
    intro="""      <p>Amit Engineers is one of the fifty-plus organisations we have worked with since 2023,
      and sits in the manufacturing, engineering and industrial group on
      <a href="/clients/">our client wall</a>. They are also local to us &mdash; we are both in
      Mohali.</p>""",
    problems=[
        "<strong>Everything waits for the owner.</strong> Leave, hiring, salary, a complaint "
        "&mdash; nothing moves until one person decides it, and a week away slows the whole "
        "business down.",
        "<strong>The paperwork is a worry nobody has time for.</strong> Registrations, filings "
        "and statutory records are handled when something forces the issue rather than on a "
        "calendar.",
        "<strong>No written process.</strong> Joining, exit and appraisal all happen differently "
        "depending on who is dealing with it, so nothing can be delegated.",
        "<strong>Growing past the point where memory works.</strong> Somewhere between twenty "
        "and fifty people, running HR out of a shared spreadsheet and a WhatsApp group quietly "
        "stops working.",
    ],
    services=[
        "<strong>Compliance on a calendar</strong> &mdash; reminders, filings, POSH policy and "
        "committee, and registration help for EPF, ESIC, Shops &amp; Establishment and PT.",
        "<strong>Written processes and a full letter set</strong> &mdash; contracts, appointment "
        "and relieving letters, leave, conduct and attendance policy.",
        "<strong>Alvora HRMS</strong> so leave and claims are done by staff on their phones "
        "rather than by the owner.",
        "<strong>Recruitment</strong> for engineering and office roles through "
        "<a href=\"/jobs/\">our hiring work</a>.",
    ],
)

client(
    slug="shoolini-university",
    name="Shoolini University",
    title="Shoolini University — Client — AllAboutHR",
    meta=("Shoolini University is an AllAboutHR client. HR, recruitment and campus hiring work "
          "with a leading private university in Himachal Pradesh."),
    sector="Education",
    lede=("A leading private university in Himachal Pradesh, and one of the organisations on "
          "our client wall."),
    intro="""      <p>Shoolini University is one of the fifty-plus organisations we have worked with since
      2023, and sits in the education and training group on
      <a href="/clients/">our client wall</a>.</p>
      <p>Universities sit on both sides of our business at once: they are employers with their
      own HR to run, and they are where the next intake of talent comes from. Our campus
      programme, <a href="/recruitxcel/">RecruitXcel</a>, exists because of partnerships like
      this one.</p>""",
    problems=[
        "<strong>Two very different workforces under one roof.</strong> Faculty and "
        "administrative staff need different hiring, appraisal and progression rules, and a "
        "single HR policy serves neither well.",
        "<strong>Hiring is seasonal and then urgent.</strong> Faculty recruitment concentrates "
        "around the academic calendar, so the same work has to be done in a fraction of the "
        "year.",
        "<strong>Appraisals have to withstand scrutiny.</strong> Academic promotion criteria are "
        "formal, which means the evidence behind every rating has to exist and be findable.",
        "<strong>Placement outcomes are the product.</strong> How well students are placed drives "
        "the next intake, so employability training is not a side activity.",
    ],
    services=[
        "<strong>Recruitment</strong> for faculty, administrative and operations roles, with "
        "<a href=\"/jobs/\">background checks</a>.",
        "<strong><a href=\"/recruitxcel/\">RecruitXcel</a> and campus programmes</strong> &mdash; "
        "employability skills, CV and interview preparation for students.",
        "<strong>Evidence-linked appraisals</strong> through Alvora HRMS, so a rating can always "
        "be traced to the document behind it.",
        "<strong>Alvora Learning</strong> &mdash; staff training delivered and tracked against "
        "one skills list.",
    ],
)

client(
    slug="r-b-university-mohali",
    name="Rayat Bahra University, Mohali",
    title="Rayat Bahra University Mohali — Client — AllAboutHR",
    meta=("Rayat Bahra University, Mohali is an AllAboutHR client. HR, recruitment and campus "
          "hiring work with a large private university in Punjab."),
    sector="Education",
    lede=("A large private university in Mohali, Punjab, and one of the organisations on our "
          "client wall. Also listed as R B University."),
    intro="""      <p>Rayat Bahra University is one of the fifty-plus organisations we have worked with
      since 2023, and sits in the education and training group on
      <a href="/clients/">our client wall</a>. They are local to us, in Mohali.</p>
      <p>As with every institution we work with, the relationship runs in both directions: a
      university is an employer with its own HR function to run, and it is also where a large
      part of the next intake of talent comes from.</p>""",
    problems=[
        "<strong>Scale makes small inconsistencies expensive.</strong> With hundreds of staff "
        "across departments, a rule applied three different ways becomes a dispute rather than "
        "an irritation.",
        "<strong>Faculty and support staff need different systems.</strong> Academic progression "
        "and administrative grading are not the same thing, and forcing one framework on both "
        "satisfies nobody.",
        "<strong>Hiring peaks around the academic calendar.</strong> A year of recruitment gets "
        "compressed into a few months, every year.",
        "<strong>Student employability is measured by employers, not by the institution.</strong> "
        "Placement results depend on how students present themselves, which is a trainable "
        "skill.",
    ],
    services=[
        "<strong>Recruitment</strong> for faculty, administration and operations, at volume when "
        "the calendar demands it &mdash; see <a href=\"/jobs/\">our hiring work</a>.",
        "<strong>Campus and employability programmes</strong>, including "
        "<a href=\"/recruitxcel/\">RecruitXcel</a> for students targeting recruitment and HR "
        "careers.",
        "<strong>Job levels, grades and reporting lines</strong> that work for academic and "
        "administrative staff separately.",
        "<strong>Alvora HRMS</strong> for records, leave, attendance and appraisals at "
        "institutional scale.",
    ],
)

# --- testimonials -----------------------------------------------------------

TESTI_NOTE = """
      <div class="note">
        <h4>Where this came from</h4>
        <p>This is reproduced word for word as it was given to us. You can read more of what
        clients and candidates say on our <a href="/testimonials/">testimonials page</a>, which links
        through to 125+ five-star reviews on Google.</p>
      </div>"""

TESTI_CARDS = [
    ("/testimonials/", "p", "Reviews", "More reviews",
     "125+ five-star Google reviews from the businesses and candidates we have worked with.",
     "Read them"),
    ("/job-openings/", "p", "Candidates", "Looking for a job?",
     "Send your CV. We are paid by the employer, never by you.",
     "Send your CV"),
    ("/jobs/", "t", "Employers", "Hiring?",
     "Search, bulk, campus and leadership hiring, with background checks.",
     "For employers"),
]


def testimonial(slug, name, who, title, meta, eyebrow, lede, quote, intro, outro=""):
    q = "".join("<p>%s</p>" % p for p in quote)
    add(
        slug=slug,
        title=title,
        meta=meta,
        eyebrow=eyebrow,
        h1=name,
        lede=lede,
        trail=[HOME, ("/testimonials/", "Testimonials"), (None, name)],
        content="""%s

      <blockquote>
        %s
        <cite>%s</cite>
      </blockquote>
%s%s""" % (intro, q, who, outro, TESTI_NOTE),
        cards=TESTI_CARDS,
        cta_h2="Want this to be your experience?",
        cta_p=("Whether you are hiring or looking, one message is enough to start. You will get "
               "a straight answer either way."),
        wa="Hi%20AllAboutHR%20%E2%80%94%20I%20read%20a%20testimonial%20on%20your%20site%20and%20would%20like%20to%20talk.",
        cta_second=("/testimonials/", "Read more reviews"),
    )


testimonial(
    slug="pinky-bansal-an-accounting-candidate",
    name="Pinky Bansal: an accounting candidate",
    who="Pinky Bansal, placed at Nahar Group of Companies, Mohali, Punjab",
    title="Pinky Bansal, An Accounting Candidate — AllAboutHR",
    meta=("An accounting candidate placed by AllAboutHR at Nahar Group of Companies, Mohali: "
          "“they are giving the best job options to capable candidates at zero charges.”"),
    eyebrow="What our candidates say",
    lede=("An accounts placement at a large manufacturing group — and a reminder that we are "
          "paid by the employer, never by the candidate."),
    intro="""      <p>Pinky Bansal came to us as an accounting candidate and was placed at
      <a href="/nahar-group-of-companies/">Nahar Group of Companies</a> in Mohali, Punjab.</p>""",
    quote=["Placed at Nahar Group of Companies Mohali Punjab. Wonderful HR consulting services "
           "in Mohali and Chandigarh. They are giving the best job options to capable candidates "
           "at zero charges."],
    outro="""
      <h2>The part worth repeating</h2>
      <p><strong>Zero charges.</strong> We do not charge a candidate to register, to interview or
      to join. Our fee is paid by the employer. If anybody ever asks you for money in our name,
      tell us.</p>
      <p>If you are looking for an accounts or finance role, <a href="/job-openings/">send us
      your CV</a> with the role you want, your location and notice period, and your expected
      salary.</p>""",
)

testimonial(
    slug="dinesh-garg",
    name="Dinesh Garg, CEO of a CA firm in Mohali",
    who="CA Dinesh Garg, CEO, Chartered Accountants&rsquo; firm, Mohali",
    title="Dinesh Garg (CEO, CA Firm Mohali) — AllAboutHR",
    meta=("A Mohali chartered accountancy firm on hiring with AllAboutHR: 50+ resumes, 20 "
          "interviewed, 5 hired. “Now I have a good team.”"),
    eyebrow="What our clients say",
    lede=("A chartered accountancy firm that had struggled for a long time to find accounting "
          "staff with the depth of knowledge the work needed."),
    intro="""      <p>One of the clearest accounts of how a mandate actually runs came from the CEO of a
      chartered accountancy firm in Mohali. We have left it exactly as he wrote it.</p>""",
    quote=["We are a Chartered Accountant&rsquo;s Firm. We were struggling a lot for good "
           "accounting staff with sophisticated knowledge for long. When we requested "
           "Mr. Mahavir Singh &amp; his team, they worked so hard and sent us approx 50+ "
           "resumes, out of which we chose approx 20 and after interviewing those candidates, "
           "we hired 5 appropriate candidates that were fit for the profile. Now I have a good "
           "team. I also recommended him to a few of my clients and they also appreciated his "
           "services. Thanks to Mahavir Ji. I strongly recommend him for all sorts of human "
           "resources or manpower needs.",
           "Regards, CA Dinesh Garg."],
    outro="""
      <h2>What those numbers actually describe</h2>
      <p>Fifty-plus CVs, about twenty taken to interview, five hired. That ratio is worth
      understanding rather than glossing over: specialist accounting roles have a narrow pool,
      and the work is in the screening rather than the sourcing. A pile of forwarded CVs would
      have cost this firm weeks of partner time and produced the same five hires, or fewer.</p>
      <p>This is the <strong>Flow</strong> service &mdash; permanent hiring at volume where the
      brief is specific. If that is the problem you have, <a href="/jobs/">read how a mandate
      runs</a>.</p>""",
)

testimonial(
    slug="bulbul-pachar-a-fresher-candidate",
    name="Bulbul Pachar, a fresher candidate",
    who="Bulbul Pachar, a fresher candidate",
    title="Bulbul Pachar (A Fresher Candidate) — AllAboutHR",
    meta=("A fresher candidate on career guidance from AllAboutHR: “thank you for helping "
          "me identify my hidden talents and work towards pursuing my dream goals.”"),
    eyebrow="What our candidates say",
    lede=("A first job is a different conversation from a senior hire, and it needs different "
          "help: honest feedback, and someone willing to spend the time."),
    intro="""      <p>Career guidance is the part of our work that never appears on an invoice. Bulbul
      Pachar came to us as a fresher.</p>""",
    quote=["Thanks for your support and correct guidance AllAboutHR Team, especially CEO "
           "Mahavir Sir. I appreciate you taking time out of your busy day to help me and to "
           "guide me. Thank you for helping me identify my hidden talents and work towards "
           "pursuing my dream goals. Thank you all for your valuable efforts.",
           "A best-guiding and human resource consulting company. They are really one-stop "
           "solutions for your all career related needs."],
    outro="""
      <h2>If you are starting out</h2>
      <p>We place freshers, and we will not pretend the conversation is the same as a senior
      hire. Expect honest feedback on your CV, help with how you present yourself, and a
      realistic view of what a first job pays. 100+ career guidance sessions have gone through
      the founders directly.</p>
      <p>If training would get you further than another hundred applications, we will say so
      &mdash; that is what <a href="/training/">our training</a> and
      <a href="/recruitxcel/">RecruitXcel</a> are for. And when you are ready,
      <a href="/job-openings/">send us your CV</a>.</p>""",
)

# --- the three service posts ------------------------------------------------

add(
    slug="we-help-you-to-make-business-stratgey",
    title="We Help You Craft Winning Business Strategies — AllAboutHR",
    meta=("Strategy fails on people, not on ideas. We build the org design, headcount plan, "
          "job levels and goals that let a business actually execute one."),
    eyebrow="Services",
    h1="We help you craft winning business strategies.",
    lede=("Success starts with a clear vision and the right strategy to bring it to life. We go "
          "beyond traditional HR services to partner with you in building a business that can "
          "actually execute one."),
    trail=[HOME, ("/service-best-expert-solution/", "Services"), (None, "Business strategy")],
    content="""      <h2>Strategy fails on people, not on ideas</h2>
      <p>Most strategies that go nowhere were not bad strategies. They were strategies no part
      of the organisation was built to deliver — nobody owned the number, the structure put the
      decision three levels from the information, or the people who had to execute it were never
      told what changed. That is an HR problem wearing a strategy costume.</p>

      <h2>What we actually do</h2>
      <ul>
        <li><strong>Organisation design.</strong> Who does what, who decides what, and how many
        people the plan needs — not an org chart drawn to match the people you happen to have.</li>
        <li><strong>A headcount plan with department targets.</strong> So growth is costed before
        it is promised, and every department knows the number it is answerable for.</li>
        <li><strong>Job levels and grades.</strong> The quiet foundation under pay, promotion and
        hiring. Without it, every salary conversation is improvised.</li>
        <li><strong>Goals that cascade.</strong> Company target to department target to an
        individual goal somebody agreed to. If the chain breaks anywhere, nothing lands.</li>
        <li><strong>Re-measurement.</strong> Nine to twelve months on we check the same numbers
        again. If they did not move, we say so.</li>
      </ul>

      <div class="note plum">
        <h4>We start by finding out what is true</h4>
        <p>Before designing anything we run a <strong>six-week health check</strong> — fifteen
        areas of your HR, each scored, with the evidence shown. Most owners are surprised by
        which one is worst, and that is the point: strategy built on a guess about your own
        organisation is just a more expensive guess.</p>
      </div>

      <h2>Where it sits in the Growth Loop</h2>
      <p>This is steps one and two — <strong>See</strong> and <strong>Shape</strong> — of our
      <a href="/consulting/">Growth Loop</a>. Everything else (hiring, training, appraisals,
      increments) is cheaper and works better once these two are done, which is precisely why
      we will not sell you step three first.</p>

      <h2>Have a business idea?</h2>
      <p>Share it with us. We will tell you what the people side of making it real looks like —
      how many, of what kind, by when, and what it costs. If the honest answer is that you are
      not ready for us yet, you will get that answer too.</p>""",
    cards=[
        ("/consulting/", "p", "Consulting", "The Growth Loop",
         "Five steps from “something is wrong” to “here is the proof it improved”.",
         "See how we work"),
        ("/we-provide-best-ideas-for-the-business-growth/", "p", "Growth", "Innovative HR ideas",
         "A-to-Z HR solutions, from talent acquisition to compliance management.",
         "Read more"),
        ("/packages/", "t", "Packages", "Six packages",
         "What each one includes, and when it stops being the right fit.",
         "Compare them"),
    ],
    cta_h2="Tell us where the strategy is stuck.",
    cta_p=("Usually it is not the plan. It is that nothing in the organisation is built to "
           "deliver it — and that is findable in six weeks."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20would%20like%20help%20with%20business%20strategy%20and%20org%20design.",
)

add(
    slug="we-provide-best-ideas-for-the-business-growth",
    title="Innovative HR Ideas for Business Growth — AllAboutHR",
    meta=("A-to-Z HR solutions for a growing business: talent acquisition, HR operations "
          "setup, employee development and compliance management."),
    eyebrow="Services",
    h1="We provide innovative HR ideas to propel your business growth.",
    lede=("Have a business idea? Share it with us, and we will turn it into reality with our "
          "A-to-Z HR solutions — everything you need to build and grow a team."),
    trail=[HOME, ("/service-best-expert-solution/", "Services"), (None, "HR ideas for growth")],
    content="""      <h2>A to Z, in the order that actually works</h2>
      <p>&ldquo;A-to-Z HR solutions&rdquo; is easy to say. In practice it means four blocks of
      work, and the order matters more than the list:</p>
      <ol>
        <li><strong>Talent acquisition.</strong> Search, bulk hiring, campus hiring and
        background checks — see <a href="/jobs/">our hiring work</a>.</li>
        <li><strong>HR operations setup.</strong> Records, leave, attendance and shifts, payroll
        and the full letter set, running on a system rather than on you.</li>
        <li><strong>Employee development.</strong> <a href="/training/">Training</a>, manager
        development, staff surveys and acting on what they tell you.</li>
        <li><strong>Compliance management.</strong> EPF, ESIC, gratuity, bonus, maternity and
        POSH — with a record you could hand straight to an inspector.</li>
      </ol>

      <h2>Where the innovation actually is</h2>
      <p>Not in the vocabulary. Three things we do that most HR firms do not:</p>
      <ul>
        <li><strong>We built the software.</strong> A policy in a folder gets ignored; the same
        rules inside <a href="/alvora/">the system your managers use every day</a> get
        followed. That is the difference between advice and change.</li>
        <li><strong>Every number traces to a document.</strong> A score only moves when someone
        submits proof and a manager approves it. When an employee asks why they got a rating,
        you can show them, line by line — which removes most appraisal arguments before they
        start.</li>
        <li><strong>We will talk you out of AI.</strong> We use it only where we can show you the
        hours it saves. If a simple rule or a better form would do the same job for less money,
        we build that instead, even though the AI version would earn us more.</li>
      </ul>

      <div class="note">
        <h4>Growth has a shape</h4>
        <p>What a business needs at ten people, at a hundred and at a thousand are genuinely
        different problems, and buying the wrong one is expensive. That is why there are
        <a href="/packages/">six packages</a> rather than one: each says what problem it
        solves, exactly what is included, and <strong>when it stops being the right fit</strong>
        — so you know in advance when it is time to move up.</p>
      </div>

      <h2>From talent acquisition to compliance, with one team</h2>
      <p>The reason to take all of it from one house is that the joins are where things break.
      The consultant who found the problem designs the fix; the people who build the software are
      in the same company; and nine to twelve months later the same health check runs again to
      prove whether it worked. Nobody can quietly blame the other supplier.</p>""",
    cards=[
        ("/service-best-expert-solution/", "p", "Services", "Everything we do",
         "Consulting, Alvora software and Kinexus systems, set out in one place.",
         "See the services"),
        ("/we-help-you-to-make-business-stratgey/", "p", "Strategy", "Business strategy",
         "Org design, headcount plans and goals that actually cascade.",
         "Read more"),
        ("/alvora/", "t", "Software", "Alvora",
         "Four platforms where every number traces back to the document it came from.",
         "See the platforms"),
    ],
    cta_h2="Share the idea. We will cost the people side.",
    cta_p=("How many, of what kind, by when, and what it takes to keep them. One message is "
           "enough to start."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20have%20a%20business%20idea%20and%20need%20the%20HR%20side%20built.",
)

add(
    slug="we-help-individuals-and-businesses-make-things-happen-for-their-dream",
    title="We Help Individuals and Businesses Make Things Happen — AllAboutHR",
    meta=("Career counselling, CV crafting, LinkedIn optimisation, interview prep and skills "
          "training for individuals — plus full HR support for businesses."),
    eyebrow="Services",
    h1="We help individuals and businesses make things happen.",
    lede=("For individuals, we turn career aspirations into something you can act on. For "
          "businesses, we build the HR that lets the plan happen. The two halves feed each "
          "other."),
    trail=[HOME, ("/service-best-expert-solution/", "Services"), (None, "Individuals and businesses")],
    content="""      <h2>For individuals</h2>
      <p>We help people turn career aspirations into reality — whether you are chasing a first
      job, a better one, or a change of direction. The practical help is:</p>
      <ul>
        <li><strong>Career counselling.</strong> An honest read on where you stand and what is
        realistically reachable in the next twelve months.</li>
        <li><strong>CV crafting.</strong> Written for the person actually screening it, who will
        give it about twenty seconds.</li>
        <li><strong>LinkedIn profile optimisation.</strong> So recruiters searching for your
        skills find you rather than someone else.</li>
        <li><strong>Interview preparation.</strong> Structured practice, and straight feedback on
        the answers that are letting you down.</li>
        <li><strong>Skill development training.</strong> Through
        <a href="/training/">AllAboutHR Academy</a> and
        <a href="/recruitxcel/">RecruitXcel</a>, when the gap is a skill rather than a CV.</li>
      </ul>
      <p>100+ career guidance sessions have run through the founders directly, and 500+
      candidates have been placed. We are paid by the employer, so none of this costs you a
      placement fee. <a href="/job-openings/">Send us your CV &rarr;</a></p>

      <h2>For businesses</h2>
      <p>On the other side of the same table, we build the HR a plan needs in order to happen:
      <a href="/jobs/">hiring</a>, HR operations on a system,
      <a href="/training/">development</a>, compliance you can prove, and appraisals and
      increments that stand up when challenged. Six packages cover it from ten people upwards —
      <a href="/packages/">see which one fits</a>.</p>

      <div class="note plum">
        <h4>Why we do both</h4>
        <p>Working both sides is the reason the advice is any good. We know what employers
        actually reject a CV for, because they tell us. And we know why good candidates turn
        down offers, because they tell us that too. A consultancy that only ever hears one side
        is guessing about the other.</p>
      </div>

      <h2>Whichever side you are on</h2>
      <p>The starting move is the same: tell us the real problem in a sentence or two. You will
      get questions back rather than a brochure, and if we are not the right people you will be
      told that rather than sold something.</p>""",
    cards=[
        ("/job-openings/", "p", "Individuals", "Send your CV",
         "What to put in the message, and why candidates are never charged a fee.",
         "For candidates"),
        ("/training/", "p", "Individuals", "Training",
         "Career counselling, CV and LinkedIn help, interview prep and skills training.",
         "See the programmes"),
        ("/service-best-expert-solution/", "t", "Businesses", "Everything we do",
         "Consulting, software and systems, set out in one place.",
         "See the services"),
    ],
    cta_h2="Tell us which side of the table you are on.",
    cta_p=("Hiring, or looking? Either way, one message is enough and you will get a straight "
           "answer."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20would%20like%20help%20with%20my%20career%2Fmy%20team.",
)
