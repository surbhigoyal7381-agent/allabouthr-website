# -*- coding: utf-8 -*-
"""The four commercial pages at real, indexable URLs.

/consulting/  /alvora/  /kinexus/  /packages/

These existed only as hash routes (`/#/packages`), which Google does not treat
as separate pages — so the four things the business actually sells had no URL
anyone could land on, link to or rank.

They are not copies of the single-page site. The facts are the same, because
index.html is the source of truth for them, but each page is written to stand
on its own and goes deeper than the panel it corresponds to. The hash routes
stay as the interactive version; these are the front doors. There is no
duplicate-content risk, because the hash routes were never separate URLs.
"""

from content import HOME, add

# ---------------------------------------------------------------- consulting

add(
    slug="consulting",
    active="/consulting/",
    title="HR Consulting — The Growth Loop — AllAboutHR",
    meta=("Strategic HR consulting for Indian businesses. Five steps from “something is "
          "wrong” to “here is the proof it improved” — and we re-measure a year later."),
    eyebrow="AllAboutHR · Strategic HR consulting",
    h1="Fix the people problem. Then prove it stayed fixed.",
    lede=("We call it the Growth Loop. Five steps that take you from “something is "
          "wrong” to “here is the proof it improved”. Most HR firms hand you "
          "a report and leave. The last step of ours is checking the numbers a year later."),
    trail=[HOME, ("/service-best-expert-solution/", "Services"), (None, "HR consulting")],
    content="""      <h2>Why most HR consulting fails</h2>
      <p>Not because the advice is wrong. Because nothing in the business is built to carry it
      out. A neat appraisal framework designed in a workshop does not survive in a company that
      still tracks attendance on a shared spreadsheet, and a policy in a folder gets ignored
      while the same rule inside the system managers use every day gets followed.</p>
      <p>That is why the loop has five steps rather than one, and why the fifth one exists.</p>

      <h2>1 &middot; See — know what&rsquo;s true</h2>
      <p>This is the step that tells you where the money is leaking. Most owners are surprised
      by the answer.</p>
      <ul>
        <li><strong>AllAboutHR Lens.</strong> A six-week health check of your HR. Fifteen
        areas, each given a score, with the evidence shown. You see exactly which one is
        hurting you most.</li>
        <li><strong>AllAboutHR Signals.</strong> The numbers behind the people problems — who
        leaves and when, what each exit costs you, and whether anyone is being paid
        unfairly.</li>
        <li><strong>AllAboutHR Assure.</strong> A check of your legal paperwork and your POSH
        set-up, so nothing is missing if an inspector asks.</li>
        <li><strong>Kinexus Baseline.</strong> The same idea, for your systems. Where your
        information actually sits, how many places it has to be re-typed, and how many hours a
        week that wastes. <a href="/kinexus/">More on Kinexus &rarr;</a></li>
      </ul>

      <h2>2 &middot; Shape — design the system</h2>
      <p>Turning the findings into rules your managers can actually follow.</p>
      <ul>
        <li><strong>AllAboutHR Blueprint.</strong> Setting up the HR function properly — who
        does what, how many people you need, and the targets each department is measured
        on.</li>
        <li><strong>AllAboutHR Calibrate.</strong> Clear job levels, honest rating scales and
        the skills each role needs. This is what stops two managers scoring the same person
        differently.</li>
      </ul>

      <h2>3 &middot; Source — bring the right people in</h2>
      <p>Fewer wrong hires. A wrong hire at manager level typically costs several months of
      salary before anyone admits it was wrong.</p>
      <ul>
        <li><strong>AllAboutHR Search</strong> — senior and leadership hires.</li>
        <li><strong>AllAboutHR Flow</strong> — bulk and permanent hiring when you need numbers,
        fast.</li>
        <li><strong>AllAboutHR Campus</strong> — hiring straight from colleges through our
        institution partnerships. <a href="/recruitxcel/">RecruitXcel</a> is the main
        programme.</li>
        <li><strong>AllAboutHR Verify</strong> — background checks, so you find out before
        joining rather than after.</li>
        <li><strong>Alvora Hire</strong> — the platform underneath it all.
        <a href="/alvora/">See the software &rarr;</a></li>
      </ul>
      <p><a href="/jobs/">How a recruitment mandate actually runs &rarr;</a></p>

      <h2>4 &middot; Strengthen — enable and engage them</h2>
      <p>Keeping the people you already paid to hire and train.</p>
      <ul>
        <li><strong>AllAboutHR Academy</strong> — technical skills, communication, HR workshops
        and internships. <a href="/training/">See the programmes &rarr;</a></li>
        <li><strong>AllAboutHR Lead</strong> — developing your managers, usually because the
        health check showed that is where the problem sits.</li>
        <li><strong>AllAboutHR Pulse</strong> — short, regular staff surveys, and more
        importantly tracking whether anything was done about the answers.</li>
        <li><strong>Alvora HRMS and Alvora Learning</strong> — the systems that make it
        routine.</li>
      </ul>

      <h2>5 &middot; Sustain — perform, reward, prove</h2>
      <p>The step most firms skip, because it is where you find out whether the money was well
      spent.</p>
      <ul>
        <li><strong>AllAboutHR Perform</strong> — rolling out appraisals properly: goals set,
        evidence collected, ratings moderated across managers.</li>
        <li><strong>AllAboutHR Reward</strong> — running the increment cycle: salary bands, a
        clear increment matrix, and fixing any unfair pay gaps.</li>
        <li><strong>AllAboutHR Retain</strong> — finding out why people leave while they are
        still here, and which managers lose the most staff.</li>
        <li><strong>AllAboutHR Proof</strong> — we run the same health check nine to twelve
        months later and compare. <strong>If the numbers did not move, we tell you.</strong></li>
      </ul>

      <div class="note plum">
        <h4>Two things sit alongside all five</h4>
        <p><strong>Managed</strong> means we run the HR work for you instead of just advising —
        part-time or fully outsourced. <strong>Build</strong> is
        <a href="/kinexus/">Kinexus</a>: when a step needs software you do not have, we build
        it rather than leaving you stuck.</p>
      </div>

      <h2>Why this compounds, and a one-off project does not</h2>
      <ol>
        <li><strong>We find the real problem.</strong> Six weeks, fifteen areas, each scored
        with the evidence. Most owners are surprised by which one is worst.</li>
        <li><strong>We design the fix.</strong> Clear job levels, honest rating scales, rules
        managers can follow — written for your business, not copied from a template.</li>
        <li><strong>The software makes it stick.</strong> A policy in a folder gets ignored. The
        same rules inside the system your managers use every day get followed.</li>
        <li><strong>We check it worked.</strong> Nine to twelve months later we run the same
        check-up again and compare.</li>
      </ol>

      <h2>Four promises you can hold us to</h2>
      <ul>
        <li><strong>Numbers you can check.</strong> Every score comes with the evidence behind
        it. Where your data does not exist, that is the finding — we will not invent a number
        to fill the gap.</li>
        <li><strong>You get the person who did the work.</strong> The consultant who analysed
        your business is the one you keep talking to.</li>
        <li><strong>Every promise has a number attached.</strong> We will not promise
        &ldquo;transformation&rdquo;. We will tell you what we expect to change, by how much,
        and when we will measure it again.</li>
        <li><strong>We stay until your team can run it.</strong> We train your people and sit
        in the first cycles with them.</li>
      </ul>
      <p><a href="/why-choose-allabouthr/">More on how we work &rarr;</a></p>

      <h2>What it costs</h2>
      <p>Consulting is sold as one of <a href="/packages/">six packages</a>, from ten people
      upwards. Each says what problem it solves, exactly what is included, and when it stops
      being the right fit — so you know in advance when it is time to move up.</p>""",
    extra_ld="""<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Service","name":"Strategic HR Consulting",
"serviceType":"HR consulting",
"provider":{"@id":"https://allabouthr.co/#organization"},
"areaServed":{"@type":"Country","name":"India"},
"url":"https://allabouthr.co/consulting/",
"description":"The Growth Loop — five steps from diagnosis to re-measurement: See, Shape, Source, Strengthen, Sustain.",
"hasOfferCatalog":{"@type":"OfferCatalog","name":"The Growth Loop","itemListElement":[
{"@type":"Offer","itemOffered":{"@type":"Service","name":"See — HR health check, fifteen areas scored"}},
{"@type":"Offer","itemOffered":{"@type":"Service","name":"Shape — job levels, rating scales, HR operating model"}},
{"@type":"Offer","itemOffered":{"@type":"Service","name":"Source — search, bulk, campus hiring and background checks"}},
{"@type":"Offer","itemOffered":{"@type":"Service","name":"Strengthen — training, manager development, staff surveys"}},
{"@type":"Offer","itemOffered":{"@type":"Service","name":"Sustain — appraisals, increments and re-measurement"}}]}}
</script>""",
    cards=[
        ("/packages/", "p", "Pricing", "Six packages",
         "From ten people upwards. What each includes, and when it stops being the right fit.",
         "Compare them"),
        ("/alvora/", "p", "Software", "Alvora",
         "The HR platforms that make the advice stick once we have gone.",
         "See the software"),
        ("/why-choose-allabouthr/", "t", "Promises", "Why choose AllAboutHR",
         "Four promises with numbers attached, and the step most HR firms skip.",
         "Read the promises"),
    ],
    cta_h2="Start with a health check.",
    cta_p=("Six weeks, fifteen areas, each scored with the evidence shown. Most owners are "
           "surprised by which one is worst — and that is the point."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20would%20like%20to%20talk%20about%20HR%20consulting%20and%20a%20health%20check.",
    cta_second=("/packages/", "See the packages"),
)

# -------------------------------------------------------------------- alvora

add(
    slug="alvora",
    active="/alvora/",
    title="Alvora — HR, Hiring and Training Software — AllAboutHR",
    meta=("Alvora: HRMS, recruitment, contractor and training software where every number "
          "traces back to the document it came from. An AllAboutHR platform."),
    eyebrow="Alvora — an AllAboutHR platform",
    h1="No more numbers you can’t explain.",
    lede=("Four pieces of software that work together. A score only moves when someone submits "
          "proof and a manager approves it — so when an employee asks “why did I get "
          "this rating?”, you can show them, line by line."),
    trail=[HOME, ("/service-best-expert-solution/", "Services"), (None, "Alvora")],
    content="""      <p>That single habit removes most appraisal arguments before they start. It is also the
      thing most HR software does not do: it will happily store a rating, but it cannot tell
      you where the rating came from.</p>

      <h2>The four platforms</h2>
      <ul>
        <li><strong>Alvora HRMS</strong> <span class="tag t">Built</span> — employee records,
        leave, attendance and shifts, goals, appraisals, increments and letters, in one place.
        Your HR team stops chasing spreadsheets and your managers stop asking them to.</li>
        <li><strong>Alvora Hire</strong> <span class="tag t">Built</span> — every CV in one
        pipeline, no duplicates, no candidate lost in someone&rsquo;s inbox. Interview notes
        are captured as you go, so shortlists are based on what was actually said.</li>
        <li><strong>Alvora Gig</strong> <span class="tag s">In build</span> — for contractors
        and vendor staff: joining papers, compliance documents, timesheets and payments. Useful
        when a big part of your workforce is not on your payroll.</li>
        <li><strong>Alvora Learning</strong> <span class="tag s">In build</span> — training
        delivered and tracked, using the same skill list your appraisals use. So you can see
        whether training actually changed anyone&rsquo;s rating.</li>
      </ul>
      <p class="hint">We mark what is built and what is still being built. You should never
      find out during a demo that a feature does not exist yet.</p>

      <h2>From goal to pay rise, without a gap</h2>
      <p>Most HR software stops at the rating and leaves the pay decision to a spreadsheet.
      That gap is exactly where staff stop trusting the process.</p>
      <div class="tw">
        <table>
          <thead><tr><th>Step</th><th>What happens</th><th>What you can show later</th></tr></thead>
          <tbody>
            <tr><td><strong>Goal</strong></td><td>Set from the company target, agreed with the employee, then locked</td><td>Who changed the target, when, and why</td></tr>
            <tr><td><strong>Proof</strong></td><td>The employee submits evidence as they go; duplicates are caught</td><td>The documents behind the number</td></tr>
            <tr><td><strong>Rating</strong></td><td>Worked out from the result using rules you set, not a manager&rsquo;s mood</td><td>A plain-English explanation the employee can read themselves</td></tr>
            <tr><td><strong>Review meeting</strong></td><td>Managers compare ratings side by side and adjust the odd ones out</td><td>Every change, with the reason given</td></tr>
            <tr><td><strong>Increment</strong></td><td>Budget checked, rules applied, approvals collected</td><td>A letter and a payroll entry that match the decision exactly</td></tr>
          </tbody>
        </table>
      </div>

      <h2>Where AI sits, and where it does not</h2>
      <p><strong>AI helps. A person decides.</strong></p>
      <h3>What it does</h3>
      <ul>
        <li>Writes a first draft of a job advert you then edit</li>
        <li>Points out a vague goal before a manager approves it</li>
        <li>Answers &ldquo;how much leave do I have left?&rdquo; from your own policy, with the
        source</li>
        <li>Explains a number in plain words — the maths is done by code, not by AI</li>
      </ul>
      <h3>What it never does</h3>
      <ul>
        <li>Decide anyone&rsquo;s rating. The number that affects pay is chosen by a named
        person</li>
        <li>Read faces, voices or moods. We have not built it and cannot add it later</li>
        <li>Watch how people work and use it against them</li>
        <li>Calculate leave balances or pay. That stays ordinary, checkable code</li>
      </ul>
      <div class="note">
        <p>Every AI feature can be switched off, and everything still works without it. You are
        never stuck if the AI is wrong or unavailable.</p>
      </div>

      <h2>How you get it</h2>
      <p>Alvora is not sold as a separate licence. It comes inside the
      <a href="/packages/">packages</a> — HRMS Essentials from the smallest one upwards, HRMS
      Core on Operate, and Alvora Hire on Partner. That is deliberate: software on its own
      rarely fixes an HR problem, and we would rather configure it around what a
      <a href="/consulting/">health check</a> actually found.</p>""",
    extra_ld="""<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ItemList","name":"Alvora platforms",
"itemListElement":[
{"@type":"ListItem","position":1,"item":{"@type":"SoftwareApplication","name":"Alvora HRMS","applicationCategory":"BusinessApplication","operatingSystem":"Web","description":"Employee records, leave, attendance and shifts, goals, appraisals, increments and letters.","publisher":{"@id":"https://allabouthr.co/#organization"}}},
{"@type":"ListItem","position":2,"item":{"@type":"SoftwareApplication","name":"Alvora Hire","applicationCategory":"BusinessApplication","operatingSystem":"Web","description":"Recruitment pipeline with de-duplication and interview notes captured as you go.","publisher":{"@id":"https://allabouthr.co/#organization"}}},
{"@type":"ListItem","position":3,"item":{"@type":"SoftwareApplication","name":"Alvora Gig","applicationCategory":"BusinessApplication","operatingSystem":"Web","description":"Contractor and vendor staff: joining papers, compliance, timesheets and payments.","publisher":{"@id":"https://allabouthr.co/#organization"}}},
{"@type":"ListItem","position":4,"item":{"@type":"SoftwareApplication","name":"Alvora Learning","applicationCategory":"BusinessApplication","operatingSystem":"Web","description":"Training delivered and tracked against the same skills appraisals use.","publisher":{"@id":"https://allabouthr.co/#organization"}}}]}
</script>""",
    cards=[
        ("/packages/", "p", "Pricing", "Six packages",
         "Which package each Alvora platform comes with.",
         "Compare them"),
        ("/consulting/", "p", "Consulting", "The Growth Loop",
         "The advice the software is there to make stick.",
         "See how we work"),
        ("/kinexus/", "t", "Systems", "Kinexus Systems",
         "If the gap is not HR software but the system your business never had.",
         "See what we build"),
    ],
    cta_h2="See it running on your own data.",
    cta_p=("A demo on sample data proves nothing. Ask us to show you the evidence chain using "
           "a real appraisal cycle from your business."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20I%20would%20like%20to%20see%20Alvora.",
    cta_second=("/packages/", "See the packages"),
)

# ------------------------------------------------------------------- kinexus

add(
    slug="kinexus",
    active="/kinexus/",
    title="Kinexus Systems — Business Software and AI Automation — AllAboutHR",
    meta=("Kinexus Systems builds the software your business is missing and automates the "
          "routine work inside it — for Indian manufacturing, logistics, retail and services."),
    eyebrow="Kinexus Systems — an AllAboutHR company",
    h1="Most owners aren’t short of effort. They’re short of systems.",
    lede=("We build the software your business is missing, and add AI to the software you "
          "already use. You can see where things stand without asking anyone, and your team "
          "stops re-typing the same information into three places."),
    trail=[HOME, ("/service-best-expert-solution/", "Services"), (None, "Kinexus Systems")],
    content="""      <p>We work with manufacturing, logistics, retail, healthcare, professional services and
      recruitment firms. Three steps, and you can stop after any of them.</p>

      <h2>Step 1 &middot; Baseline — find out</h2>
      <blockquote><p>I don&rsquo;t know where anything stands until I ask three people.</p></blockquote>
      <p>You are running the business on memory, messages and spreadsheets. It works — until
      something slips, and by the time you hear about it the cheap fix has gone.</p>
      <p><strong>What we do.</strong> We follow one job all the way through your business, from
      enquiry to payment, and write down where the information actually sits at every step —
      which sheet, which chat group, whose head. Then we count what the re-typing and the
      chasing costs you each week.</p>
      <ul class="ochecks">
        <li>A clear picture of where your information really lives</li>
        <li>The hours per week you are losing, in a number you can act on</li>
        <li>A short list of what to fix first, cheapest and fastest at the top</li>
        <li>A small working version built on your own data — before you spend anything</li>
      </ul>
      <p class="hint"><strong>Fixed price. Fixed dates. Ends in a decision</strong> — and
      sometimes that decision is &ldquo;you don&rsquo;t need us yet&rdquo;.</p>

      <h2>Step 2 &middot; Foundation — build</h2>
      <blockquote><p>Every department has its own spreadsheet, and none of them agree.</p></blockquote>
      <p>Nobody can tell you today&rsquo;s real position without a phone call. Month-end is a
      reconstruction exercise, and your costs are a guess until it is far too late to change
      them.</p>
      <p><strong>What we do.</strong> We build the system your business is missing and put
      everything in one place — orders, jobs, stock, staff, costs. It is built on proven
      open-source foundations, <strong>so you own it outright</strong> and are never locked
      into us or into a licence that climbs every year.</p>
      <ul class="ochecks">
        <li>One screen that shows where every job actually stands, live</li>
        <li>Paperwork that fills itself in instead of being re-typed</li>
        <li>Real cost and margin per job, not an estimate at month-end</li>
        <li>Your team trained to run it, with the handover notes included</li>
      </ul>

      <h2>Step 3 &middot; Agents — automate</h2>
      <blockquote><p>My team spends a day a week moving information from one place to another.</p></blockquote>
      <p>The systems work. The people are the glue between them — copying figures, chasing
      missing documents, sending the same reminder for the fourth time.</p>
      <p><strong>What we do.</strong> We put AI to work on the repetitive jobs inside the
      systems you already have — matching documents, chasing what is missing, preparing routine
      paperwork. Anything unusual stops and goes to a named person, with a note explaining
      why.</p>
      <p class="hint"><strong>Priced per job automated, not per user.</strong> You pay for
      hours saved, so the sum either works or we do not build it.</p>

      <h2>Three things we say out loud</h2>
      <ul>
        <li><strong>AI is not the answer to everything.</strong> We only use it where we can
        show you the hours it saves. If a simple rule or a better-designed form would do the
        same job for less money, we will build that instead — even though the AI version would
        earn us more.</li>
        <li><strong>We show you before you pay.</strong> Before you commit to anything, we build
        a small working version using your own data. You judge the real thing, not a slide
        about it.</li>
        <li><strong>We are there at every step.</strong> From the first walk-through to the day
        it goes live and long after — the same people throughout, not a sales team, then a
        delivery team, then a support queue.</li>
      </ul>

      <h2>What we promise about the AI we build</h2>
      <div class="tw">
        <table>
          <thead><tr><th>The promise</th><th>How we make sure of it</th></tr></thead>
          <tbody>
            <tr><td>It cannot do anything you can&rsquo;t undo</td><td>We simply do not give it the ability. It is not a rule we ask it to follow</td></tr>
            <tr><td>It can&rsquo;t be tricked by text it reads</td><td>Words hidden in a supplier email or a CV are treated as text, never as commands</td></tr>
            <tr><td>Personal data never reaches the AI</td><td>Aadhaar, PAN and bank details are stripped out first, and we test that it works</td></tr>
            <tr><td>You can see what it did</td><td>Every action is recorded, along with the person who approved it</td></tr>
            <tr><td>You can turn it off</td><td>Every job has a normal, non-AI way of getting done as well</td></tr>
          </tbody>
        </table>
      </div>

      <h2>How it is priced</h2>
      <p>Systems work is <strong>quoted, not subscribed</strong>. Baseline is a fixed price for
      a fixed piece of work. Foundation is quoted as a project, with a monthly support figure.
      Agents are priced per job automated. We quote against what we actually find, so you never
      buy a package with parts you do not need.</p>

      <p>Kinexus Systems keeps its own site, with the engineering work set out in more detail.
      <a class="exl" href="https://www.kinexus.co.in" target="_blank" rel="noopener">Visit
      kinexus.co.in</a></p>""",
    extra_ld="""<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Service","name":"Kinexus Systems — business software and AI automation",
"serviceType":"Custom business software and process automation",
"provider":{"@id":"https://allabouthr.co/#organization"},
"areaServed":{"@type":"Country","name":"India"},
"url":"https://allabouthr.co/kinexus/",
"audience":{"@type":"BusinessAudience","name":"Manufacturing, logistics, retail, healthcare and professional services"},
"hasOfferCatalog":{"@type":"OfferCatalog","name":"Kinexus Systems","itemListElement":[
{"@type":"Offer","itemOffered":{"@type":"Service","name":"Baseline","description":"Follow one job through the business, map where information sits, count the hours lost. Fixed price, fixed dates."}},
{"@type":"Offer","itemOffered":{"@type":"Service","name":"Foundation","description":"Build the missing system on open-source foundations the client owns outright."}},
{"@type":"Offer","itemOffered":{"@type":"Service","name":"Agents","description":"AI on the repetitive work inside existing systems, priced per job automated."}}]}}
</script>""",
    cards=[
        ("/consulting/", "p", "Consulting", "The Growth Loop",
         "If the problem is your people rather than your systems — or, usually, both.",
         "See how we work"),
        ("/alvora/", "p", "Software", "Alvora",
         "HR, hiring, contractor and training software, already built.",
         "See the platforms"),
        ("/packages/", "t", "Pricing", "Packages",
         "HR work is packaged; systems work is quoted. Here is how both are priced.",
         "See the packages"),
    ],
    cta_h2="Start with a Baseline.",
    cta_p=("Fixed price, fixed dates, and it ends in a decision. We will tell you the hours you "
           "are losing each week — and whether it is worth fixing yet."),
    wa="Hi%20Kinexus%20%E2%80%94%20I%20cannot%20see%20what%20is%20happening%20in%20my%20business.%20Can%20we%20talk%20about%20a%20Baseline%3F",
    cta_second=("/consulting/", "See the consulting work"),
)

# ------------------------------------------------------------------ packages

PACKS = [
    ("Essentials", "Up to 10 employees",
     "I don&rsquo;t really know what I&rsquo;m supposed to be filing — and I&rsquo;m hoping nobody checks.",
     "We take the legal paperwork off your desk. Filings happen on time, the policies exist, "
     "and you stop worrying about it.",
     ["Compliance calendar with reminders, so nothing is missed",
      "POSH policy and committee set up properly",
      "Registration help — EPF, ESIC, Shops &amp; Establishment, PT",
      "Contract, appointment and relieving letter templates",
      "Core policies — leave, conduct, attendance, hours",
      "Alvora HRMS Essentials — records, leave, documents, self-service"],
     "Deliberately capped at 10 people, which is why it is this cheap. At 11 you move to Comply."),
    ("Comply", "11 – 500 employees",
     "If a labour inspector walked in tomorrow, I couldn&rsquo;t prove a thing.",
     "Every legal requirement met, with the record to prove it — and one named person "
     "answerable if anyone asks.",
     ["Policies written for your business, not copied from a template",
      "Labour law guidance — EPF, ESIC, Gratuity, Bonus, Maternity",
      "POSH end to end, including the annual return",
      "A record you can hand straight to an inspector",
      "Full letter set, plus written joining and exit processes",
      "Payroll support and statutory filings"],
     "Move up when the paperwork is sorted but everything still runs through you."),
    ("Operate", "11 – 500 employees",
     "Nothing moves without me. I can&rsquo;t take a week off.",
     "HR runs on a system instead of on you. Leave, attendance, payroll and hiring happen "
     "without anyone needing your sign-off.",
     ["Everything in Comply",
      "Alvora HRMS Core — leave, attendance, shifts, payroll, documents",
      "Staff do their own leave and claims, on their phone",
      "Clear job levels, grades and who reports to whom",
      "A headcount plan and department targets",
      "Hiring at 6% instead of 8.33%, and cheaper background checks",
      "<strong>Included free —</strong> a check of whether your other systems are ready"],
     "Move up when the system works but you still can&rsquo;t tell who is doing well."),
    ("Perform", "21 – 500 employees",
     "My best people are leaving, and I only find out why in the exit interview.",
     "You can see who is doing well and show why. Appraisals stop being an argument and start "
     "being a record.",
     ["Everything in Operate",
      "Goals and appraisals in the system, linked to evidence",
      "A skills framework with honest rating levels",
      "We run the review cycle and the moderation meetings for you",
      "Staff surveys and eNPS, with the actions tracked",
      "Why people are leaving — analysed, not guessed",
      "Training your managers to run a review that stands up to challenge"],
     "Move up when you can see performance but pay still doesn&rsquo;t follow it."),
    ("Partner", "41 – 500 employees",
     "Increment season is a fight, and I can&rsquo;t explain how the numbers were decided.",
     "Pay and promotion decisions you can defend to anyone who asks — and proof, in numbers, "
     "that things actually improved.",
     ["Everything in Perform",
      "Increment cycles run in the system — budgets, rules, letters, payroll",
      "Alvora Hire — the recruitment platform",
      "Salary bands, so you know who is paid oddly and why",
      "A clear increment matrix instead of a negotiation",
      "Pay gap analysis, with a plan to fix what it finds",
      "Yearly re-measurement against your starting numbers"],
     "When you build your own HR team, you move to Counsel rather than leaving."),
    ("Counsel", "251+ employees",
     "I have an HR team, but nothing they send me helps me make a decision.",
     "Your own HR team, made sharper. We advise, benchmark and measure. We do not run it for "
     "you.",
     ["A senior advisor on retainer for strategy and escalations",
      "Alvora HRMS at full scale, with your team trained to admin it",
      "A yearly check-up of the whole organisation, and a yearly re-measure",
      "Org design and operating model advice",
      "Executive search at preferential rates",
      "Compared against your own past numbers, not borrowed industry averages"],
     "The top of the ladder. From here we go deeper rather than bigger."),
]


def packs_html():
    out = []
    for name, rng, pain, outcome, bullets, move in PACKS:
        li = "".join("<li>%s</li>" % b for b in bullets)
        out.append("""      <h2>%s</h2>
      <p class="hint" style="margin-top:-8px">%s</p>
      <blockquote><p>%s</p></blockquote>
      <p>%s</p>
      <ul>%s</ul>
      <div class="note"><p><strong>When to move on:</strong> %s</p></div>"""
                   % (name, rng, pain, outcome, li, move))
    return "\n\n".join(out)


def packs_ld():
    items = []
    for i, (name, rng, pain, outcome, bullets, move) in enumerate(PACKS, 1):
        items.append(
            '{"@type":"Offer","position":%d,"name":%s,'
            '"itemOffered":{"@type":"Service","name":%s,"description":%s,'
            '"provider":{"@id":"https://allabouthr.co/#organization"}},'
            '"eligibleCustomerType":"Business","areaServed":{"@type":"Country","name":"India"}}'
            % (i, '"%s"' % name, '"AllAboutHR %s"' % name,
               '"%s — %s"' % (rng, outcome.replace('"', "'"))))
    return ",".join(items)


add(
    slug="packages",
    active="/packages/",
    title="HR Packages and Pricing — AllAboutHR",
    meta=("Six HR packages for Indian businesses from 10 to 2,500 people. Each says what it "
          "includes and when it stops being the right fit. Quoted on headcount."),
    eyebrow="Packages",
    h1="Six packages. You always know exactly what you get.",
    lede=("From ten people upwards. Each package says what problem it solves, exactly what is "
          "included, and when it stops being the right fit — so you never pay for more than "
          "you need, and you know in advance when it is time to move up."),
    trail=[HOME, ("/service-best-expert-solution/", "Services"), (None, "Packages")],
    content="""      <p>Below each one is the sentence that tells you when to stop paying for it. No other
      HR firm will write that down, which is exactly why it is worth writing down.</p>

%s

      <h2>What they cost</h2>
      <p>Pricing depends on your headcount, and every quote comes with a table showing exactly
      what you get at that size — how many visits, how many review cycles, how fast we answer.
      <strong>We show it to you before you sign, not after.</strong>
      <a href="/contact-us/">Message us and we will price it for your headcount.</a></p>

      <h2>Systems work is quoted, not subscribed</h2>
      <p><a href="/kinexus/">Kinexus Systems</a> is priced differently, because it is a
      different kind of work. Baseline is a fixed price for a fixed piece of work. Foundation
      is quoted as a project, with a monthly support figure. Agents are priced per job
      automated. We quote against what we actually find, so you never buy a package with parts
      you do not need.</p>

      <div class="note plum">
        <h4>Two Engines</h4>
        <p>Check your people and your systems in the same six weeks. One project, two reports,
        one meeting with you — and the order to fix things in, cheapest and fastest first.
        Nobody else in the Indian mid-market offers both together.</p>
      </div>

      <h2>Not sure which one?</h2>
      <p>That is the normal starting position, and it is what the
      <a href="/consulting/">health check</a> is for: six weeks, fifteen areas, each scored
      with the evidence. Tell us what is going wrong and we will point you at the cheapest
      thing that fixes it. Sometimes the honest answer is that you do not need us yet, and we
      will say so.</p>""" % packs_html(),
    extra_ld="""<script type="application/ld+json">
{"@context":"https://schema.org","@type":"OfferCatalog","name":"AllAboutHR packages",
"url":"https://allabouthr.co/packages/",
"provider":{"@id":"https://allabouthr.co/#organization"},
"itemListElement":[%s]}
</script>""" % packs_ld(),
    cards=[
        ("/consulting/", "p", "Consulting", "The Growth Loop",
         "What the packages actually deliver, step by step.",
         "See how we work"),
        ("/alvora/", "p", "Software", "Alvora",
         "Which platform comes with which package.",
         "See the software"),
        ("/contact-us/", "t", "Contact", "Get a price",
         "Tell us your headcount and we will send a costed proposal — or an honest “not yet”.",
         "Ask for a quote"),
    ],
    cta_h2="Tell us your headcount.",
    cta_p=("That is all we need to price it. You will get a table showing exactly what you get "
           "at that size, before you sign anything."),
    wa="Hi%20AllAboutHR%20%E2%80%94%20please%20price%20a%20package%20for%20my%20headcount.",
    cta_second=("/consulting/", "See how we work"),
)
