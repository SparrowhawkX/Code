"""
CareerOS seed data — updated May 11, 2026.
Loaded once on first run (or after Archive All + restart).
"""

from datetime import date

# ── Contacts ──────────────────────────────────────────────────────────────────

SEED_CONTACTS = [

    # ── US Track ──────────────────────────────────────────────────────────────

    {
        "name": "Jennifer Layke",
        "title": "Executive Director",
        "organization": "ACEEE",
        "relationship_context": (
            "Intro via Pawan Mulukutla. Former WRI Global Energy Director 2016-2025, now ED at ACEEE. "
            "Call May 1 — strong connection; she read the Belfer paper. Offered to forward resume to contacts. "
            "Suggested bridge/consulting roles to build US market context."
        ),
        "status": "Warm",
        "last_contact_date": date(2026, 5, 1),
        "next_action": "Await introductions Jennifer offered to make",
        "next_action_date": None,
        "thread": [
            {
                "date": date(2026, 5, 1),
                "entry_type": "call",
                "content": (
                    "Call May 1 — strong connection. She read the Belfer paper. "
                    "Suggested bridge/consulting roles to build US market context. "
                    "Offered to forward resume to her network. "
                    "Follow-up email + cover note sent same day."
                ),
            }
        ],
    },

    {
        "name": "Lena Diaz",
        "title": "Senior Talent Acquisition Partner",
        "organization": "ICF",
        "relationship_context": (
            "Called Dipesh May 8 after Reed Leon-Hinton circulated his profile internally. "
            "MOST ACTIVE US LEAD — respond immediately when her email arrives."
        ),
        "status": "Active",
        "last_contact_date": date(2026, 5, 8),
        "next_action": "Respond immediately when Lena Diaz email arrives",
        "next_action_date": date(2026, 5, 12),
        "thread": [
            {
                "date": date(2026, 5, 8),
                "entry_type": "received",
                "content": (
                    "Lena called after Reed Leon-Hinton circulated profile internally. "
                    "Left voicemail May 8 — she is following up with email. "
                    "This is the most active US lead."
                ),
            }
        ],
    },

    {
        "name": "Reed Leon-Hinton",
        "title": "Senior Consultant, Power Markets",
        "organization": "ICF",
        "relationship_context": (
            "Works on ERCOT wholesale market projections for asset owners. "
            "Call May 7 — agreed to circulate profile internally, which led to Lena Diaz contact."
        ),
        "status": "Warm",
        "last_contact_date": date(2026, 5, 7),
        "next_action": "Keep warm — Lena Diaz is the active ICF thread",
        "next_action_date": None,
        "thread": [
            {
                "date": date(2026, 5, 7),
                "entry_type": "call",
                "content": (
                    "Call May 7 — 20 minutes. Works on ERCOT wholesale market projections for asset owners. "
                    "Agreed to circulate profile internally — led to Lena Diaz contact. "
                    "Follow-up email sent with April 2026 resume."
                ),
            }
        ],
    },

    {
        "name": "Erika Myers",
        "organization": "CharIN Global",
        "relationship_context": (
            "Call May 11 — no openings, not aware of any. Husband at CSIS — offered to put in a word. "
            "Suggested think tanks (WRI, others). Follow-up email with resume sent. "
            "Keep warm — fresh CSIS entry point via husband."
        ),
        "status": "Warm",
        "last_contact_date": date(2026, 5, 11),
        "next_action": "Keep warm. Follow up if CSIS position opens via husband",
        "next_action_date": None,
        "thread": [
            {
                "date": date(2026, 5, 11),
                "entry_type": "call",
                "content": (
                    "Call May 11 — no openings at CharIN, not aware of any relevant openings elsewhere. "
                    "Husband at CSIS — offered to put in a word if position opens. "
                    "Suggested think tanks (WRI, others). Asked for follow-up email with resume — sent."
                ),
            }
        ],
    },

    {
        "name": "Hy Martin",
        "organization": "DESRI India",
        "relationship_context": (
            "HKS MPA/ID + MBA alum. Responded to cold outreach. "
            "Call moved up from May 29 to May 15. DESRI India has India operations."
        ),
        "status": "Active",
        "last_contact_date": date(2026, 5, 11),
        "next_action": "Prep for call May 15 — DESRI India operations focus",
        "next_action_date": date(2026, 5, 15),
        "thread": [
            {
                "date": date(2026, 5, 11),
                "entry_type": "note",
                "content": (
                    "HKS MPA/ID + MBA alum. Responded to cold outreach. "
                    "Call moved up from May 29 to May 15. DESRI India has India operations — prep needed."
                ),
            }
        ],
    },

    {
        "name": "Anup Bandivadekar",
        "organization": "Hewlett Foundation",
        "relationship_context": "Intro via Pawan Mulukutla. Confirmed availability May 9+.",
        "status": "Pending",
        "last_contact_date": None,
        "next_action": "Schedule call this week (May 12)",
        "next_action_date": date(2026, 5, 12),
        "thread": [],
    },

    {
        "name": "Afeena Ashfaq",
        "organization": "SED Foundation",
        "relationship_context": "Intro via Pawan Mulukutla. Was travelling — follow-up sent.",
        "status": "Pending",
        "last_contact_date": None,
        "next_action": "Await response to follow-up",
        "next_action_date": None,
        "thread": [],
    },

    {
        "name": "Lakshmi Rajagopalan",
        "organization": "",
        "relationship_context": "Intro via Pawan Mulukutla. Responded — busy until mid-June.",
        "status": "Hold",
        "last_contact_date": None,
        "next_action": "Connect mid-June",
        "next_action_date": date(2026, 6, 15),
        "thread": [],
    },

    {
        "name": "Surhud Vaidya",
        "title": "Consultant, Distribution/DERs",
        "organization": "ICF",
        "relationship_context": (
            "Call April 28 — 15 min routing call only. Introduced Reed Leon-Hinton. "
            "Track closed — Reed and Lena are the active ICF threads."
        ),
        "status": "Hold",
        "last_contact_date": date(2026, 4, 28),
        "next_action": None,
        "next_action_date": None,
        "thread": [
            {
                "date": date(2026, 4, 28),
                "entry_type": "call",
                "content": "15 min routing call. Introduced Reed Leon-Hinton. Track closed — Reed and Lena active.",
            }
        ],
    },

    # ── India Track ────────────────────────────────────────────────────────────

    {
        "name": "Pawan Mulukutla",
        "organization": "WRI India",
        "relationship_context": (
            "Activated April 28 after long delay. Made 5 introductions same day "
            "(Jennifer Layke, Lakshmi, Anup, Afeena, Erika). "
            "Informed Madhav (WRI India CEO) — door open for India conversation. "
            "Dipesh confirmed India on table from July. Response sent April 29 — no reply yet."
        ),
        "status": "Active",
        "last_contact_date": date(2026, 4, 29),
        "next_action": "Follow up this week on Madhav India conversation",
        "next_action_date": date(2026, 5, 12),
        "thread": [
            {
                "date": date(2026, 4, 28),
                "entry_type": "call",
                "content": (
                    "Activated after long delay. Made 5 introductions: Jennifer Layke (ACEEE), "
                    "Lakshmi Rajagopalan, Anup Bandivadekar (Hewlett), Afeena Ashfaq (SED), Erika Myers (CharIN). "
                    "Also informed Madhav (WRI India CEO) — door open for India conversation."
                ),
            },
            {
                "date": date(2026, 4, 29),
                "entry_type": "sent",
                "content": "Response sent confirming India on table from July. No reply yet — follow up this week.",
            },
        ],
    },

    {
        "name": "Purnendu Chaubey",
        "title": "VP",
        "organization": "ReNew Power",
        "relationship_context": (
            "WhatsApp May 7. Call May 10 (Saturday). Candid debrief: "
            "Indian power companies have limited genuine strategy roles — mostly project execution. "
            "He will activate contacts, speak to Sumant Sinha (ReNew CEO), look at PE-backed platforms. "
            "Salary asked — responded 120-150L. Resume sent via WhatsApp."
        ),
        "status": "Warm",
        "last_contact_date": date(2026, 5, 10),
        "next_action": "Follow up May 24",
        "next_action_date": date(2026, 5, 24),
        "thread": [
            {
                "date": date(2026, 5, 10),
                "entry_type": "call",
                "content": (
                    "Candid debrief: Indian power companies have limited genuine strategy roles — "
                    "mostly project execution. He will activate contacts, speak to Sumant Sinha (ReNew CEO), "
                    "look at PE-backed platforms. Salary range shared: 120-150L. Resume sent via WhatsApp."
                ),
            }
        ],
    },

    {
        "name": "Amit Agarwal",
        "title": "Regulatory Affairs",
        "organization": "Reliance Infrastructure",
        "relationship_context": (
            "WhatsApp sent May 7. Replied — in DC, back in India next week. Will speak then."
        ),
        "status": "Active",
        "last_contact_date": date(2026, 5, 7),
        "next_action": "Follow up May 15 to schedule call",
        "next_action_date": date(2026, 5, 15),
        "thread": [
            {
                "date": date(2026, 5, 7),
                "entry_type": "whatsapp",
                "content": "WhatsApp sent. Replied — in DC, back in India next week. Will speak then.",
            }
        ],
    },

    {
        "name": "Dinesh Jagdale",
        "title": "Former Joint Secretary, MNRE",
        "organization": "Suzlon",
        "relationship_context": (
            "Call April 25 — confirmed strategy/public policy fit. "
            "Offered to share CV with executive chairman. CV sent same day. "
            "Reply warm but soft ('Thanks, wish you good luck'). Follow up May 12."
        ),
        "status": "Warm",
        "last_contact_date": date(2026, 4, 25),
        "next_action": "Follow up May 12 — ask if he had a chance to share CV",
        "next_action_date": date(2026, 5, 12),
        "thread": [
            {
                "date": date(2026, 4, 25),
                "entry_type": "call",
                "content": (
                    "Call confirmed strategy/public policy fit. Offered to share CV with executive chairman. "
                    "CV sent same day. Reply warm but soft ('Thanks, wish you good luck')."
                ),
            }
        ],
    },

    {
        "name": "Aayushi Agarwal",
        "organization": "PwC India",
        "relationship_context": (
            "College classmate. On WhatsApp. Met for work 3 years ago. At PwC for 2 years. "
            "Open position: Director C&I Energy at PwC India. WhatsApp sent May 11 — warm, direct ask."
        ),
        "status": "Active",
        "last_contact_date": date(2026, 5, 11),
        "next_action": "Await response — follow up in 3 days if no reply",
        "next_action_date": date(2026, 5, 14),
        "thread": [
            {
                "date": date(2026, 5, 11),
                "entry_type": "whatsapp",
                "content": (
                    "WhatsApp sent — warm, direct ask to put in a word for Director C&I Energy role at PwC India."
                ),
            }
        ],
    },

    {
        "name": "Manisha Jha",
        "organization": "Blueleaf Energy",
        "relationship_context": (
            "1st degree HKS MPA/ID alum. At Blueleaf Energy (PE-backed renewable platform). "
            "Open position: Associate Chief of Staff, Bengaluru. LinkedIn message sent May 11."
        ),
        "status": "Active",
        "last_contact_date": date(2026, 5, 11),
        "next_action": "Await response — follow up in 3 days if no reply",
        "next_action_date": date(2026, 5, 14),
        "thread": [
            {
                "date": date(2026, 5, 11),
                "entry_type": "linkedin",
                "content": "LinkedIn message sent re Associate Chief of Staff role at Blueleaf Energy, Bengaluru.",
            }
        ],
    },

    {
        "name": "Mohit Bhargava",
        "organization": "IECC",
        "relationship_context": (
            "Call April 24 — positive. Role: Associate Director, Industrial Policy & Decarbonisation. "
            "Delhi-based, philanthropy-funded. Salary 55-60L + 10% bonus (below floor). "
            "Transearch (Waiser/Poromita) running the search."
        ),
        "status": "Active",
        "last_contact_date": date(2026, 4, 24),
        "next_action": "Keep process open — below floor but worth continuing",
        "next_action_date": None,
        "thread": [
            {
                "date": date(2026, 4, 24),
                "entry_type": "call",
                "content": (
                    "Positive call. Role: Associate Director, Industrial Policy & Decarbonisation. "
                    "Delhi-based, philanthropy-funded. Salary: 55-60L + 10% bonus — below 120-150L floor. "
                    "Transearch (Poromita) running the search."
                ),
            }
        ],
    },

    {
        "name": "RB Balaji",
        "title": "IFC Green Hydrogen Lead",
        "organization": "IFC",
        "relationship_context": (
            "Connected via Jamie Ferguson. Key lesson from call April 24: "
            "be direct and confident from opening — state what you want, don't be defensive about gaps. "
            "Suggested targeting IO/Senior not AIO."
        ),
        "status": "Warm",
        "last_contact_date": date(2026, 4, 24),
        "next_action": "No immediate action needed — IFC application submitted",
        "next_action_date": None,
        "thread": [
            {
                "date": date(2026, 4, 24),
                "entry_type": "call",
                "content": (
                    "Call via Jamie Ferguson intro. Key lesson: be direct and confident from opening. "
                    "Schooled on confidence — state what you want. "
                    "Suggested targeting IO/Senior level not AIO at IFC."
                ),
            }
        ],
    },

    # ── Pending outreach ───────────────────────────────────────────────────────

    {
        "name": "Mahesh Naik",
        "organization": "World Bank",
        "title": "Strategy Office",
        "relationship_context": (
            "Spoke for an hour in August, never followed up. Delhi-based. Overdue outreach."
        ),
        "status": "Pending",
        "last_contact_date": None,
        "next_action": "Send outreach this week — overdue since August",
        "next_action_date": date(2026, 5, 12),
        "thread": [],
    },

    {
        "name": "Jas Singh",
        "organization": "World Bank",
        "relationship_context": "Recommended by RB Balaji — policy aspects. Not yet contacted.",
        "status": "Pending",
        "last_contact_date": None,
        "next_action": "Initial outreach (Balaji referral)",
        "next_action_date": date(2026, 5, 16),
        "thread": [],
    },

    {
        "name": "Jesse Jenkins",
        "title": "Professor",
        "organization": "Princeton University",
        "relationship_context": "Substack note not yet sent.",
        "status": "Pending",
        "last_contact_date": None,
        "next_action": "Send Substack note",
        "next_action_date": date(2026, 5, 16),
        "thread": [],
    },

    {
        "name": "Radhika Khosla",
        "organization": "Oxford OICSD",
        "relationship_context": "LinkedIn message not yet sent.",
        "status": "Pending",
        "last_contact_date": None,
        "next_action": "Send LinkedIn message",
        "next_action_date": date(2026, 5, 16),
        "thread": [],
    },

    {
        "name": "Ani Balabanyan",
        "title": "Manager, Energy Policy & Regulations, KIEPR",
        "organization": "World Bank",
        "relationship_context": (
            "Identified as hiring manager for KIEPR Senior Energy Specialist role (req35851). "
            "WB restructuring ongoing — no hiring clarity until June."
        ),
        "status": "Hold",
        "last_contact_date": None,
        "next_action": "Await WB restructuring clarity — revisit June",
        "next_action_date": date(2026, 6, 1),
        "thread": [],
    },
]


