"""
Seed data for CareerOS. Called once on first run.
Merges with any existing DB rows — will not create duplicates (matches on name).
"""

from datetime import date

SEED_CONTACTS = [
    {
        "name": "Dolf Gielen",
        "title": "Senior Energy Specialist",
        "organization": "World Bank ESMAP",
        "email": "",
        "relationship_context": (
            "Senior colleague at WB ESMAP. During WB restructuring meeting on March 20 gave name of "
            "KIEPR hiring manager Ani Balabanyan. NOTE: do NOT route IRENA approach through Dolf."
        ),
        "status": "Hold",
        "last_contact_date": date(2026, 3, 20),
        "next_action": "WB restructuring — no clarity until June. Revisit first week of June if still needed.",
        "next_action_date": date(2026, 6, 1),
        "thread": [
            {
                "date": date(2026, 3, 20),
                "entry_type": "call",
                "content": (
                    "Connected re WB opportunities. WB restructuring ongoing — no clarity until June. "
                    "Dolf provided KIEPR hiring manager contact: Ani Balabanyan (abalabanyan@worldbank.org). "
                    "Outcome: Put WB track on hold; pursue KIEPR directly and independently."
                ),
            }
        ],
    },
    {
        "name": "Ani Balabanyan",
        "title": "Manager, Energy Policy & Regulations, KIEPR",
        "organization": "World Bank",
        "email": "abalabanyan@worldbank.org",
        "relationship_context": (
            "KIEPR (Knowledge, Innovation & Economics for the Power and Renewables) hiring manager at WB. "
            "Contact provided by Dolf Gielen on March 20. Cold outreach — no prior relationship."
        ),
        "status": "Pending",
        "last_contact_date": None,
        "next_action": "Send email Monday March 23 from Harvard email address. Reference Dolf lightly.",
        "next_action_date": date(2026, 3, 23),
        "thread": [],
    },
    {
        "name": "Michelle Hallack",
        "title": "Energy Economist",
        "organization": "World Bank ESMAP",
        "email": "",
        "relationship_context": (
            "Colleague at WB ESMAP. Pattern of non-response to outreach. Low priority until she initiates."
        ),
        "status": "Hold",
        "last_contact_date": None,
        "next_action": "Hold — do not initiate again. Respond warmly if she reaches out.",
        "next_action_date": None,
        "thread": [],
    },
    {
        "name": "Surbhi Bhardwaj",
        "title": "Senior Energy Specialist",
        "organization": "World Bank India",
        "email": "",
        "relationship_context": (
            "Worked together closely on the $3B World Bank PforR for India MNRE. "
            "Warm goodbye when I left for Harvard in 2024. Strong shared history."
        ),
        "status": "Warm",
        "last_contact_date": None,
        "next_action": "Send a warm personal note — catch up, mention job search, ask if she knows of WB openings.",
        "next_action_date": date(2026, 3, 24),
        "thread": [],
    },
    {
        "name": "Pawan Mulukutla",
        "title": "Executive Director, Integrated Transport, Clean Air & Hydrogen",
        "organization": "WRI India",
        "email": "",
        "relationship_context": (
            "Created a role for me at WRI India in 2023. I left on excellent terms in August 2024 to come to Harvard. "
            "Knows my work deeply. Call scheduled Monday March 23 at 8:30am IST."
        ),
        "status": "Active",
        "last_contact_date": date(2026, 3, 20),
        "next_action": "Call Monday March 23 at 8:30am IST. Explore whether WRI India has a senior role.",
        "next_action_date": date(2026, 3, 23),
        "thread": [
            {
                "date": date(2026, 3, 20),
                "entry_type": "sent",
                "content": "Reached out to reconnect and schedule call. Call confirmed for Monday March 23 8:30am IST.",
            }
        ],
    },
    {
        "name": "Jamie Ferguson",
        "title": "Global Head of Climate",
        "organization": "IFC",
        "email": "",
        "relationship_context": (
            "Prior warm LinkedIn exchange. Senior IFC climate lead — high-value target for climate finance/policy roles."
        ),
        "status": "Pending",
        "last_contact_date": None,
        "next_action": "Follow up Thursday March 26 — LinkedIn message or email.",
        "next_action_date": date(2026, 3, 26),
        "thread": [],
    },
    {
        "name": "Mahesh Naik",
        "title": "Strategy Office",
        "organization": "World Bank",
        "email": "",
        "relationship_context": "HKS MPA/MC 2023 alum. World Bank Strategy Office — useful for internal WB intel and referrals.",
        "status": "Pending",
        "last_contact_date": None,
        "next_action": "Send note Tuesday March 24 — alumni connection angle, ask for 20 min call.",
        "next_action_date": date(2026, 3, 24),
        "thread": [],
    },
    {
        "name": "Ankur Dhanuka",
        "title": "Investment Officer, Climate",
        "organization": "IFC",
        "email": "",
        "relationship_context": "Warm relationship. IFC climate investment officer — potential referral into IFC climate or energy team.",
        "status": "Warm",
        "last_contact_date": None,
        "next_action": "Send note Wednesday March 25.",
        "next_action_date": date(2026, 3, 25),
        "thread": [],
    },
    {
        "name": "Obinna Oisiadinso",
        "title": "Digital Infrastructure Lead",
        "organization": "IFC",
        "email": "",
        "relationship_context": (
            "Ghosted two emails. AI/data center infrastructure angle relevant to Belfer research. "
            "Only try via LinkedIn — max 3 sentences."
        ),
        "status": "No Response",
        "last_contact_date": None,
        "next_action": "One final attempt: 3-sentence LinkedIn message only. If no response, close.",
        "next_action_date": date(2026, 3, 27),
        "thread": [],
    },
    {
        "name": "R. Balaji",
        "title": "Senior Industry Specialist",
        "organization": "IFC",
        "email": "",
        "relationship_context": (
            "Good call in July 2025. No response to January 2026 email. "
            "IFC industry specialist — worth one more try via different channel."
        ),
        "status": "No Response",
        "last_contact_date": date(2026, 1, 15),
        "next_action": "Try LinkedIn InMail this week — reference July call, keep it brief.",
        "next_action_date": date(2026, 3, 25),
        "thread": [
            {
                "date": date(2025, 7, 15),
                "entry_type": "call",
                "content": "Good exploratory call. Discussed IFC energy and climate opportunities. Agreed to stay in touch.",
            },
            {
                "date": date(2026, 1, 15),
                "entry_type": "sent",
                "content": "Follow-up email referencing July call. No response received.",
            },
        ],
    },
    {
        "name": "Simon Black",
        "title": "Senior Economist",
        "organization": "IMF",
        "email": "",
        "relationship_context": "IMF economist. Not a priority at this stage.",
        "status": "Cold",
        "last_contact_date": None,
        "next_action": "Not a priority. No action needed.",
        "next_action_date": None,
        "thread": [],
    },
    {
        "name": "Shubham",
        "title": "Contact",
        "organization": "Avina Inc",
        "email": "",
        "relationship_context": "Avina Inc contact. CV sent March 20. CEO has been briefed. Awaiting call setup.",
        "status": "Active",
        "last_contact_date": date(2026, 3, 20),
        "next_action": "Await call setup — follow up if no contact by March 26.",
        "next_action_date": date(2026, 3, 26),
        "thread": [
            {
                "date": date(2026, 3, 20),
                "entry_type": "sent",
                "content": "CV sent to Shubham at Avina Inc. CEO has been briefed on my background. Awaiting call scheduling.",
            }
        ],
    },
    {
        "name": "Sharad Bharadwaj",
        "title": "Associate Director",
        "organization": "E3",
        "email": "",
        "relationship_context": (
            "Went through final round interview with E3 in February 2025. Strong fit with energy/policy work. "
            "Now applying for the full-time Associate Director role."
        ),
        "status": "Pending",
        "last_contact_date": date(2025, 2, 28),
        "next_action": "Apply for full-time AD role at E3 today. Reference Feb 2025 final round.",
        "next_action_date": date(2026, 3, 20),
        "thread": [
            {
                "date": date(2025, 2, 28),
                "entry_type": "call",
                "content": "Final round interview at E3 for Associate Director role. Strong performance but role did not close.",
            }
        ],
    },
    {
        "name": "Simi Rose George",
        "title": "Head, Energy Storage",
        "organization": "California Energy Commission",
        "email": "",
        "relationship_context": (
            "HKS MPA/ID alum. Promised last summer to send Belfer policy brief on AI/data center/grid. "
            "Have not yet followed through."
        ),
        "status": "Pending",
        "last_contact_date": None,
        "next_action": "Send Belfer brief with personal note this week — fulfill the promise made last summer.",
        "next_action_date": date(2026, 3, 24),
        "thread": [],
    },
    {
        "name": "Bharat Thakre",
        "title": "Engineer",
        "organization": "Amazon (Palm Springs)",
        "email": "",
        "relationship_context": (
            "Close friend. Currently at Amazon. AWS job IDs of interest: 3112034 and 3059008. "
            "Normal friend call — also explore internal Amazon referral."
        ),
        "status": "Pending",
        "last_contact_date": None,
        "next_action": "Normal friend call this week. Mention AWS job IDs 3112034 and 3059008.",
        "next_action_date": date(2026, 3, 25),
        "thread": [],
    },
    {
        "name": "Vrushali Gaud",
        "title": "Global Director, Climate Operations",
        "organization": "Google",
        "email": "",
        "relationship_context": "Senior Google climate leader. InMail sent March 20. High-value connection for climate/energy policy at Google.",
        "status": "Active",
        "last_contact_date": date(2026, 3, 20),
        "next_action": "Await LinkedIn InMail response. Follow up if no response by March 27.",
        "next_action_date": date(2026, 3, 27),
        "thread": [
            {
                "date": date(2026, 3, 20),
                "entry_type": "linkedin",
                "content": "LinkedIn InMail sent to Vrushali Gaud re Google climate/energy policy opportunities.",
            }
        ],
    },
    {
        "name": "Chester Chua",
        "title": "Head, APAC AI Policy",
        "organization": "Google Cloud",
        "email": "",
        "relationship_context": (
            "HKS MPA/ID alum (Class of 2007). APAC AI policy lead at Google Cloud — strong overlap with "
            "Belfer AI/energy research. Alumni connection gives a warm in."
        ),
        "status": "Warm",
        "last_contact_date": None,
        "next_action": "Send LinkedIn InMail Tuesday March 24 — lead with HKS alumni connection + Belfer AI/grid work.",
        "next_action_date": date(2026, 3, 24),
        "thread": [],
    },
    {
        "name": "Suchit Puri",
        "title": "AI Lead",
        "organization": "Google Cloud India",
        "email": "",
        "relationship_context": "School friend. AI lead at Google Cloud India. Personal relationship — WhatsApp is the right channel.",
        "status": "Warm",
        "last_contact_date": None,
        "next_action": "WhatsApp this week — personal check-in, then mention job search and Google interest.",
        "next_action_date": date(2026, 3, 24),
        "thread": [],
    },
    {
        "name": "Gauri Singh",
        "title": "Deputy Director-General",
        "organization": "IRENA",
        "email": "",
        "relationship_context": (
            "Former Joint Secretary MNRE — worked closely together. Now DDG at IRENA Abu Dhabi. "
            "IMPORTANT: Reach out directly. Do NOT go through Dolf Gielen."
        ),
        "status": "Warm",
        "last_contact_date": None,
        "next_action": "Direct personal outreach — email or LinkedIn. Reference shared MNRE work, ask about IRENA senior openings.",
        "next_action_date": date(2026, 3, 26),
        "thread": [],
    },
]


