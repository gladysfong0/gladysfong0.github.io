"""
Portfolio Generator — Gladys Nicolle Fong (v3)
================================================
HOW TO USE:
1. Add your photos to the "my portfolio" folder:
     gladys_photo.jpg        <- your headshot
     project_wmata.jpg       <- WMATA project photo
     project_iot.jpg         <- IoT plant project photo
     project_fema.jpg        <- FEMA tool photo
     project_scooter.jpg     <- scooter project photo
     project_bird.jpg        <- mechanical bird photo
2. Run:  python generate_portfolio.py
3. Push everything to GitHub!
"""

PROFILE = {
    "name": "Gladys Nicolle Fong",
    "title": "Systems Engineer & Data Scientist",
    "tagline": "Engineering Management & Systems Engineering",
    "about": (
        "I'm a first-generation engineer from West Covina, California — and honestly, "
        "I wouldn't have it any other way. Growing up, I was always the person asking "
        "'but why does this system work like that?' Turns out, that's basically a "
        "Systems Engineering degree waiting to happen. "
        "I'm finishing my B.S. in Engineering Management & Systems Engineering at The "
        "George Washington University (minor in Data Analytics for Decisions) and I've "
        "spent the last two years redesigning transit safety data infrastructure for WMATA, "
        "building IoT plant monitors, and mapping disaster vulnerability for FEMA — "
        "all with the goal of making systems that actually work for people who need them most. "
        "I'm bilingual in English and Spanish, an IEEE published author, and a Thrive Scholar. "
        "When I'm not deep in a SysML diagram or debugging a Python model at midnight, "
        "I'm probably tutoring students or figuring out how to make something more equitable. "
        "Big on impact. Bigger on making sure the right communities feel it."
    ),
    "email": "gladysfong0@gmail.com",
    "linkedin": "https://www.linkedin.com/in/gladys-fong-3b330b28a/",
    "github": "https://github.com/gladysfong0",
    "resume_file": "Gladys_Fong_Resume.pdf",
}

PHOTO_FILE = "gladys_photo.jpg"

TYPING_WORDS = [
    "Systems Engineer",
    "Data Architect",
    "MBSE Practitioner",
    "IoT Engineer",
    "Geospatial Analyst",
    "Predictive Modeler",
    "Requirements Engineer",
    "First-Gen Engineer",
]

AWARDS = [
    {
        "title": "Best Paper Winner",
        "body": "Andrew P. Sage Memorial Capstone Competition (2026) — WMATA Safety Data Architecture & Forecasting",
    },
    {
        "title": "IEEE Published Author",
        "body": "Published research on transit safety data architecture",
    },
    {
        "title": "Honorable Mention",
        "body": "SIEDS UVA Systems Engineering Competition",
    },
]

SKILLS = [
    "Systems Architecture", "MBSE / SysML", "Requirements Engineering",
    "Fault Tree Analysis", "Capella", "Python (Pandas, NumPy, Scikit-learn, Matplotlib)",
    "MATLAB", "SQL", "Control Systems", "SOLIDWORKS / AutoCAD",
    "Raspberry Pi 4", "GIS / Geospatial Mapping", "Tableau", "Excel",
    "OpenAI API", "Machine Learning", "Predictive Modeling",
    "Data Architecture", "AI Agent Development", "Agile / Scrum",
    "Risk Analysis", "Stakeholder Engagement",
]