# ── Applications ──────────────────────────────────────────────────────────────

SEED_APPLICATIONS = [
    {
        "role": "Energy Investment Officer — KIESI",
        "organization": "IFC (World Bank Group)",
        "req_number": "req36322",
        "status": "Applied",
        "applied_date": None,
        "location": "Washington DC / Remote",
        "notes": (
            "Finance-forward resume used. RB Balaji (IFC green hydrogen lead) connected via Jamie Ferguson. "
            "Balaji call April 24 — suggested targeting IO/Senior not AIO. Status unclear. "
            "Resume version: IFC April 2026."
        ),
        "resume_version": "IFC April 2026",
        "lane": "Multilateral",
    },
    {
        "role": "Senior Energy Specialist — KIEPR",
        "organization": "World Bank",
        "req_number": "req35851",
        "status": "Applied",
        "applied_date": None,
        "location": "Washington DC",
        "notes": (
            "Ani Balabanyan identified as hiring manager. WB restructuring ongoing — "
            "no hiring clarity until June. Resume version: March 23 (policy/multilateral)."
        ),
        "resume_version": "March 23",
        "lane": "Multilateral",
    },
    {
        "role": "Policy and Regulatory Expert (P3)",
        "organization": "ISA (International Solar Alliance)",
        "status": "Applied",
        "applied_date": date(2026, 5, 5),
        "location": "Delhi / Gurgaon",
        "notes": (
            "Submitted May 5. Cover letter tailored around ISA presidency role at MNRE. "
            "Awaiting response."
        ),
        "resume_version": "March 23",
        "lane": "Multilateral",
    },
    {
        "role": "Programme Director — Ammonia & Industrial Decarbonisation",
        "organization": "Systemiq",
        "status": "Applied",
        "applied_date": date(2026, 5, 11),
        "location": "Delhi",
        "notes": (
            "Submitted May 11. Resume and cover letter tailored. Expected comp: ~80 LPA. "
            "Strong fit — ammonia/fertiliser work is direct match."
        ),
        "resume_version": "Systemiq May 11",
        "lane": "India Private",
    },
    {
        "role": "Energy Specialist",
        "organization": "ADB (Asian Development Bank)",
        "status": "Applied",
        "applied_date": None,
        "location": "Delhi",
        "notes": "Applied. Direct outreach also initiated. Resume version: ADB April 2026.",
        "resume_version": "ADB April 2026",
        "lane": "Multilateral",
    },
    {
        "role": "Adviser & Head, Energy & Natural Resources",
        "organization": "Commonwealth Secretariat",
        "status": "Drafting",
        "location": "London",
        "notes": (
            "London-based. Good fit on work — natural resources gap and visa situation need clarification. "
            "Decision pending on whether to submit."
        ),
        "lane": "Multilateral",
    },
    {
        "role": "Associate Director — Industrial Policy & Decarbonisation",
        "organization": "IECC",
        "status": "Under Review",
        "location": "Delhi",
        "notes": (
            "Mohit Bhargava (IECC) call April 24 — positive. "
            "Poromita (Transearch) running the search. "
            "Salary: 55-60L + 10% bonus — below 120-150L floor. Process ongoing, keep open."
        ),
        "lane": "India Private",
    },
    {
        "role": "India Chair",
        "organization": "CSIS",
        "status": "Withdrawn",
        "applied_date": None,
        "location": "Washington DC",
        "notes": "Gracefully closed April 22 after two calls with Rossow. Fellow/bridge option didn't materialise.",
        "lane": "Think Tank",
    },
    {
        "role": "Multiple Roles",
        "organization": "Google",
        "status": "Rejected",
        "applied_date": None,
        "location": "Remote / US",
        "notes": "Rejected at GHA stage. Closed for 6 months.",
        "lane": "US Private",
    },
    {
        "role": "Data Centers & Large Load Integration",
        "organization": "RAP (Regulatory Assistance Project)",
        "status": "Withdrawn",
        "applied_date": None,
        "location": "Remote / US",
        "notes": "Closed May 8 — compensation $75-100K, below $150K floor. Did not submit.",
        "lane": "Think Tank",
    },
]