SEED_APPLICATIONS = [
    {
        "role": "Senior Energy Specialist, KIEPR",
        "organization": "World Bank",
        "req_number": "req35851",
        "status": "Applied",
        "applied_date": date(2026, 3, 19),
        "deadline": None,
        "location": "Washington DC",
        "notes": "Submitted March 19. Ani Balabanyan is hiring manager. Follow up after email March 23.",
        "lane": "Lane A",
    },
    {
        "role": "Associate Director",
        "organization": "E3",
        "req_number": "",
        "status": "Drafting",
        "applied_date": None,
        "deadline": date(2026, 3, 20),
        "location": "Washington DC / Remote",
        "notes": "Apply today. Reference Feb 2025 final-round interview with Sharad Bharadwaj.",
        "lane": "Lane A",
    },
    {
        "role": "Experienced Professional, Fast-Track",
        "organization": "Asian Development Bank",
        "req_number": "",
        "status": "Drafting",
        "applied_date": None,
        "deadline": date(2026, 3, 27),
        "location": "Manila / Various",
        "notes": "Apply this week. Fast-track program for mid-career professionals.",
        "lane": "Lane B",
    },
    {
        "role": "TBD Senior Role",
        "organization": "Avina Inc",
        "req_number": "",
        "status": "Under Review",
        "applied_date": date(2026, 3, 20),
        "deadline": None,
        "location": "TBD",
        "notes": "CV sent March 20. CEO briefed. Awaiting call. Shubham is contact.",
        "lane": "Lane A",
    },
    {
        "role": "Energy Specialist (Vienna)",
        "organization": "World Bank ECA",
        "req_number": "req36031",
        "status": "Drafting",
        "applied_date": None,
        "deadline": None,
        "location": "Vienna, Austria",
        "notes": "Decide after Pawan call March 23. ECA energy team.",
        "lane": "Lane B",
    },
    {
        "role": "Energy Specialist (Serbia)",
        "organization": "World Bank ECA",
        "req_number": "",
        "status": "Drafting",
        "applied_date": None,
        "deadline": None,
        "location": "Belgrade, Serbia",
        "notes": "Decide after Pawan call March 23. ECA energy team.",
        "lane": "Lane B",
    },
    # ── Tech & Consulting pipeline ──────────────────────────────────────────────
    {
        "role": "Sr Delivery Consultant",
        "organization": "AWS",
        "status": "Rejected",
        "lane": "Lane C",
    },
    {
        "role": "Strategic Negotiator Data Centers",
        "organization": "Google",
        "status": "Drafting",
        "lane": "Lane C",
    },
    {
        "role": "Consulting Manager Energy Transition",
        "organization": "S&P Global",
        "status": "Drafting",
        "lane": "Lane C",
    },
    {
        "role": "Director Industrial Decarbonization",
        "organization": "PwC",
        "status": "Applied",
        "lane": "Lane C",
    },
    {
        "role": "Consultant Utilities",
        "organization": "PA Associates",
        "status": "Applied",
        "lane": "Lane C",
    },
    {
        "role": "Sr Energy Markets PM",
        "organization": "Microsoft",
        "status": "Applied",
        "lane": "Lane C",
    },
    {
        "role": "Energy Manager Commercial Supply",
        "organization": "Meta",
        "status": "Applied",
        "lane": "Lane C",
    },
    {
        "role": "Energy & Climate Policy Lead",
        "organization": "CoreWeave",
        "status": "Applied",
        "lane": "Lane C",
    },
    {
        "role": "Utility Advisory Consultant",
        "organization": "PA Consulting",
        "status": "Applied",
        "lane": "Lane C",
    },
    {
        "role": "Energy Manager Clean Energy",
        "organization": "Meta",
        "status": "Applied",
        "lane": "Lane C",
    },
    {
        "role": "Technical PM Global Infrastructure",
        "organization": "Google",
        "status": "Drafting",
        "lane": "Lane C",
    },
    {
        "role": "Senior Consultant",
        "organization": "NERA",
        "status": "Drafting",
        "lane": "Lane C",
    },
    {
        "role": "Senior Director Power & Renewables",
        "organization": "FTI",
        "status": "Drafting",
        "lane": "Lane C",
    },
    {
        "role": "Energy Infrastructure Lead EMEA",
        "organization": "Ada Infrastructure",
        "status": "Drafting",
        "lane": "Lane C",
    },
    {
        "role": "Contract PM Global Infrastructure",
        "organization": "Google",
        "status": "Drafting",
        "lane": "Lane C",
    },
    {
        "role": "Renewable Energy Procurement APJC",
        "organization": "Amazon",
        "status": "Drafting",
        "lane": "Lane C",
    },
    {
        "role": "Sr Manager Green Finance",
        "organization": "Climate Policy Initiative",
        "status": "Drafting",
        "lane": "Lane C",
    },
    {
        "role": "Industrial Electrification",
        "organization": "Agora",
        "status": "Drafting",
        "lane": "Lane C",
    },
    {
        "role": "Senior Director",
        "organization": "MTI",
        "status": "Drafting",
        "lane": "Lane C",
    },
    {
        "role": "Head ESaaS",
        "organization": "Keppel",
        "status": "Drafting",
        "lane": "Lane C",
    },
    {
        "role": "Sr Manager Storage",
        "organization": "ESVolta",
        "status": "Drafting",
        "lane": "Lane C",
    },
]


