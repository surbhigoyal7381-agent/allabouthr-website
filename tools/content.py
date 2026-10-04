# -*- coding: utf-8 -*-
"""Copy for the recovered AllAboutHR path-based pages.

Source of truth for every page under a real path (/about-us/, /our-team/, and
the rest). Each entry is handed to shell.page(). Edit the copy here and re-run
tools/build_pages.py.

Provenance: the page list and the original wording were recovered from the
Internet Archive capture of the old WordPress site
(https://web.archive.org/web/20250227103507/https://allabouthr.co/) plus the
URLs Google still has indexed. Figures and founder detail are taken from the
current index.html so the two stay consistent.
"""

HOME = ("/", "Home")

# --- reusable "where to next" card sets -------------------------------------

C_COMPANY = [
    ("/our-team/", "p", "People", "Our team",
     "Two founders, forty-four years between them. One decides who to hire; the other builds the systems those decisions run on.",
     "Meet them"),
    ("/why-choose-allabouthr/", "p", "Promises", "Why choose AllAboutHR",
     "Four promises with numbers attached, and the one step most HR firms skip.",
     "Read the promises"),
    ("/service-best-expert-solution/", "t", "Services", "Everything we do",
     "Talent, training and jobs, plus the software and systems work that grew out of them.",
     "See the services"),
]

C_SERVICES = [
    ("/jobs/", "p", "Jobs", "Jobs",
     "Connecting capable people with SMEs and large employers across north India. Candidates are never charged.",
     "For candidates and employers"),
    ("/training/", "p", "Training", "Training",
     "Technical skills, communication, HR workshops and internships — delivered and then tracked.",
     "See the programmes"),
    ("/#/packages", "t", "Packages", "Six packages",
     "From ten people upwards. Each one says what it includes and when it stops being the right fit.",
     "Compare them"),
]

C_PROOF = [
    ("/about-us/", "p", "Company", "About AllAboutHR",
     "Since 2023, from Mohali. Why an HR consultancy ended up writing its own software.",
     "Read the story"),
    ("/contact-us/", "t", "Contact", "Talk to us",
     "WhatsApp, email or a thirty-minute call. Most people leave clearer about their actual problem.",
     "Get in touch"),
    ("/#/review", "p", "Reviews", "What clients say",
     "125+ five-star Google reviews from the businesses and candidates we have worked with.",
     "Read the reviews"),
]

C_CLIENTS = [
    ("/#/about", "t", "Clients", "The full client wall",
     "Fifty-plus organisations across fifteen industries, grouped by sector.",
     "See every client"),
    ("/why-choose-allabouthr/", "p", "Promises", "Why choose AllAboutHR",
     "How we work, and what we will put a number against.",
     "Read the promises"),
    ("/contact-us/", "t", "Contact", "Ask for a reference",
     "We will put you in touch with a client in your own industry.",
     "Request one"),
]

# --- pages ------------------------------------------------------------------

PAGES = []


def add(**kw):
    PAGES.append(kw)