PROJECTS = [
    {
        "title": "WMATA Safety Data Architecture & Forecasting",
        "tags": ["Python", "Nonlinear Regression", "Data Architecture", "GIS", "MBSE"],
        "description": (
            "Capstone fellowship with GWU x WMATA. Redesigned WMATA's siloed safety data "
            "into a centralized logical data architecture for cross-departmental incident "
            "analysis. Built a Python forecasting tool modeling seasonality and location-based "
            "incident patterns for predictive maintenance planning."
        ),
        "badge": "Best Paper — Sage Capstone 2026",
        "photo": "project_wmata.jpg",
        "github_link": "",
        "demo_link": "",
    },
    {
        "title": "IoT Plant Health Monitoring System",
        "tags": ["Raspberry Pi 4", "Machine Learning", "SysML", "Capella", "Python"],
        "description": (
            "Designed and deployed an embedded smart monitoring system with 4 environmental "
            "sensors, Raspberry Pi 4, and automated pump control. Developed an ML-based plant "
            "health classification model and real-time monitoring dashboard."
        ),
        "badge": "",
        "photo": "project_iot.jpg",
        "github_link": "",
        "demo_link": "",
    },
    {
        "title": "FEMA Equitable Disaster Resource Allocation Tool",
        "tags": ["Python", "GIS", "Vulnerability Index", "Data Analytics"],
        "description": (
            "Built a Python tool normalizing socioeconomic, geographic, and infrastructure "
            "indicators into a Vulnerability Index to identify Houston-area communities most "
            "at risk of inadequate disaster response. Produced geospatial heat maps and "
            "presented recommendations to FEMA Response leadership."
        ),
        "badge": "",
        "photo": "project_fema.jpg",
        "github_link": "",
        "demo_link": "",
    },
    {
        "title": "E-Scooter Infrastructure Requirements Analysis",
        "tags": ["GIS", "Python", "Requirements Engineering", "Urban Mobility"],
        "description": (
            "Conducted full requirements analysis for ADA-compliant e-scooter docking "
            "infrastructure in Foggy Bottom, DC. Built GIS heat maps visualizing ridership "
            "demand and accessibility gaps; translated stakeholder-driven requirements into "
            "infrastructure specifications."
        ),
        "badge": "",
        "photo": "project_scooter.jpg",
        "github_link": "",
        "demo_link": "",
    },
    {
        "title": "Mechanical Bird — Systems Design & Fabrication",
        "tags": ["SOLIDWORKS", "AutoCAD", "SysML", "Machining"],
        "description": (
            "Designed and manufactured a mechanical bird with flapping wings and 360-degree "
            "head rotation using SOLIDWORKS, AutoCAD, and machining tools. Applied SysML "
            "decomposition and iterative design verification throughout fabrication."
        ),
        "badge": "",
        "photo": "project_bird.jpg",
        "github_link": "",
        "demo_link": "",
    },
]

# ============================================================
#  COLORS — dusty rose + cream + slate, pops of magenta/lilac
# ============================================================
ROSE      = "#C9748A"
LILAC     = "#9B7FBD"
BLUSH     = "#E8B4C0"
TEAL      = "#5BBFB5"
GOLD      = "#C9A84C"
BG_DARK   = "#0F0D11"
BG_CARD   = "#18141C"
BG_CARD2  = "#201B26"
TEXT_MAIN  = "#F2EEF5"
TEXT_MUTED = "#8A7F94"

def tag_pill(tag):
    palette = [
        (ROSE,  "#2e1219"),
        (LILAC, "#1e1428"),
        (TEAL,  "#0d2826"),
    ]
    color, bg = palette[hash(tag) % len(palette)]
    return (
        f'<span style="background:{bg};color:{color};border:1px solid {color}66;'
        f'padding:3px 11px;border-radius:20px;font-size:11px;font-weight:600;'
        f'letter-spacing:0.3px;">{tag}</span>'
    )

def project_card(p):
    tags_html = " ".join(tag_pill(t) for t in p["tags"])
    links = ""
    if p["github_link"]:
        links += f'<a href="{p["github_link"]}" target="_blank" class="btn-link">GitHub</a>'
    if p["demo_link"]:
        links += f'<a href="{p["demo_link"]}" target="_blank" class="btn-link btn-demo">Live Demo</a>'
    badge_html = f'<div class="card-badge">{p["badge"]}</div>' if p["badge"] else ""
    photo_html = f"""
      <div class="card-photo-wrap">
        <img src="{p['photo']}" alt="{p['title']}" class="card-photo"
             onerror="this.parentElement.classList.add('no-photo')">
        <div class="card-photo-placeholder">No photo yet — add {p['photo']}</div>
      </div>"""
    return f"""
    <div class="card reveal">
      {photo_html}
      <div class="card-body">
        {badge_html}
        <h3>{p["title"]}</h3>
        <div class="tags">{tags_html}</div>
        <p class="desc">{p["description"]}</p>
        <div class="card-links">{links}</div>
      </div>
    </div>"""