# ── Tasks ─────────────────────────────────────────────────────────────────────

SEED_TASKS = [

    # Due today / urgent
    {
        "title": "Lena Diaz (ICF) — respond immediately when email arrives",
        "category": "Career",
        "priority": "High",
        "time_estimate": "30 min",
        "due_date": date(2026, 5, 12),
        "linked_contact": "Lena Diaz",
        "notes": "Most active US lead. Check email repeatedly. Respond same day.",
    },
    {
        "title": "Dinesh Jagdale (Suzlon) — follow-up: did he share CV with exec chairman?",
        "category": "Career",
        "priority": "High",
        "time_estimate": "10 min",
        "due_date": date(2026, 5, 12),
        "linked_contact": "Dinesh Jagdale",
    },
    {
        "title": "Anup Bandivadekar (Hewlett Foundation) — schedule call",
        "category": "Career",
        "priority": "High",
        "time_estimate": "10 min",
        "due_date": date(2026, 5, 12),
        "linked_contact": "Anup Bandivadekar",
    },
    {
        "title": "Pawan Mulukutla (WRI India) — follow up on Madhav India conversation",
        "category": "Career",
        "priority": "High",
        "time_estimate": "15 min",
        "due_date": date(2026, 5, 12),
        "linked_contact": "Pawan Mulukutla",
    },
    {
        "title": "Mahesh Naik (World Bank) — send overdue outreach",
        "category": "Career",
        "priority": "High",
        "time_estimate": "20 min",
        "due_date": date(2026, 5, 12),
        "linked_contact": "Mahesh Naik",
        "notes": "Spoke an hour in August, never followed up. Delhi-based. Overdue.",
    },

    # May 15
    {
        "title": "Hy Martin (DESRI India) — prep and call May 15",
        "category": "Career",
        "priority": "High",
        "time_estimate": "1.5 hr",
        "due_date": date(2026, 5, 15),
        "linked_contact": "Hy Martin",
        "notes": "Research DESRI India operations before call.",
    },
    {
        "title": "Amit Agarwal (Reliance Infra) — follow up to schedule call",
        "category": "Career",
        "priority": "Medium",
        "time_estimate": "10 min",
        "due_date": date(2026, 5, 15),
        "linked_contact": "Amit Agarwal",
    },

    # This week
    {
        "title": "Aayushi Agarwal (PwC India) — follow up if no reply",
        "category": "Career",
        "priority": "Medium",
        "time_estimate": "10 min",
        "due_date": date(2026, 5, 14),
        "linked_contact": "Aayushi Agarwal",
    },
    {
        "title": "Manisha Jha (Blueleaf Energy) — follow up if no reply",
        "category": "Career",
        "priority": "Medium",
        "time_estimate": "10 min",
        "due_date": date(2026, 5, 14),
        "linked_contact": "Manisha Jha",
    },
    {
        "title": "Jas Singh (World Bank) — initial outreach (Balaji referral)",
        "category": "Career",
        "priority": "Medium",
        "time_estimate": "15 min",
        "due_date": date(2026, 5, 16),
        "linked_contact": "Jas Singh",
    },
    {
        "title": "Jesse Jenkins (Princeton) — send Substack note",
        "category": "Career",
        "priority": "Medium",
        "time_estimate": "20 min",
        "due_date": date(2026, 5, 16),
        "linked_contact": "Jesse Jenkins",
    },
    {
        "title": "Radhika Khosla (Oxford OICSD) — send LinkedIn message",
        "category": "Career",
        "priority": "Medium",
        "time_estimate": "15 min",
        "due_date": date(2026, 5, 16),
        "linked_contact": "Radhika Khosla",
    },

    # Commonwealth Secretariat decision
    {
        "title": "Commonwealth Secretariat — decide whether to submit application",
        "category": "Career",
        "priority": "High",
        "time_estimate": "30 min",
        "due_date": date(2026, 5, 16),
        "notes": "London-based. Good fit on work — clarify visa situation and natural resources gap first.",
    },

    # May 24
    {
        "title": "Purnendu Chaubey (ReNew Power) — follow up",
        "category": "Career",
        "priority": "Medium",
        "time_estimate": "10 min",
        "due_date": date(2026, 5, 24),
        "linked_contact": "Purnendu Chaubey",
        "notes": "He will speak to Sumant Sinha (ReNew CEO) and look at PE-backed platforms.",
    },

    # Ongoing / no fixed date
    {
        "title": "GLG / AlphaSights / Guidepoint — register for expert networks",
        "category": "Career",
        "priority": "Medium",
        "time_estimate": "1 hr",
        "due_date": None,
        "notes": "Passive income option. Registration status unclear. Action needed.",
    },
    {
        "title": "GIZ India — initial outreach (India-Germany Task Force connection)",
        "category": "Career",
        "priority": "Medium",
        "time_estimate": "20 min",
        "due_date": None,
    },
    {
        "title": "CEEW — identify contact and initiate outreach",
        "category": "Career",
        "priority": "Low",
        "time_estimate": "30 min",
        "due_date": None,
        "notes": "No direct contact identified yet.",
    },
    {
        "title": "Middle East track — activate: EY-Parthenon Dubai, Deloitte ME, Strategy& Gulf, IRENA, Masdar",
        "category": "Career",
        "priority": "Medium",
        "time_estimate": "2 hr",
        "due_date": None,
        "notes": "Identified but not yet activated. Third parallel track.",
    },
]