# 1 ---------------------------------------------------------------- about-us
add(
    slug="about-us",
    active="/about-us/",
    title="About Us — AllAboutHR",
    meta=("HR consulting from Mohali, Punjab since 2023 — plus the HR software and business "
          "systems we ended up building because our own advice kept needing them."),
    eyebrow="About us",
    h1="We started in HR. Then we started building the software.",
    lede=("We have worked with Indian businesses since 2023, from Mohali in Punjab. "
          "Talent, training and jobs is where we began, and it is still the core of "
          "what we do."),
    trail=[HOME, (None, "About us")],
    content="""      <h2>What we do</h2>
      <p>We sort out your HR, build the software you are missing, and join the two up — so
      the business runs properly without you in the middle of every decision. That covers
      three kinds of work, run by one team:</p>
      <ul>
        <li><strong>Strategic HR consulting.</strong> We find out what is really wrong with
        your HR, design the fix, help you run it, then check a year later whether it worked.
        In numbers, not opinions.</li>
        <li><strong>HR technology — Alvora.</strong> Software for hiring, HR, contractors and
        training, built so every number traces back to the document it came from.</li>
        <li><strong>Operations excellence — Kinexus Systems.</strong> We build the software a
        business is missing, and add AI only where it saves real hours.</li>
      </ul>

      <h2>Why a consultancy ended up writing software</h2>
      <p>Our reports kept telling owners things they could not act on. The findings were
      right. The problem was that nothing in the business recorded the thing that needed to
      change. A neat appraisal framework designed in a workshop does not survive in a company
      that still tracks attendance on a shared spreadsheet.</p>
      <p>So we built the software ourselves. Then we built the layer underneath it, for
      businesses whose real problem was that they had no system at all. That is the whole
      story, and it is why the three parts of the company work together instead of competing
      for the same client.</p>

      <h2>Where we started</h2>
      <p>The three words on our original sign were <strong>talent, training and jobs</strong>,
      and none of them have gone anywhere:</p>
      <ul>
        <li><strong>Talent.</strong> The right people drive innovation and growth, in a
        ten-person startup as much as in a group of companies. Getting that wrong is the most
        expensive mistake a growing business makes.</li>
        <li><strong>Training.</strong> Skill development is what turns a promising hire into a
        dependable one, and a technically strong manager into one people will stay for.</li>
        <li><strong>Jobs.</strong> Jobs are pathways, not positions. We connect capable people
        with good employers — and we do not charge the candidate.</li>
      </ul>

      <h2>In numbers</h2>
      <dl class="facts">
        <div><dt>In business</dt><dd>Since 2023, from Mohali, Punjab</dd></div>
        <div><dt>Candidates placed</dt><dd>500+</dd></div>
        <div><dt>Organisations served</dt><dd>50+, across fifteen industries</dd></div>
        <div><dt>Google reviews</dt><dd>125+ at five stars</dd></div>
      </dl>

      <h2>How we talk</h2>
      <p>Plain words, and a number next to every claim. In practice that means the answer
      first and the detail after; any technical word explained the first time we use it; bad
      news at the top rather than hidden in paragraph four; and &ldquo;we don&rsquo;t
      know&rdquo; when that is the true answer.</p>
      <p>What you will not get is jargon where an ordinary word would do, a feature described
      as ready when it is still being built, big promises with no number attached, or an
      account manager sitting between you and the person doing the work.</p>

      <div class="note">
        <h4>The three brands, in one line each</h4>
        <p><strong>AllAboutHR</strong> is the parent company and the advice side.
        <strong>Alvora</strong> is our software, always introduced as an AllAboutHR platform.
        <strong>Kinexus Systems</strong> is our systems team, who build what a business is
        missing and automate the routine work inside it.</p>
      </div>""",
    cards=C_COMPANY,
    cta_h2="Start with whatever hurts most.",
    cta_p=("A call costs nothing. Most people leave it with a clearer idea of their actual "
           "problem than they came in with — whether or not they end up working with us."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20read%20your%20About%20page%20and%20would%20like%20to%20talk%20about%20my%20business.",
)

# 2 ---------------------------------------------------------------- our-team
add(
    slug="our-team",
    title="Our Team — AllAboutHR",
    meta=("Meet the founders of AllAboutHR — Mahavir Singh, 19+ years in HR, and Surbhi Goyal, "
          "25 years building HR and AI systems. You work with them directly."),
    eyebrow="Who you are dealing with",
    h1="Two founders. Forty-four years between them.",
    lede=("One has spent a career deciding who to hire. The other has spent a career building "
          "the systems those decisions run on. That is the whole company in one sentence."),
    trail=[HOME, ("/about-us/", "About us"), (None, "Our team")],
    content="""      <h2>Mahavir Singh — Co-founder &amp; CEO</h2>
      <p class="hint" style="margin-top:-6px">19+ years in HR</p>
      <p>An MBA in HR who spent fifteen years inside corporate HR teams before starting
      AllAboutHR in 2023. He has sat on the other side of the table for more hiring decisions
      than most people will in a career, which is why the advice tends to be practical rather
      than theoretical.</p>
      <dl class="facts">
        <div><dt>Interviews</dt><dd>30,000+ conducted</dd></div>
        <div><dt>Placements</dt><dd>500+ successful hires</dd></div>
        <div><dt>Career guidance</dt><dd>100+ sessions</dd></div>
        <div><dt>Before this</dt><dd>15 years in corporate HR</dd></div>
      </dl>
      <ul>
        <li>Builds HR functions from scratch, and runs them as a service where a company is
        not ready for its own team.</li>
        <li>Has worked with startups, growing SMEs and large enterprises — the advice changes
        with the size.</li>
        <li><strong>WahStory Spotlight 40 Under 40 Awardee, 2024.</strong></li>
      </ul>

      <h2>Surbhi Goyal — Co-founder &amp; CTO</h2>
      <p class="hint" style="margin-top:-6px">25 years accelerating businesses by aligning
      people, processes and systems</p>
      <p>She started out writing code for government offices in Haryana, where software either
      worked for the clerk at the counter or it did not work at all. That lesson never left:
      <strong>adoption is the deliverable, not installation.</strong> Most recently VP of
      Products, building AI systems for enterprises.</p>
      <dl class="facts">
        <div><dt>HR platforms</dt><dd>15 years at a European HR platform</dd></div>
        <div><dt>Team built</dt><dd>Grew the India team she ran from 1 to 150+</dd></div>
        <div><dt>Attrition</dt><dd>Under 2% while she ran it</dd></div>
        <div><dt>Fastest AI build</dt><dd>28 days from idea to production</dd></div>
      </dl>
      <ul>
        <li>Ran product and engineering for a Nordic HR platform for fifteen years — she has
        built the thing our clients are buying.</li>
        <li><strong>ISO 27001 lead auditor</strong>, and has owned SOC&nbsp;2 Type II and
        ISO 27001 compliance end to end.</li>
        <li>Her rule on AI: it belongs only where it earns its place, and everywhere else a
        simple system wins.</li>
      </ul>

      <div class="note plum">
        <h4>No account manager</h4>
        <p>You work with them directly. There is nobody sitting between you and the person
        doing the thinking — in the room when it is going well, and when it is not. The
        consultant who analysed your business is the one you keep talking to.</p>
      </div>

      <h2>The wider team</h2>
      <p>Behind the two of them sit recruitment consultants, HR generalists, trainers and
      engineers, sized to the work in hand rather than kept on a bench. For a specific
      engagement we will tell you exactly who is doing what, and you will meet them before
      you sign.</p>""",
    cards=C_COMPANY,
    extra_ld="""<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ProfilePage","@id":"https://allabouthr.co/our-team/",
"about":[
{"@type":"Person","name":"Mahavir Singh","jobTitle":"Co-founder & CEO",
 "worksFor":{"@id":"https://allabouthr.co/#organization"},
 "knowsAbout":["Talent acquisition","HR strategy","Training","Career development"],
 "award":"WahStory Spotlight 40 Under 40 Awardee, 2024",
 "description":"An MBA in HR with 19+ years in HR, fifteen of them inside corporate HR teams. 30,000+ interviews conducted and 500+ placements."},
{"@type":"Person","name":"Surbhi Goyal","jobTitle":"Co-founder & CTO",
 "worksFor":{"@id":"https://allabouthr.co/#organization"},
 "knowsAbout":["Product management","HR technology","AI systems","ISO 27001","SOC 2"],
 "description":"25 years aligning people, processes and systems, including 15 years building a European HR platform. ISO 27001 lead auditor."}]}
</script>""",
    cta_h2="Talk to a founder, not a sales team.",
    cta_p=("Thirty minutes on the phone, no slides. You will be speaking to one of the two "
           "people above."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20would%20like%20to%20speak%20to%20one%20of%20the%20founders.",
)

# 3 ------------------------------------------------------------- job-openings
add(
    slug="job-openings",
    title="Job Openings — AllAboutHR",
    meta=("Send your CV to AllAboutHR, Mohali and we will match you against live roles across "
          "north India. Candidates are never charged a fee."),
    eyebrow="For candidates",
    h1="Looking for a job? Send us your CV.",
    lede=("We recruit for SMEs and large employers across north India. Roles move faster than "
          "any page can keep up with, so rather than publish a list that goes stale, we match "
          "your CV against whatever is live."),
    trail=[HOME, ("/jobs/", "Jobs"), (None, "Job openings")],
    content="""      <div class="note plum">
        <h4>We never charge a candidate a fee</h4>
        <p>Not for registering, not for an interview, and not on joining. Our fee is paid by
        the employer. If anybody asks you for money in our name, tell us.</p>
      </div>

      <h2>How to apply</h2>
      <ol class="steps">
        <li><span>Send your CV on <a href="https://wa.me/917696004555?text=Hi%20AllAboutHR%20%E2%80%94%20I%20am%20looking%20for%20a%20job.%20Here%20is%20my%20CV." target="_blank" rel="noopener">WhatsApp</a>
        or by email to <a href="mailto:hello@allabouthr.co">hello@allabouthr.co</a>.</span></li>
        <li><span>Tell us three things in the message: <em>the role you want</em>, <em>your
        current location and notice period</em>, and <em>your expected salary</em>. It saves a
        round of questions.</span></li>
        <li><span>If something live fits, we call you within a few working days. If nothing
        fits today, we keep you on file and come back when it does.</span></li>
        <li><span>We brief you properly before any interview — who you are meeting, what they
        actually want, and what the package really is.</span></li>
      </ol>

      <h2>What we usually recruit for</h2>
      <p>Our mandates follow our client base, so these are the areas where we most often have
      something open:</p>
      <ul>
        <li><strong>Manufacturing and engineering</strong> — production, quality, maintenance,
        stores, plant HR</li>
        <li><strong>Accounts and finance</strong> — accountants, audit assistants, finance
        executives, roles in CA firms</li>
        <li><strong>IT and ITeS</strong> — developers, support, QA, implementation</li>
        <li><strong>Sales, retail and hospitality</strong> — field sales, counter sales, store
        and branch roles</li>
        <li><strong>Healthcare, pharma and education</strong> — administration, faculty,
        operations</li>
        <li><strong>HR itself</strong> — recruiters, HR executives and HR managers</li>
      </ul>

      <h2>Freshers</h2>
      <p>We place freshers, and we do not pretend it is the same conversation as a senior hire.
      Expect honest feedback on your CV, help with how you present yourself, and a realistic
      view of the salary a first job pays. If training would get you further than another
      hundred applications, we will say so — that is what
      <a href="/training/">our training programmes</a> and
      <a href="/recruitxcel/">RecruitXcel</a> exist for.</p>

      <h2>Hiring rather than job-hunting?</h2>
      <p>If you are an employer with a role to fill, start on the
      <a href="/jobs/">jobs page</a>. Permanent, bulk and leadership hiring all work
      differently, and the right one depends on how many people you need and how quickly.</p>""",
    cards=[
        ("/jobs/", "p", "Employers", "Hiring, not job-hunting?",
         "Permanent, bulk, leadership and campus hiring — and what each one costs.",
         "For employers"),
        ("/recruitxcel/", "p", "Training", "RecruitXcel",
         "Twenty working days on end-to-end recruitment, with a case study every alternate day.",
         "See the programme"),
        ("/contact-us/", "t", "Contact", "Talk to us",
         "WhatsApp is the fastest way to reach a person rather than a ticket.",
         "Get in touch"),
    ],
    cta_h2="Send your CV. We will be straight with you.",
    cta_p=("One message is enough to start. If we cannot help, we will tell you that too, "
           "rather than leave you waiting."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20am%20looking%20for%20a%20job.%20Here%20is%20my%20CV.",
    cta_second=("/jobs/", "Read about our hiring work"),
)

# 4 ---------------------------------------------------------------- jobs
add(
    slug="jobs",
    title="Jobs — Recruitment Services — AllAboutHR",
    meta=("Permanent, bulk, leadership and campus hiring for Indian businesses, run from "
          "Mohali since 2023. 500+ candidates placed. Background checks included."),
    eyebrow="Talent · Jobs",
    h1="Jobs are pathways, not positions.",
    lede=("At the heart of what we do is connecting capable people with good employers — "
          "dynamic SMEs and established groups alike. 500+ placements since 2023."),
    trail=[HOME, ("/service-best-expert-solution/", "Services"), (None, "Jobs")],
    content="""      <h2>For employers</h2>
      <p>A wrong hire at manager level typically costs several months of salary before anyone
      admits it was wrong. Most of that cost is avoidable, and it is avoided at the shortlist
      rather than at the interview. Four ways we hire, depending on what you need:</p>
      <ul>
        <li><strong>Search.</strong> Senior and leadership hires, found rather than advertised.</li>
        <li><strong>Flow.</strong> Bulk and permanent hiring when you need numbers, fast.</li>
        <li><strong>Campus.</strong> Hiring straight from colleges through our institution
        partnerships. <a href="/recruitxcel/">RecruitXcel</a> is the main programme.</li>
        <li><strong>Verify.</strong> Background checks, so you find out before joining rather
        than after.</li>
      </ul>

      <div class="note">
        <h4>What it costs</h4>
        <p>Standard recruitment runs at 8.33% of annual package. On our
        <a href="/#/packages">Operate package</a> and above it drops to <strong>6%</strong>,
        with cheaper background checks, because the hiring sits inside a retainer we are
        already running. We will tell you which way round is cheaper for you.</p>
      </div>

      <h2>How a mandate actually runs</h2>
      <ol class="steps">
        <li><span><em>We agree the role properly.</em> Not a copied job description — what the
        person has to deliver in the first six months, and what you will pay for it.</span></li>
        <li><span><em>We source and screen.</em> You see a shortlist with notes, not a stack of
        forwarded CVs.</span></li>
        <li><span><em>You interview.</em> We brief both sides, chase the diary and keep the
        candidate warm, which is where most mandates quietly die.</span></li>
        <li><span><em>Offer and joining.</em> We stay involved through notice period, because
        that is when candidates get counter-offered.</span></li>
      </ol>

      <h2>For candidates</h2>
      <p>We are paid by the employer, never by you. What you get is an honest read on where
      your CV stands, a proper brief before any interview, and a straight answer about the
      package rather than a number that changes at the offer stage.</p>
      <p><a href="/job-openings/">Send us your CV &rarr;</a></p>

      <h2>Where the recruitment sits in the bigger picture</h2>
      <p>Hiring is the third of the five steps in our <a href="/#/consulting">Growth
      Loop</a> — <em>Source</em>, after <em>See</em> and <em>Shape</em>. That order matters. If
      your appraisal system is guesswork and your pay bands do not exist, hiring harder will
      not fix your attrition. We will say so before we take the mandate.</p>""",
    cards=[
        ("/job-openings/", "p", "Candidates", "Send your CV",
         "What to put in the message, what happens next, and why we never charge you a fee.",
         "For candidates"),
        ("/training/", "p", "Training", "Training",
         "Sometimes the problem is not who you hired — it is that nobody developed them.",
         "See the programmes"),
        ("/#/consulting", "t", "Consulting", "The Growth Loop",
         "Five steps from “something is wrong” to “here is the proof it improved”.",
         "See how we work"),
    ],
    cta_h2="Tell us the role you cannot fill.",
    cta_p=("One message with the role, the location and the budget is enough for us to tell "
           "you whether we can help and roughly how long it will take."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20have%20a%20role%20I%20cannot%20fill.%20Can%20we%20talk%3F",
)

# 5 ---------------------------------------------------------------- training
add(
    slug="training",
    title="Training — AllAboutHR",
    meta=("Technical skills, communication, HR workshops, internships and manager development "
          "from AllAboutHR, Mohali — delivered, then measured."),
    eyebrow="Talent · Training",
    h1="Training is the keystone. Measuring it is the point.",
    lede=("Training matters whether you are nurturing fresh talent or sharpening seasoned "
          "professionals. What makes it worth the money is knowing afterwards whether anything "
          "changed."),
    trail=[HOME, ("/service-best-expert-solution/", "Services"), (None, "Training")],
    content="""      <h2>What we run</h2>
      <ul>
        <li><strong>AllAboutHR Academy.</strong> The training itself — technical skills,
        communication, HR workshops and internships, run by our own trainers.</li>
        <li><strong><a href="/recruitxcel/">RecruitXcel</a>.</strong> Twenty working days on
        end-to-end recruitment, with a case study every alternate day and a certificate at the
        end. Our flagship programme.</li>
        <li><strong>AllAboutHR Lead.</strong> Developing your managers — usually commissioned
        because a health check showed that is exactly where the problem sits.</li>
        <li><strong>Alvora Learning.</strong> Training delivered and tracked in software, using
        the same skill list your appraisals use.</li>
      </ul>

      <div class="note">
        <h4>Why the skill list matters</h4>
        <p>If training is tracked against one list of skills and appraisals are scored against
        another, you can never answer the only question worth asking: did the training move
        anyone&rsquo;s rating? Using one list for both is a small decision that makes the whole
        spend accountable.</p>
      </div>

      <h2>For individuals</h2>
      <p>If you are not a company but a person trying to get further, the practical help is
      career counselling, CV crafting, LinkedIn profile optimisation, interview preparation and
      skill development training. Whether you are chasing a first job or a better one, the work
      is the same: find the gap, close the gap, then present it properly.</p>
      <p><a href="/job-openings/">If you also want to be considered for live roles, send your
      CV &rarr;</a></p>

      <h2>For companies</h2>
      <p>We will ask what you expect to change before we design anything, because &ldquo;the
      team needs training&rdquo; is a symptom, not a diagnosis. Often the honest finding is
      that the managers need developing rather than the staff, or that nothing is written down
      so every new joiner learns a different version of the job. That is a cheaper fix than a
      training calendar.</p>

      <h2>How we price it</h2>
      <p>Programmes are quoted per cohort, against the number of people and the number of days.
      On the <a href="/#/packages">Perform package</a> and above, manager training and review
      training are already included — so if you are on a retainer with us, ask before you buy
      a programme separately.</p>""",
    cards=[
        ("/recruitxcel/", "p", "Flagship", "RecruitXcel",
         "Mastering end-to-end recruitment: processes, implementation excellence and case studies.",
         "See the programme"),
        ("/jobs/", "p", "Jobs", "Hiring",
         "Search, bulk hiring, campus hiring and background checks.",
         "See the hiring work"),
        ("/#/alvora", "t", "Software", "Alvora Learning",
         "Training delivered and tracked against the skills your appraisals already use.",
         "See the platform"),
    ],
    cta_h2="Tell us what you want to change.",
    cta_p=("Not which course you want — what should be different afterwards. We will design "
           "backwards from that, and tell you if training is the wrong tool."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20would%20like%20to%20talk%20about%20training%20for%20my%20team.",
)

# 6 --------------------------------------------------------------- recruitxcel
add(
    slug="recruitxcel",
    title="RecruitXcel — End-to-End Recruitment Training — AllAboutHR",
    meta=("RecruitXcel: end-to-end recruitment training over 20 working days, 4 hours a day, "
          "with a case study every alternate day and a certificate."),
    eyebrow="Flagship programme",
    h1="RecruitXcel — a comprehensive journey through end-to-end recruitment.",
    lede=("Mastering end-to-end recruitment: processes, implementation excellence and case "
          "studies. Twenty working days, four hours a day, with a case study every alternate "
          "day."),
    trail=[HOME, ("/training/", "Training"), (None, "RecruitXcel")],
    content="""      <dl class="facts">
        <div><dt>Duration</dt><dd>20 working days, 4 hours each day</dd></div>
        <div><dt>Case studies</dt><dd>One on every alternate day</dd></div>
        <div><dt>Certification</dt><dd>Certificate from Mahavir Singh &amp; Associates</dd></div>
        <div><dt>Led by</dt><dd>Mahavir Singh, 30,000+ interviews conducted</dd></div>
      </dl>

      <h2>Who it is for</h2>
      <ul>
        <li><strong>New recruiters and HR executives</strong> who were handed a hiring target
        and left to work it out.</li>
        <li><strong>In-house talent acquisition teams</strong> that can source but lose
        candidates between shortlist and joining.</li>
        <li><strong>Freshers and career changers</strong> aiming at recruitment as a career
        rather than a stopgap.</li>
        <li><strong>Founders and managers</strong> who do their own hiring and would rather do
        it well.</li>
      </ul>

      <h2>What it covers</h2>
      <p>The spine of the programme is one hiring cycle, followed all the way through, with the
      theory attached at the point where you would actually need it:</p>
      <ul>
        <li>Understanding a role properly — writing a job description against deliverables
        instead of copying one</li>
        <li>Workforce planning, headcount approval and where a mandate really comes from</li>
        <li>Sourcing — job boards, referrals, social platforms, databases, and campus</li>
        <li>Screening and shortlisting without wasting the hiring manager&rsquo;s time</li>
        <li>Structured interviewing, competency questions and honest rating scales</li>
        <li>Assessment, reference and background checks</li>
        <li>Offer management, negotiation and surviving the notice period</li>
        <li>Onboarding, joining documentation and statutory basics</li>
        <li>Recruitment metrics — cost per hire, time to hire, offer-drop and early attrition</li>
        <li>Recruitment technology, and what an applicant tracking system does and does not
        solve</li>
      </ul>

      <div class="note plum">
        <h4>Why the case studies are half the programme</h4>
        <p>A case study every alternate day is the part people remember. Recruitment theory is
        easy to nod along to and hard to apply under a deadline with a hiring manager who has
        changed their mind twice. Working real situations — the counter-offer, the candidate who
        goes quiet, the brief that keeps moving — is what makes the rest stick.</p>
      </div>

      <h2>What you leave with</h2>
      <ul>
        <li>A certificate from Mahavir Singh &amp; Associates.</li>
        <li>A working set of templates: job description, screening notes, interview guide,
        offer and joining checklists.</li>
        <li>The recruitment metrics that matter, and how to produce them from whatever system
        you have.</li>
        <li>Honest feedback on your own hiring, from someone who has run 30,000+ interviews.</li>
      </ul>

      <h2>Dates, batches and fees</h2>
      <p>RecruitXcel runs as a scheduled batch and as a private in-house cohort for a single
      employer. Because the dates and the fee depend on the batch and whether it is in-house,
      we quote on enquiry rather than publish a price that goes stale.
      <strong>Message us for the next start date.</strong></p>""",
    cards=[
        ("/training/", "p", "Training", "All our training",
         "Technical skills, communication, HR workshops, internships and manager development.",
         "See the programmes"),
        ("/job-openings/", "p", "Jobs", "Looking for a role?",
         "If the goal is a recruitment job rather than a certificate, start here.",
         "Send your CV"),
        ("/our-team/", "t", "People", "Who teaches it",
         "Mahavir Singh, 19+ years in HR and fifteen of them inside corporate HR teams.",
         "Meet the founders"),
    ],
    cta_h2="Ask for the next RecruitXcel batch.",
    cta_p=("Tell us whether you are joining as an individual or want a private in-house cohort, "
           "and we will send dates and the fee."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20please%20send%20me%20the%20next%20RecruitXcel%20batch%20dates%20and%20fee.",
    cta_second=("/training/", "See all training"),
)

# 7 --------------------------------------------- service-best-expert-solution
add(
    slug="service-best-expert-solution",
    title="Our Services — HR Consulting, Software and Systems — AllAboutHR",
    meta=("Everything AllAboutHR does — HR consulting, recruitment, training, the Alvora HR "
          "platforms and Kinexus business systems. One team, one bill."),
    eyebrow="Our services",
    h1="Three ways we help. One team, so nothing falls between them.",
    lede=("Most firms sell you advice and leave. Others sell you software and leave. We do the "
          "advice, build the software, and stay until your team can run it."),
    trail=[HOME, (None, "Services")],
    content="""      <h2>1 &middot; Strategic HR consulting</h2>
      <p>We find out what is really wrong with your HR, design the fix, help you run it, then
      check a year later whether it worked — in numbers, not opinions. The framework is the
      <strong><a href="/#/consulting">Growth Loop</a></strong>: five steps from
      &ldquo;something is wrong&rdquo; to &ldquo;here is the proof it improved&rdquo;.</p>
      <ul>
        <li><strong>See</strong> — a six-week health check of your HR. Fifteen areas, each
        scored, with the evidence shown.</li>
        <li><strong>Shape</strong> — clear job levels, honest rating scales, rules your managers
        can actually follow.</li>
        <li><strong>Source</strong> — <a href="/jobs/">hiring</a>: search, bulk, campus and
        background checks.</li>
        <li><strong>Strengthen</strong> — <a href="/training/">training</a>, manager
        development and staff surveys.</li>
        <li><strong>Sustain</strong> — appraisals, increments, and the re-measurement most firms
        skip.</li>
      </ul>

      <h2>2 &middot; HR technology — Alvora</h2>
      <p>Four pieces of software that work together, built so a score only moves when someone
      submits proof and a manager approves it. When an employee asks why they got a rating, you
      can show them, line by line.</p>
      <ul>
        <li><strong>Alvora HRMS</strong> — records, leave, attendance and shifts, goals,
        appraisals, increments and letters.</li>
        <li><strong>Alvora Hire</strong> — every CV in one pipeline, no duplicates, interview
        notes captured as you go.</li>
        <li><strong>Alvora Gig</strong> — contractors and vendor staff: papers, compliance,
        timesheets and payments.</li>
        <li><strong>Alvora Learning</strong> — training delivered and tracked against the same
        skills your appraisals use.</li>
      </ul>
      <p><a href="/#/alvora">See the platforms &rarr;</a></p>

      <h2>3 &middot; Operations excellence — Kinexus Systems</h2>
      <p>We build the software your business is missing, and add AI to take routine work off
      your team — only where it saves real hours. Three steps, quoted rather than
      subscribed:</p>
      <ul>
        <li><strong>Baseline</strong> — we follow one job through your business and count what
        the re-typing and chasing costs you each week. Fixed price, fixed dates, ends in a
        decision.</li>
        <li><strong>Foundation</strong> — one system where everything lives, built on open-source
        foundations you own outright.</li>
        <li><strong>Agents</strong> — AI on the repetitive jobs, priced per job automated rather
        than per user.</li>
      </ul>
      <p><a href="/#/kinexus">See what we build &rarr;</a></p>

      <h2>Talent, training and jobs</h2>
      <p>The three services we started with are still the way most clients meet us:</p>
      <div class="nextrow" style="margin:18px 0 26px">
        <a class="card hov" href="/jobs/"><span class="tag p">Talent</span><h4>Jobs</h4>
          <p>Search, bulk hiring, campus hiring and background checks. 500+ placements.</p>
          <p class="go">See the hiring work &rarr;</p></a>
        <a class="card hov" href="/training/"><span class="tag p">Training</span><h4>Training</h4>
          <p>Technical skills, communication, HR workshops, internships, manager development.</p>
          <p class="go">See the programmes &rarr;</p></a>
        <a class="card hov" href="/job-openings/"><span class="tag t">Jobs</span><h4>Job openings</h4>
          <p>For candidates. Send your CV; we never charge you a fee.</p>
          <p class="go">Send your CV &rarr;</p></a>
      </div>

      <h2>How it is priced</h2>
      <p>Consulting and HR work is sold as one of <strong>six packages</strong>, from ten people
      upwards — each one says what problem it solves, exactly what is included, and when it
      stops being the right fit. Systems work is quoted against what we actually find, so you
      never buy parts you do not need.</p>
      <p><a href="/#/packages">See the six packages &rarr;</a></p>

      <h2>More on how we think</h2>
      <div class="nextrow" style="margin:18px 0 26px">
        <a class="card hov" href="/we-help-you-to-make-business-stratgey/"><h4>Business strategy</h4>
          <p>Strategy fails on people, not on ideas. Org design, headcount plans and goals that cascade.</p>
          <p class="go">Read more &rarr;</p></a>
        <a class="card hov" href="/we-provide-best-ideas-for-the-business-growth/"><h4>Innovative HR ideas</h4>
          <p>A-to-Z HR, in the order that actually works &mdash; and where the innovation really is.</p>
          <p class="go">Read more &rarr;</p></a>
        <a class="card hov" href="/we-help-individuals-and-businesses-make-things-happen-for-their-dream/"><h4>Individuals and businesses</h4>
          <p>Career counselling and CV help on one side, full HR support on the other. Why we do both.</p>
          <p class="go">Read more &rarr;</p></a>
      </div>

      <div class="note">
        <h4>Two Engines</h4>
        <p>If both your people and your systems feel broken, we can check both in the same six
        weeks — one project, two reports, one meeting with you, and the order to fix things in,
        cheapest and fastest first.</p>
      </div>""",
    cards=C_SERVICES,
    cta_h2="Not sure which of the three you need?",
    cta_p=("That is the normal starting position. Tell us what is going wrong and we will point "
           "you at the cheapest thing that fixes it — sometimes the honest answer is that you "
           "do not need us yet."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20am%20not%20sure%20which%20service%20I%20need.%20Can%20we%20talk%3F",
)

# 8 ------------------------------------------------------ why-choose-allabouthr
add(
    slug="why-choose-allabouthr",
    title="Why Choose AllAboutHR",
    meta=("Four promises you can hold us to, the one step most HR firms skip, and why our "
          "advice comes with a number attached. AllAboutHR, Mohali, since 2023."),
    eyebrow="Why choose us",
    h1="Four promises. Hold us to them.",
    lede=("Every consultancy says it is different. These are the four things we will put in "
          "writing, plus the step most HR firms quietly leave out."),
    trail=[HOME, ("/about-us/", "About us"), (None, "Why choose AllAboutHR")],
    content="""      <h2>1 &middot; Numbers you can check</h2>
      <p>Every score we give you comes with the evidence behind it. Where your data does not
      exist, that is the finding — we will not invent a number to fill the gap. A health check
      that cannot show its working is just an opinion with a cover page.</p>

      <h2>2 &middot; You get the person who did the work</h2>
      <p>The consultant who analysed your business is the one you keep talking to. You are not
      handed to a delivery team after signing, and there is no account manager between you and
      the person doing the thinking. With two founders and a small team,
      <a href="/our-team/">that is simply how it works</a>.</p>

      <h2>3 &middot; Every promise has a number attached</h2>
      <p>We will not promise &ldquo;transformation&rdquo;. We will tell you what we expect to
      change, by how much, and when we will measure it again. If we cannot put a number against
      something, we will say that instead of dressing it up.</p>

      <h2>4 &middot; We stay until your team can run it</h2>
      <p>We do not hand over a document and disappear. We train your people, sit in the first
      cycles with them, and stay involved as it beds in. A policy in a folder gets ignored; the
      same rules inside the system your managers use every day get followed.</p>

      <div class="note plum">
        <h4>The step most firms skip</h4>
        <p>Nine to twelve months after the work, we run the same health check again and compare
        it with where you started. <strong>If the numbers did not move, we say so.</strong>
        That is the last step of our Growth Loop, and it is the one that makes the first four
        promises checkable rather than decorative.</p>
      </div>

      <h2>What makes us unusual</h2>
      <ul>
        <li><strong>We do the advice and build the software.</strong> Most firms do one or the
        other, which is why good recommendations so often go nowhere — nothing in the business
        can carry them out.</li>
        <li><strong>We will talk you out of AI.</strong> If a simple rule or a better-designed
        form does the same job for less money, we will build that instead, even though the AI
        version would earn us more.</li>
        <li><strong>We show you before you pay.</strong> On systems work we build a small
        working version using your own data, so you judge the real thing rather than a slide
        about it.</li>
        <li><strong>Both engines, together.</strong> Nobody else in the Indian mid-market
        checks your people and your systems in the same six weeks.</li>
      </ul>

      <h2>The track record</h2>
      <dl class="facts">
        <div><dt>In business</dt><dd>Since 2023, from Mohali, Punjab</dd></div>
        <div><dt>Organisations served</dt><dd>50+, across fifteen industries</dd></div>
        <div><dt>Candidates placed</dt><dd>500+</dd></div>
        <div><dt>Google reviews</dt><dd>125+ at five stars</dd></div>
        <div><dt>Founders&rsquo; experience</dt><dd>44 years between the two of them</dd></div>
      </dl>
      <p>Ask us for references in your own industry — we will put you in touch with a client
      rather than send you a case study we wrote ourselves.</p>""",
    cards=C_PROOF,
    cta_h2="Hold us to the four promises.",
    cta_p=("Start with a call. If we cannot tell you what we would expect to change and by how "
           "much, you should not hire us."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20read%20your%20four%20promises%20and%20would%20like%20to%20talk.",
)

# 9 -------------------------------------------------------------- contact-us
add(
    slug="contact-us",
    title="Contact Us — AllAboutHR, Mohali",
    meta=("Talk to AllAboutHR: WhatsApp +91 76960 04555, email hello@allabouthr.co. Based in "
          "Mohali, Punjab, working with clients across India. We usually reply the same day."),
    eyebrow="Contact",
    h1="Tell us what is going wrong.",
    lede=("The fastest way to reach us is WhatsApp — one tap and you are talking to a person, "
          "not a ticket. We usually reply the same day."),
    trail=[HOME, (None, "Contact us")],
    content="""      <dl class="facts">
        <div><dt>WhatsApp</dt><dd><a href="https://wa.me/917696004555?text=Hi%20AllAboutHR%20%E2%80%94%20I%20would%20like%20to%20talk%20about%20my%20business." target="_blank" rel="noopener">+91 76960 04555</a> &mdash; fastest</dd></div>
        <div><dt>Phone</dt><dd><a href="tel:+917696004555">+91 76960 04555</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:hello@allabouthr.co">hello@allabouthr.co</a></dd></div>
        <div><dt>Based in</dt><dd>Mohali, Punjab, India</dd></div>
        <div><dt>Working with</dt><dd>Clients across India, from ten people to 2,500</dd></div>
      </dl>

      <p>From Mohali we work with clients across the country. If you would rather write it out
      than talk, there is a <a href="/#/contact">short enquiry form on the main site</a> — it
      asks for your headcount and which of our three streams sounds closest, which saves a
      round of questions.</p>

      <h2>What happens next</h2>
      <ol class="steps">
        <li><span>We reply with <em>two or three questions</em>, not a brochure.</span></li>
        <li><span>A <em>thirty-minute call</em> to check the problem is what it looks like.</span></li>
        <li><span>A <em>costed proposal</em> — or an honest &ldquo;not yet&rdquo;.</span></li>
      </ol>

      <div class="note">
        <h4>A call costs nothing</h4>
        <p>Most people leave a first call with a clearer idea of their actual problem than they
        came in with, whether or not they end up working with us. Sometimes the honest answer is
        that you do not need us yet, and we will say so.</p>
      </div>

      <h2>Reaching the right part of the house</h2>
      <ul>
        <li><strong>People problems</strong> — staff leaving, appraisals that mean nothing,
        compliance you cannot prove: start at <a href="/#/consulting">Consulting</a> or the
        <a href="/#/packages">packages</a>.</li>
        <li><strong>HR or hiring software</strong>: <a href="/#/alvora">Alvora</a>.</li>
        <li><strong>You cannot see what is happening in the business</strong>:
        <a href="/#/kinexus">Kinexus Systems</a>, who can also be reached on their own site at
        <a href="https://www.kinexus.co.in" target="_blank" rel="noopener">kinexus.co.in</a>.</li>
        <li><strong>Looking for a job</strong>: <a href="/job-openings/">send us your CV</a> —
        candidates are never charged.</li>
        <li><strong>Training or RecruitXcel dates</strong>: <a href="/recruitxcel/">RecruitXcel</a>.</li>
      </ul>

      <h2>Already worked with us?</h2>
      <p><a href="/#/review">Leave us a Google review</a> — it takes about two minutes and helps
      the next business choose well. If a project did not go the way you hoped, tell us first
      and one of the founders will reply.</p>""",
    cards=C_PROOF,
    extra_ld="""<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ContactPage","@id":"https://allabouthr.co/contact-us/",
"mainEntity":{"@id":"https://allabouthr.co/#organization"},
"about":{"@type":"ProfessionalService","name":"AllAboutHR",
 "telephone":"+91-76960-04555","email":"hello@allabouthr.co",
 "url":"https://allabouthr.co",
 "address":{"@type":"PostalAddress","addressLocality":"Mohali","addressRegion":"Punjab","addressCountry":"IN"},
 "areaServed":{"@type":"Country","name":"India"},
 "availableLanguage":["en","hi","pa"]}}
</script>""",
    cta_h2="One message is enough to start.",
    cta_p=("Tell us what is going wrong in a sentence or two. You will get questions back, not "
           "a sales deck."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20would%20like%20to%20talk%20about%20my%20business.",
    cta_second=("/#/contact", "Use the form instead"),
)