def award_card(a):
    return f"""
    <div class="award-card reveal">
      <div class="award-accent"></div>
      <div>
        <div class="award-title">{a["title"]}</div>
        <div class="award-body">{a["body"]}</div>
      </div>
    </div>"""

def skill_chip(s):
    return f'<span class="skill-chip">{s}</span>'

def build_html():
    projects_html = "\n".join(project_card(p) for p in PROJECTS)
    skills_html   = "\n".join(skill_chip(s) for s in SKILLS)
    awards_html   = "\n".join(award_card(a) for a in AWARDS)
    typing_words_js = str(TYPING_WORDS).replace("'", '"')

    resume_btn = ""
    if PROFILE["resume_file"]:
        resume_btn = f'<a href="{PROFILE["resume_file"]}" download class="cta-btn secondary-btn">Download Resume</a>'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>{PROFILE["name"]} — Systems Engineer</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      background: {BG_DARK};
      color: {TEXT_MAIN};
      font-family: 'Inter', sans-serif;
      line-height: 1.6;
      overflow-x: hidden;
    }}

    /* ── NOISE TEXTURE OVERLAY ── */
    body::before {{
      content: '';
      position: fixed; inset: 0; z-index: 0; pointer-events: none;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
      opacity: 0.4;
    }}

    /* ── ANIMATED BLOBS ── */
    .blob-wrap {{
      position: fixed; inset: 0; z-index: 0; pointer-events: none; overflow: hidden;
    }}
    .blob {{
      position: absolute; border-radius: 50%;
      filter: blur(80px); opacity: 0.12;
      animation: blobFloat 18s ease-in-out infinite;
    }}
    .blob-1 {{
      width: 500px; height: 500px;
      background: {ROSE}; top: -100px; left: -100px;
      animation-delay: 0s;
    }}
    .blob-2 {{
      width: 400px; height: 400px;
      background: {LILAC}; bottom: 10%; right: -80px;
      animation-delay: -6s;
    }}
    .blob-3 {{
      width: 300px; height: 300px;
      background: {TEAL}; top: 50%; left: 40%;
      animation-delay: -12s;
    }}
    @keyframes blobFloat {{
      0%, 100% {{ transform: translate(0,0) scale(1); }}
      33%       {{ transform: translate(30px,-40px) scale(1.05); }}
      66%       {{ transform: translate(-20px, 20px) scale(0.96); }}
    }}

    /* ── SCROLL REVEAL ── */
    .reveal {{
      opacity: 0; transform: translateY(32px);
      transition: opacity 0.75s ease, transform 0.75s ease;
    }}
    .reveal.visible {{ opacity: 1; transform: translateY(0); }}
    .reveal-left {{
      opacity: 0; transform: translateX(-40px);
      transition: opacity 0.75s ease, transform 0.75s ease;
    }}
    .reveal-left.visible {{ opacity: 1; transform: translateX(0); }}
    .reveal-right {{
      opacity: 0; transform: translateX(40px);
      transition: opacity 0.75s ease, transform 0.75s ease;
    }}
    .reveal-right.visible {{ opacity: 1; transform: translateX(0); }}

    /* ── NAV ── */
    nav {{
      position: sticky; top: 0; z-index: 200;
      display: flex; justify-content: space-between; align-items: center;
      padding: 1.1rem 2.5rem;
      background: {BG_DARK}cc;
      backdrop-filter: blur(16px);
      border-bottom: 1px solid {ROSE}22;
      transition: box-shadow 0.3s;
    }}
    nav.scrolled {{ box-shadow: 0 2px 30px #00000055; }}
    .nav-logo {{
      font-family: 'Playfair Display', serif;
      font-weight: 700; font-size: 1.15rem;
      background: linear-gradient(90deg, {ROSE}, {LILAC});
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      letter-spacing: 0.5px;
    }}
    .nav-links a {{
      color: {TEXT_MUTED}; text-decoration: none;
      margin-left: 2rem; font-size: 0.88rem; font-weight: 500;
      transition: color 0.2s; letter-spacing: 0.3px;
    }}
    .nav-links a:hover {{ color: {ROSE}; }}

    /* ── HERO ── */
    .hero-wrap {{
      position: relative; min-height: 94vh;
      display: flex; align-items: center;
    }}
    .hero {{
      position: relative; z-index: 1;
      max-width: 900px; margin: 0 auto;
      padding: 6rem 2.5rem 4rem;
    }}
    .hero-eyebrow {{
      font-size: 0.75rem; font-weight: 600; letter-spacing: 5px;
      text-transform: uppercase; color: {TEAL};
      margin-bottom: 1.4rem;
      animation: fadeUp 0.8s ease both;
    }}
    .hero h1 {{
      font-family: 'Playfair Display', serif;
      font-size: clamp(3rem, 7.5vw, 5.5rem);
      font-weight: 800; line-height: 1.08; margin-bottom: 1rem;
      animation: fadeUp 0.9s ease 0.1s both;
    }}
    .hero-typing-line {{
      display: flex; align-items: center; gap: 0.5rem;
      margin-bottom: 1.6rem;
      animation: fadeUp 1s ease 0.2s both;
    }}
    .typing-label {{
      font-size: 1.1rem; color: {TEXT_MUTED}; font-weight: 300;
    }}
    .typing-text {{
      font-size: 1.1rem; font-weight: 600;
      background: linear-gradient(90deg, {ROSE}, {LILAC});
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      min-width: 180px;
    }}
    .cursor {{
      display: inline-block; width: 2px; height: 1.1em;
      background: {ROSE}; margin-left: 2px; vertical-align: middle;
      animation: blink 1s step-end infinite;
    }}
    @keyframes blink {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    .hero-sub {{
      font-size: 1rem; color: {TEXT_MUTED}; max-width: 560px;
      margin-bottom: 2.8rem; line-height: 1.8; font-weight: 300;
      animation: fadeUp 1s ease 0.3s both;
    }}
    .hero-actions {{
      display: flex; gap: 1rem; flex-wrap: wrap;
      animation: fadeUp 1s ease 0.4s both;
    }}
    @keyframes fadeUp {{
      from {{ opacity: 0; transform: translateY(24px); }}
      to   {{ opacity: 1; transform: translateY(0); }}
    }}

    /* ── DECORATIVE LINE ── */
    .deco-line {{
      display: inline-block; width: 48px; height: 2px;
      background: linear-gradient(90deg, {ROSE}, {LILAC});
      margin-bottom: 1rem; border-radius: 2px;
    }}

    /* ── BUTTONS ── */
    .cta-btn {{
      padding: 0.8rem 2rem; border-radius: 50px;
      font-weight: 600; font-size: 0.9rem;
      text-decoration: none; display: inline-block;
      transition: all 0.25s; letter-spacing: 0.3px;
    }}
    .primary-btn {{
      background: linear-gradient(135deg, {ROSE}, {LILAC});
      color: #fff;
      box-shadow: 0 4px 20px {ROSE}44;
    }}
    .primary-btn:hover {{ transform: translateY(-3px); box-shadow: 0 8px 28px {ROSE}66; }}
    .secondary-btn {{
      background: transparent;
      border: 1.5px solid {LILAC}88; color: {LILAC};
    }}
    .secondary-btn:hover {{ background: {LILAC}18; transform: translateY(-3px); }}

    /* ── SECTIONS ── */
    section {{ position: relative; z-index: 1; max-width: 1080px; margin: 0 auto; padding: 6rem 2.5rem; }}
    .section-label {{
      font-size: 0.7rem; font-weight: 700; letter-spacing: 5px;
      text-transform: uppercase; color: {ROSE}; margin-bottom: 0.4rem;
    }}
    .section-title {{
      font-family: 'Playfair Display', serif;
      font-size: clamp(1.9rem, 4vw, 2.6rem);
      font-weight: 700; margin-bottom: 3rem; line-height: 1.2;
    }}
    .divider {{
      border: none; position: relative; z-index: 1;
      border-top: 1px solid {ROSE}18; margin: 0 2rem;
    }}

    /* ── AWARDS ── */
    .awards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1.2rem;
    }}
    .award-card {{
      background: {BG_CARD}; border: 1px solid {GOLD}22;
      border-radius: 14px; padding: 1.4rem 1.6rem;
      display: flex; align-items: flex-start; gap: 1rem;
      transition: transform 0.25s, box-shadow 0.25s;
    }}
    .award-card:hover {{ transform: translateY(-4px); box-shadow: 0 8px 30px #00000044; }}
    .award-accent {{
      width: 3px; min-height: 40px; border-radius: 3px;
      background: linear-gradient(180deg, {GOLD}, {ROSE});
      flex-shrink: 0; margin-top: 2px;
    }}
    .award-title {{ font-weight: 700; font-size: 0.92rem; margin-bottom: 0.3rem; color: {TEXT_MAIN}; }}
    .award-body {{ color: {TEXT_MUTED}; font-size: 0.83rem; line-height: 1.5; }}

    /* ── PROJECT CARDS ── */
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 1.6rem;
    }}
    .card {{
      background: {BG_CARD}; border: 1px solid {ROSE}18;
      border-radius: 18px; overflow: hidden;
      transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
      display: flex; flex-direction: column;
    }}
    .card:hover {{
      transform: translateY(-7px);
      box-shadow: 0 16px 48px #00000055;
      border-color: {ROSE}55;
    }}
    .card-photo-wrap {{
      width: 100%; height: 190px;
      overflow: hidden; position: relative;
      background: {BG_CARD2};
    }}
    .card-photo-wrap.no-photo .card-photo {{ display: none; }}
    .card-photo-wrap.no-photo .card-photo-placeholder {{ display: flex; }}
    .card-photo {{
      width: 100%; height: 100%; object-fit: cover;
      transition: transform 0.4s ease;
    }}
    .card:hover .card-photo {{ transform: scale(1.04); }}
    .card-photo-placeholder {{
      display: none; position: absolute; inset: 0;
      align-items: center; justify-content: center;
      flex-direction: column; gap: 0.5rem;
      color: {TEXT_MUTED}; font-size: 0.78rem; text-align: center;
      padding: 1rem;
      background: linear-gradient(135deg, {BG_CARD2}, {BG_DARK});
    }}
    .card-photo-placeholder::before {{
      content: 'Add photo';
      font-size: 1.8rem; display: block;
    }}
    .card-body {{ padding: 1.6rem; display: flex; flex-direction: column; flex: 1; }}
    .card-badge {{
      display: inline-block;
      background: {GOLD}15; border: 1px solid {GOLD}44;
      color: {GOLD}; font-size: 0.72rem; font-weight: 700;
      padding: 3px 11px; border-radius: 20px;
      margin-bottom: 0.8rem; width: fit-content;
      letter-spacing: 0.3px;
    }}
    .card h3 {{
      font-size: 1.02rem; font-weight: 700;
      margin-bottom: 0.75rem; line-height: 1.35;
    }}
    .tags {{ display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 0.9rem; }}
    .desc {{
      color: {TEXT_MUTED}; font-size: 0.86rem;
      flex: 1; margin-bottom: 1.1rem; line-height: 1.7;
    }}
    .card-links {{ display: flex; gap: 0.7rem; flex-wrap: wrap; margin-top: auto; }}
    .btn-link {{
      font-size: 0.8rem; font-weight: 600; color: {ROSE};
      text-decoration: none; border: 1px solid {ROSE}44;
      padding: 4px 14px; border-radius: 20px; transition: background 0.2s;
    }}
    .btn-link:hover {{ background: {ROSE}18; }}
    .btn-demo {{ color: {TEAL}; border-color: {TEAL}44; }}
    .btn-demo:hover {{ background: {TEAL}18; }}

    /* ── SKILLS ── */
    .skills-wrap {{ display: flex; flex-wrap: wrap; gap: 0.6rem; }}
    .skill-chip {{
      background: {BG_CARD}; border: 1px solid {LILAC}22;
      color: {TEXT_MUTED}; padding: 6px 16px;
      border-radius: 50px; font-size: 0.83rem; font-weight: 500;
      transition: all 0.2s; cursor: default;
    }}
    .skill-chip:hover {{ border-color: {ROSE}77; color: {ROSE}; background: {ROSE}0d; }}

    /* ── ABOUT ── */
    .about-layout {{
      display: grid; grid-template-columns: 260px 1fr;
      gap: 3.5rem; align-items: start;
    }}
    .about-photo-wrap {{ position: relative; }}
    .about-photo-frame {{
      position: relative; border-radius: 20px; overflow: hidden;
      aspect-ratio: 3/4;
    }}
    .about-photo-frame::after {{
      content: '';
      position: absolute; inset: 0;
      border-radius: 20px;
      border: 1.5px solid {ROSE}44;
      pointer-events: none;
    }}
    .about-photo {{
      width: 100%; height: 100%; object-fit: cover; display: block;
      transition: transform 0.4s;
    }}
    .about-photo:hover {{ transform: scale(1.03); }}
    .about-photo-placeholder {{
      width: 100%; aspect-ratio: 3/4;
      border-radius: 20px;
      border: 1.5px dashed {LILAC}44;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      gap: 0.6rem; text-align: center; padding: 1.5rem;
      color: {TEXT_MUTED}; font-size: 0.82rem;
      background: {BG_CARD};
    }}
    .glow-ring {{
      position: absolute; inset: -8px; border-radius: 28px; z-index: -1;
      background: linear-gradient(135deg, {ROSE}33, {LILAC}33, {TEAL}22);
      filter: blur(16px);
    }}
    .about-text .about-box {{
      background: {BG_CARD}; border: 1px solid {ROSE}18;
      border-left: 3px solid {ROSE};
      border-radius: 0 16px 16px 0;
      padding: 1.8rem 2rem;
      font-size: 0.97rem; color: #c4bccb; line-height: 1.9;
      margin-bottom: 1.8rem;
    }}

    /* ── FOOTER ── */
    footer {{
      position: relative; z-index: 1;
      text-align: center; padding: 2.5rem;
      color: {TEXT_MUTED}; font-size: 0.8rem;
      border-top: 1px solid {ROSE}18;
    }}
    footer a {{ color: {ROSE}; text-decoration: none; }}
    footer a:hover {{ color: {BLUSH}; }}

    @media (max-width: 720px) {{
      .about-layout {{ grid-template-columns: 1fr; }}
      .about-photo-wrap {{ max-width: 200px; margin: 0 auto; }}
      nav {{ padding: 1rem 1.2rem; }}
      .nav-links a {{ margin-left: 1rem; font-size: 0.8rem; }}
      .hero {{ padding: 4rem 1.2rem 2.5rem; }}
      section {{ padding: 4rem 1.2rem; }}
    }}
  </style>
</head>
<body>

<div class="blob-wrap">
  <div class="blob blob-1"></div>
  <div class="blob blob-2"></div>
  <div class="blob blob-3"></div>
</div>

<nav id="navbar">
  <span class="nav-logo">Gladys Fong</span>
  <div class="nav-links">
    <a href="#awards">Awards</a>
    <a href="#projects">Projects</a>
    <a href="#skills">Skills</a>
    <a href="#about">About</a>
    <a href="mailto:{PROFILE["email"]}">Contact</a>
  </div>
</nav>

<!-- HERO -->
<div class="hero-wrap">
  <div class="hero">
    <p class="hero-eyebrow">GWU · Engineering Management & Systems Engineering · Class of 2026</p>
    <h1>Gladys Nicolle<br>Fong</h1>
    <div class="hero-typing-line">
      <span class="typing-label">I am a</span>
      <span class="typing-text" id="typing-target"></span><span class="cursor"></span>
    </div>
    <p class="hero-sub">
      Designing resilient, data-driven systems at the intersection of hardware,
      software, and people — with an eye toward equity and real-world impact.
    </p>
    <div class="hero-actions">
      <a href="#projects" class="cta-btn primary-btn">View Projects</a>
      {resume_btn}
    </div>
  </div>
</div>

<hr class="divider">

<!-- AWARDS -->
<section id="awards">
  <div class="reveal"><div class="deco-line"></div></div>
  <p class="section-label reveal">Recognition</p>
  <h2 class="section-title reveal">Awards & Publications</h2>
  <div class="awards-grid">
    {awards_html}
  </div>
</section>

<hr class="divider">

<!-- PROJECTS -->
<section id="projects">
  <div class="reveal"><div class="deco-line"></div></div>
  <p class="section-label reveal">Work</p>
  <h2 class="section-title reveal">Engineering Projects</h2>
  <div class="grid">
    {projects_html}
  </div>
</section>

<hr class="divider">

<!-- SKILLS -->
<section id="skills">
  <div class="reveal"><div class="deco-line"></div></div>
  <p class="section-label reveal">Toolkit</p>
  <h2 class="section-title reveal">Skills & Tools</h2>
  <div class="skills-wrap reveal">
    {skills_html}
  </div>
</section>

<hr class="divider">

<!-- ABOUT -->
<section id="about">
  <div class="reveal"><div class="deco-line"></div></div>
  <p class="section-label reveal">About</p>
  <h2 class="section-title reveal">Who I Am</h2>
  <div class="about-layout">
    <div class="about-photo-wrap reveal-left">
      <div class="glow-ring"></div>
      <div class="about-photo-frame">
        <img src="{PHOTO_FILE}" alt="Gladys Fong" class="about-photo"
             onerror="this.style.display='none'">
      </div>
      <div class="about-photo-placeholder" id="photo-placeholder" style="display:none;">
        <p>Add your headshot!<br>Name it <strong>{PHOTO_FILE}</strong> and put it in your portfolio folder, then re-run the script.</p>
      </div>
    </div>
    <div class="about-text reveal-right">
      <div class="about-box">{PROFILE["about"]}</div>
      <div style="display:flex;gap:1rem;flex-wrap:wrap;">
        <a href="mailto:{PROFILE["email"]}" class="cta-btn primary-btn">Get in Touch</a>
        <a href="{PROFILE["linkedin"]}" target="_blank" class="cta-btn secondary-btn">LinkedIn</a>
        <a href="{PROFILE["github"]}" target="_blank" class="cta-btn secondary-btn">GitHub</a>
      </div>
    </div>
  </div>
</section>

<footer>
  <p>Built with Python &nbsp;·&nbsp; Hosted on GitHub Pages</p>
  <p style="margin-top:0.5rem;">
    <a href="mailto:{PROFILE["email"]}">{PROFILE["email"]}</a>
  </p>
</footer>

<script>
  // ── TYPING EFFECT ──
  const words = {typing_words_js};
  let wi = 0, ci = 0, deleting = false;
  const el = document.getElementById('typing-target');
  function type() {{
    const word = words[wi];
    if (!deleting) {{
      el.textContent = word.slice(0, ++ci);
      if (ci === word.length) {{ deleting = true; setTimeout(type, 1800); return; }}
    }} else {{
      el.textContent = word.slice(0, --ci);
      if (ci === 0) {{ deleting = false; wi = (wi + 1) % words.length; }}
    }}
    setTimeout(type, deleting ? 60 : 90);
  }}
  type();

  // ── SCROLL REVEAL ──
  const observer = new IntersectionObserver(entries => {{
    entries.forEach(e => {{ if (e.isIntersecting) e.target.classList.add('visible'); }});
  }}, {{ threshold: 0.1 }});
  document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach(el => observer.observe(el));

  // Stagger project cards
  document.querySelectorAll('.grid .card').forEach((c, i) => {{
    c.style.transitionDelay = (i * 0.09) + 's';
  }});
  document.querySelectorAll('.awards-grid .award-card').forEach((c, i) => {{
    c.style.transitionDelay = (i * 0.1) + 's';
  }});

  // ── NAV SCROLL ──
  window.addEventListener('scroll', () => {{
    document.getElementById('navbar').classList.toggle('scrolled', scrollY > 20);
  }});

  // ── PHOTO FALLBACK ──
  const photoImg = document.querySelector('.about-photo');
  const photoPlaceholder = document.getElementById('photo-placeholder');
  if (photoImg && photoImg.complete && photoImg.naturalWidth === 0) {{
    photoImg.style.display = 'none';
    photoPlaceholder.style.display = 'flex';
  }}
  if (photoImg) photoImg.addEventListener('error', () => {{
    photoImg.style.display = 'none';
    photoPlaceholder.style.display = 'flex';
  }});
</script>

</body>
</html>"""
    return html


if __name__ == "__main__":
    output = build_html()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(output)
    print("Done! index.html generated.")
    print(f"\nNext — add your photos to the 'my portfolio' folder:")
    print(f"  {PHOTO_FILE}  <- your headshot")
    for p in PROJECTS:
        print(f"  {p['photo']}  <- {p['title'][:40]}")
    print("\nThen push everything to GitHub!")