# ── CV Bullets ────────────────────────────────────────────────────────────────

CV_BULLETS = [
    # Harvard Belfer Center
    {
        "employer": "Harvard Belfer Center",
        "period": "2025–2026",
        "bullet_text": "Authored research on clean energy transition financing mechanisms for emerging markets, cited in policy dialogues at COP30 preparatory sessions.",
        "tags": "research, clean energy, financing, emerging markets, policy",
    },
    {
        "employer": "Harvard Belfer Center",
        "period": "2025–2026",
        "bullet_text": "Modelled green hydrogen demand scenarios across 15 countries using LCOH projections and electrolyser cost curves; findings informed ISA policy brief.",
        "tags": "green hydrogen, modelling, ISA, energy policy, quantitative",
    },

    # MNRE — National Green Hydrogen Mission
    {
        "employer": "Ministry of New and Renewable Energy (MNRE), Government of India",
        "period": "2018–2024",
        "bullet_text": "Led design and launch of India's National Green Hydrogen Mission (₹19,744 Cr); oversaw SIGHT incentive programme for electrolyser manufacturing and green hydrogen production.",
        "tags": "green hydrogen, policy design, government, MNRE, electrolysers",
    },
    {
        "employer": "Ministry of New and Renewable Energy (MNRE), Government of India",
        "period": "2018–2024",
        "bullet_text": "Negotiated bilateral MoUs on clean energy with 12 countries; represented India at ISA, IRENA, and G20 energy working groups.",
        "tags": "diplomacy, bilateral, IRENA, G20, international energy, ISA",
    },
    {
        "employer": "Ministry of New and Renewable Energy (MNRE), Government of India",
        "period": "2018–2024",
        "bullet_text": "Built cross-ministry task force (MNRE, MoP, MoF) to align fiscal incentives for RE manufacturing under PLI scheme; secured ₹4,500 Cr allocation.",
        "tags": "PLI, fiscal policy, manufacturing, cross-government, RE",
    },
    {
        "employer": "Ministry of New and Renewable Energy (MNRE), Government of India",
        "period": "2018–2024",
        "bullet_text": "Oversaw 8 GW solar park development pipeline across 6 states; resolved land acquisition, grid connectivity, and PPA renegotiation disputes.",
        "tags": "solar, infrastructure, PPA, land acquisition, grid",
    },
    {
        "employer": "Ministry of New and Renewable Energy (MNRE), Government of India",
        "period": "2018–2024",
        "bullet_text": "Drafted India's Nationally Determined Contribution (NDC) energy sector targets (500 GW RE by 2030); coordinated with NITI Aayog and MoEFCC.",
        "tags": "NDC, climate policy, 500GW, NITI Aayog, net zero",
    },

    # World Bank ESMAP
    {
        "employer": "World Bank ESMAP",
        "period": "2024–2025",
        "bullet_text": "Designed $45M technical assistance programme for South Asia clean cooking transition; conducted political economy analysis across Bangladesh, Nepal, India.",
        "tags": "clean cooking, South Asia, World Bank, technical assistance, political economy",
    },
    {
        "employer": "World Bank ESMAP",
        "period": "2024–2025",
        "bullet_text": "Led sector assessment for off-grid solar in Sub-Saharan Africa; benchmarked 8 regulatory frameworks and identified $2B blended finance opportunity.",
        "tags": "off-grid solar, Africa, blended finance, regulatory, World Bank",
    },
    {
        "employer": "World Bank ESMAP",
        "period": "2024–2025",
        "bullet_text": "Produced flagship ESMAP report on green hydrogen readiness in developing economies; presented to WB board and 40+ government delegations.",
        "tags": "green hydrogen, ESMAP, report, developing economies, presentations",
    },

    # WRI India
    {
        "employer": "WRI India",
        "period": "2016–2018",
        "bullet_text": "Led Cities Clean Energy programme: partnered with 12 municipal corporations on distributed solar and EV charging infrastructure planning.",
        "tags": "cities, solar, EV, municipal, WRI, clean energy",
    },
    {
        "employer": "WRI India",
        "period": "2016–2018",
        "bullet_text": "Managed $3.2M ClimateWorks-funded research portfolio; delivered 6 policy briefs adopted by state energy departments in Gujarat and Maharashtra.",
        "tags": "climate finance, research management, state policy, Gujarat, Maharashtra",
    },

    # Reliance Industries
    {
        "employer": "Reliance Industries",
        "period": "2012–2016",
        "bullet_text": "Structured $180M upstream gas field asset sale; managed due diligence, regulatory approvals, and SPA negotiation with international buyer.",
        "tags": "M&A, gas, upstream, transaction, regulatory, private sector",
    },
    {
        "employer": "Reliance Industries",
        "period": "2012–2016",
        "bullet_text": "Built financial model for 400 MW gas-to-power project; scenario analysis across 5 fuel price and tariff regimes; presented to board.",
        "tags": "financial modelling, gas-to-power, tariff, board presentation, private sector",
    },

    # Welspun Energy
    {
        "employer": "Welspun Energy",
        "period": "2009–2012",
        "bullet_text": "Led PPA negotiations for 200 MW solar portfolio across Rajasthan, Gujarat, and MP; achieved 12% above-market tariff on 3 projects.",
        "tags": "PPA, solar, tariff negotiation, Rajasthan, Gujarat, commercial",
    },
    {
        "employer": "Welspun Energy",
        "period": "2009–2012",
        "bullet_text": "Managed EPC contractor selection and contract execution for 75 MW wind project in Tamil Nadu; delivered on time and 8% under budget.",
        "tags": "EPC, wind, project management, Tamil Nadu, construction",
    },
]