CV_BULLETS = [
    # ── MNRE (2016-2024) ──────────────────────────────────────────────────────
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Led the $2.1B National Green Hydrogen Mission — drafted policy framework, financial architecture, and inter-ministerial coordination.",
     "tags": "hydrogen,policy,government,mission,energy transition,emerging markets"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Led India's $9B national solar rooftop program — designed regulatory framework, subsidy mechanisms, and deployment targets.",
     "tags": "solar,renewable energy,rooftop,policy,government,deployment"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Drafted Electricity Act amendments and National Tariff Policy revisions governing India's power sector.",
     "tags": "electricity,tariff,regulation,policy,legislation,power sector"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Designed transmission pricing and open access frameworks enabling 100 GW+ of renewable energy integration into the grid.",
     "tags": "transmission,grid,open access,renewable integration,100GW,infrastructure"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Negotiated regulatory and cost-allocation frameworks with 50+ utilities and state regulators across India.",
     "tags": "regulation,negotiation,utilities,state regulators,cost allocation,stakeholder"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Structured RPO compliance and renewable energy certificate market mechanisms for national adoption.",
     "tags": "RPO,REC,compliance,market,renewable,certificate"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Led India-US and India-Germany Bilateral Hydrogen Task Forces; served as national representative to IPHE.",
     "tags": "hydrogen,bilateral,diplomacy,IPHE,international,task force,US,Germany"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Contributed to G20 Energy Transition Working Group under India's presidency — drafted green hydrogen and energy transition text.",
     "tags": "G20,energy transition,presidency,multilateral,green hydrogen,diplomacy"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Led technical negotiations and results-framework design for a $3B World Bank Program-for-Results (PforR) linking disbursement to policy milestones.",
     "tags": "World Bank,PforR,results framework,negotiation,development finance,$3B"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Managed a $10M/year R&D portfolio — evaluated hydrogen, fuel cells, flow batteries, and ocean energy projects from IITs, IISc, and CSIR.",
     "tags": "R&D,portfolio management,hydrogen,fuel cells,batteries,storage,innovation"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Approved NTPC green hydrogen bus pilot in Leh; rejected gravity storage pilot after independent techno-economic modeling.",
     "tags": "hydrogen,bus,pilot,storage,NTPC,techno-economic,modeling"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Negotiated 15-year take-or-pay green ammonia offtake agreements with fertilizer manufacturers, replacing short-term grey ammonia contracts.",
     "tags": "ammonia,offtake,fertilizer,take-or-pay,commercial,hydrogen,industrial"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Designed the $1.8B Production-Linked Incentive (PLI) mechanism for green hydrogen electrolyzers and components.",
     "tags": "PLI,incentive,electrolyzer,manufacturing,green hydrogen,industrial policy"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Contributed to India's Biennial Update Report to UNFCCC; prepared India's Article 6 Paris Agreement negotiating position.",
     "tags": "UNFCCC,climate,Paris Agreement,Article 6,carbon markets,NDC"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Coordinated India-ISA energy access programs for 5 African countries and 5 Small Island Developing States.",
     "tags": "ISA,energy access,Africa,SIDS,international,solar,development"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Built LCOE/LCOH models, battery storage optimization models, and viability gap funding models for policy analysis.",
     "tags": "LCOE,LCOH,modeling,battery,storage,viability gap,quantitative,financial"},
    {"employer": "Ministry of New and Renewable Energy (MNRE), Government of India", "period": "2016–2024",
     "bullet_text": "Led team of 20 including consultants, technical experts, and young professionals across hydrogen and renewables programs.",
     "tags": "leadership,team,management,consultants,technical,capacity"},

    # ── Belfer Center (2025-present) ─────────────────────────────────────────
    {"employer": "Harvard Kennedy School, Belfer Center for Science and International Affairs", "period": "2025–present",
     "bullet_text": "Analyzed interconnection bottlenecks in PJM and ERCOT and their implications for hyperscale AI data center siting.",
     "tags": "PJM,ERCOT,interconnection,data centers,AI,grid,transmission,US"},
    {"employer": "Harvard Kennedy School, Belfer Center for Science and International Affairs", "period": "2025–present",
     "bullet_text": "Developed regulatory and financial risk frameworks for integrating gigawatt-scale data center loads into US electricity markets.",
     "tags": "data centers,AI,regulation,financial risk,electricity markets,grid,policy"},
    {"employer": "Harvard Kennedy School, Belfer Center for Science and International Affairs", "period": "2025–present",
     "bullet_text": "Assessed transmission cost allocation and reserve margin risks under gigawatt-scale data center clustering in US grids.",
     "tags": "transmission,cost allocation,reserve margin,data centers,grid stability"},
    {"employer": "Harvard Kennedy School, Belfer Center for Science and International Affairs", "period": "2025–present",
     "bullet_text": "Evaluated technical and commercial viability of SMRs, geothermal, and long-duration storage as power sources for AI data centers.",
     "tags": "SMR,nuclear,geothermal,long-duration storage,data centers,AI,clean energy"},
    {"employer": "Harvard Kennedy School, Belfer Center for Science and International Affairs", "period": "2025–present",
     "bullet_text": "Designed policy and commercial pathways to accelerate time-to-power for new generation serving data center demand.",
     "tags": "policy,commercial,time-to-power,data centers,generation,procurement"},
    {"employer": "Harvard Kennedy School, Belfer Center for Science and International Affairs", "period": "2025–present",
     "bullet_text": "Quantified capital cost impacts of reliability pricing reforms (CONE, ICAP) on data center energy procurement strategies.",
     "tags": "reliability pricing,CONE,ICAP,capital cost,data centers,electricity markets"},
    {"employer": "Harvard Kennedy School, Belfer Center for Science and International Affairs", "period": "2025–present",
     "bullet_text": "Published two Belfer Center policy briefs on AI, data centers, and US grid policy; authored SYPA 'Cables Before Compute' submitted to Ministry of Power.",
     "tags": "publication,policy brief,AI,data centers,grid,Belfer,research,writing"},

    # ── WB ESMAP (2025) ───────────────────────────────────────────────────────
    {"employer": "World Bank ESMAP", "period": "2025",
     "bullet_text": "Designed demand and evaluation framework for clean hydrogen deployment in emerging markets.",
     "tags": "hydrogen,emerging markets,demand,evaluation,framework,World Bank"},
    {"employer": "World Bank ESMAP", "period": "2025",
     "bullet_text": "Built techno-economic and unit economics models for green hydrogen in steel, fertilizer, refining, and transport value chains.",
     "tags": "techno-economic,modeling,hydrogen,steel,fertilizer,refining,transport,unit economics"},
    {"employer": "World Bank ESMAP", "period": "2025",
     "bullet_text": "Designed concessional finance and credit enhancement structures to catalyze clean hydrogen investment in emerging markets.",
     "tags": "concessional finance,credit enhancement,blended finance,hydrogen,emerging markets,investment"},
    {"employer": "World Bank ESMAP", "period": "2025",
     "bullet_text": "Supported cross-country market creation strategies for green hydrogen in South Asia, Sub-Saharan Africa, and Southeast Asia.",
     "tags": "market creation,green hydrogen,South Asia,Africa,Southeast Asia,strategy"},

    # ── WRI India (2024) ──────────────────────────────────────────────────────
    {"employer": "World Resources Institute (WRI) India", "period": "2024",
     "bullet_text": "Led hydrogen and energy storage initiatives — evaluated BESS deployment models and revenue-stacking strategies.",
     "tags": "WRI,hydrogen,BESS,battery storage,revenue stacking,deployment"},
    {"employer": "World Resources Institute (WRI) India", "period": "2024",
     "bullet_text": "Structured procurement frameworks for hydrogen pilots and industrial electrification programs in India.",
     "tags": "procurement,hydrogen,industrial electrification,pilots,India"},

    # ── Welspun Energy (2011-2016) ────────────────────────────────────────────
    {"employer": "Welspun Energy", "period": "2011–2016",
     "bullet_text": "Led technical due diligence for the $1.3B divestment of a 940 MW renewable energy portfolio.",
     "tags": "due diligence,divestment,renewable energy,private sector,$1.3B,M&A,portfolio"},
    {"employer": "Welspun Energy", "period": "2011–2016",
     "bullet_text": "Built financial and operational models for renewable energy assets; managed operations across 15 assets.",
     "tags": "financial modeling,operations,renewable energy,asset management,private sector"},
    {"employer": "Welspun Energy", "period": "2011–2016",
     "bullet_text": "Deployed predictive maintenance systems across renewable fleet; led ISO 9001 quality certification.",
     "tags": "predictive maintenance,operations,ISO 9001,quality,renewable energy"},

    # ── Reliance Infrastructure (2009-2011) ───────────────────────────────────
    {"employer": "Reliance Infrastructure", "period": "2009–2011",
     "bullet_text": "Managed procurement for a 4,000 MW thermal power project; achieved 10% cost reduction through competitive bidding.",
     "tags": "procurement,thermal power,cost reduction,infrastructure,private sector"},
]


# ── Seed tasks ────────────────────────────────────────────────────────────────
# linked_contact: matched by name at seed time (case-insensitive)
# due_date: None = no fixed date, "today" = date.today(), "YYYY-MM-DD" = fixed

SEED_TASKS = [
    # TODAY — April 3
    {"title": "Google Assessment — check email, act immediately if present",
     "category": "Career", "priority": "High", "time_estimate": "15 min",
     "due_date": date(2026, 4, 3)},
    {"title": "Jamie Ferguson — LinkedIn message (10 min)",
     "category": "Career", "priority": "High", "time_estimate": "10 min",
     "due_date": date(2026, 4, 3), "linked_contact": "Jamie Ferguson"},
    {"title": "Gauri Singh — IRENA outreach (10 min)",
     "category": "Career", "priority": "High", "time_estimate": "10 min",
     "due_date": date(2026, 4, 3), "linked_contact": "Gauri Singh"},
    {"title": "Anthony Martin (DESRI) — HKS alumni outreach",
     "category": "Career", "priority": "Medium", "time_estimate": "10 min",
     "due_date": date(2026, 4, 3)},
    {"title": "Mike Alter (Microsoft) — HKS alumni outreach, mention existing application",
     "category": "Career", "priority": "Medium", "time_estimate": "10 min",
     "due_date": date(2026, 4, 3)},
    {"title": "Check if Dr. Maithani responded about Siddharthan and WB Narayan",
     "category": "Career", "priority": "Medium", "time_estimate": "5 min",
     "due_date": date(2026, 4, 3)},
    {"title": "Herif Jones — Order Regalia",
     "category": "Personal", "priority": "High", "time_estimate": "10 min",
     "due_date": date(2026, 4, 3)},

    # THIS WEEKEND — April 5–6
    {"title": "US Taxes — block 3–4 hours, file if documents ready",
     "category": "Personal", "priority": "High", "time_estimate": "3–4 hours",
     "due_date": date(2026, 4, 6)},
    {"title": "Driving licence test — 45 quiet minutes",
     "category": "Personal", "priority": "Medium", "time_estimate": "45 min",
     "due_date": date(2026, 4, 6)},
    {"title": "Pawan follow-up — gentle nudge on ClimateWorks, Dan Lashof, Jennifer Laky intros",
     "category": "Career", "priority": "Medium", "time_estimate": "10 min",
     "due_date": date(2026, 4, 5), "linked_contact": "Pawan Mulukutla"},
    {"title": "LinkedIn post on SYPA work",
     "category": "Career", "priority": "Low", "time_estimate": "30 min",
     "due_date": date(2026, 4, 6)},

    # MONDAY April 6
    {"title": "Rachel RA meeting — come with specific ask",
     "category": "Academic", "priority": "High", "time_estimate": "1 hour",
     "due_date": date(2026, 4, 6)},
    {"title": "Mahesh Naik — WB alumni note",
     "category": "Career", "priority": "High", "time_estimate": "10 min",
     "due_date": date(2026, 4, 6), "linked_contact": "Mahesh Naik"},
    {"title": "Ankur Dhanuka — IFC note",
     "category": "Career", "priority": "High", "time_estimate": "10 min",
     "due_date": date(2026, 4, 6), "linked_contact": "Ankur Dhanuka"},
    {"title": "R. Balaji — LinkedIn InMail",
     "category": "Career", "priority": "High", "time_estimate": "10 min",
     "due_date": date(2026, 4, 6), "linked_contact": "R. Balaji"},
    {"title": "Obinna — final 3-sentence LinkedIn message, then close",
     "category": "Career", "priority": "High", "time_estimate": "5 min",
     "due_date": date(2026, 4, 6), "linked_contact": "Obinna Oisiadinso"},
    {"title": "Jeff Bryant (Enfinity) — HKS alumni outreach",
     "category": "Career", "priority": "Medium", "time_estimate": "10 min",
     "due_date": date(2026, 4, 6)},
    {"title": "Will Eberle (RWE) — HKS alumni outreach",
     "category": "Career", "priority": "Medium", "time_estimate": "10 min",
     "due_date": date(2026, 4, 6)},
    {"title": "UC Berkeley — send Nikit/Amol outreach",
     "category": "Career", "priority": "Medium", "time_estimate": "15 min",
     "due_date": date(2026, 4, 6)},
    {"title": "CSIS — identify contact and send note",
     "category": "Career", "priority": "Medium", "time_estimate": "20 min",
     "due_date": date(2026, 4, 6)},
    {"title": "Faculty outreach — Henry Lee, Akash Deep, Eli Sandler",
     "category": "Academic", "priority": "Medium", "time_estimate": "20 min",
     "due_date": date(2026, 4, 6)},

    # THIS WEEK — April 7–11
    {"title": "API 148 assignment — block Wednesday or Thursday (5–6 hours)",
     "category": "Academic", "priority": "High", "time_estimate": "5–6 hours",
     "due_date": date(2026, 4, 10)},
    {"title": "E3 AD application — submit directly without Sharad referral",
     "category": "Career", "priority": "High", "time_estimate": "2 hours",
     "due_date": date(2026, 4, 10)},
    {"title": "Avina — nudge Shubham if nothing by end of week",
     "category": "Career", "priority": "Medium", "time_estimate": "5 min",
     "due_date": date(2026, 4, 11), "linked_contact": "Shubham"},
    {"title": "Suchit — check for other Google roles worth applying through referral link",
     "category": "Career", "priority": "Medium", "time_estimate": "15 min",
     "due_date": date(2026, 4, 9), "linked_contact": "Suchit Puri"},
    {"title": "ADB Fast-Track — check if still accepting applications",
     "category": "Career", "priority": "Medium", "time_estimate": "10 min",
     "due_date": date(2026, 4, 9)},

    # NEXT WEEK — ongoing
    {"title": "Tier 2 Glenn contacts — Alla Jezmir, Dan Peckham, Jason Peuquet",
     "category": "Career", "priority": "Low", "time_estimate": "30 min",
     "due_date": date(2026, 4, 13)},
    {"title": "Ratnika Prasad — quick LinkedIn check before deciding",
     "category": "Career", "priority": "Low", "time_estimate": "5 min",
     "due_date": date(2026, 4, 13)},
]
