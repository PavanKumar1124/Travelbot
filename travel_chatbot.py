import streamlit as st
from groq import Groq
from datetime import datetime

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="✈️ AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",   # collapsed by default → mobile-friendly
)

# ─────────────────────────────────────────────
#  FULL RESPONSIVE CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
/* ── Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
*, html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    box-sizing: border-box;
}

/* ── Remove streamlit top padding ── */
.block-container { padding-top: 1rem !important; max-width: 100% !important; }

/* ══════════════════════════════════
   HERO BANNER
══════════════════════════════════ */
.hero {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    padding: 2.2rem 2rem;
    border-radius: 20px;
    margin-bottom: 1.2rem;
    text-align: center;
    color: white;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; inset: 0;
    background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
.hero h1 {
    font-size: clamp(1.4rem, 4vw, 2.4rem);
    font-weight: 700;
    margin: 0;
    letter-spacing: -0.5px;
}
.hero p {
    font-size: clamp(0.78rem, 2.5vw, 1rem);
    color: #a0aec0;
    margin: 0.4rem 0 0;
    line-height: 1.5;
}
.hero-badges {
    display: flex;
    gap: 0.5rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 0.9rem;
}
.hero-badge {
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.2);
    color: white;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.72rem;
    font-weight: 500;
    backdrop-filter: blur(4px);
}

/* ══════════════════════════════════
   API KEY BANNER (shown when no key)
══════════════════════════════════ */
.api-banner {
    background: linear-gradient(90deg, #fff7ed, #fef3c7);
    border: 1px solid #fbbf24;
    border-radius: 12px;
    padding: 0.9rem 1.2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1rem;
    flex-wrap: wrap;
}
.api-banner-text { font-size: 0.85rem; color: #78350f; }
.api-banner-text b { font-weight: 600; }
.api-banner-link {
    background: #f59e0b;
    color: white !important;
    border-radius: 8px;
    padding: 6px 14px;
    font-size: 0.8rem;
    font-weight: 600;
    text-decoration: none;
    white-space: nowrap;
}

/* ══════════════════════════════════
   STATUS BAR
══════════════════════════════════ */
.status-bar {
    background: #f0fff4;
    border: 1px solid #9ae6b4;
    border-radius: 10px;
    padding: 0.5rem 1rem;
    font-size: 0.78rem;
    color: #276749;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.3rem;
    margin-bottom: 0.8rem;
}
.status-dot {
    width: 8px; height: 8px;
    background: #48bb78;
    border-radius: 50%;
    display: inline-block;
    margin-right: 5px;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}

/* ══════════════════════════════════
   QUICK DESTINATION CHIPS  (mobile bar)
══════════════════════════════════ */
.dest-scroll-wrapper {
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    margin-bottom: 1rem;
    padding-bottom: 4px;
}
.dest-scroll-wrapper::-webkit-scrollbar { display: none; }
.dest-chips {
    display: flex;
    gap: 0.5rem;
    white-space: nowrap;
    padding: 2px 0;
}
.dest-chip {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: white;
    border: 1.5px solid #e2e8f0;
    border-radius: 30px;
    padding: 6px 14px;
    font-size: 0.8rem;
    font-weight: 500;
    color: #2d3748;
    cursor: pointer;
    transition: all 0.2s;
    text-decoration: none;
    white-space: nowrap;
    user-select: none;
}
.dest-chip:hover {
    background: #ebf4ff;
    border-color: #90cdf4;
    color: #2b6cb0;
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

/* ══════════════════════════════════
   FEATURE CARDS GRID
══════════════════════════════════ */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.8rem;
    margin-bottom: 1.2rem;
}
.feature-card {
    background: white;
    border: 1px solid #e8edf5;
    border-radius: 14px;
    padding: 1rem;
    text-align: center;
    transition: box-shadow 0.2s, transform 0.2s;
}
.feature-card:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    transform: translateY(-2px);
}
.feature-card .icon { font-size: 1.7rem; line-height: 1; }
.feature-card .title {
    font-size: 0.82rem;
    font-weight: 600;
    color: #2d3748;
    margin-top: 0.4rem;
}
.feature-card .sub {
    font-size: 0.7rem;
    color: #718096;
    margin-top: 0.15rem;
}

/* ══════════════════════════════════
   HINT BOX
══════════════════════════════════ */
.hint-box {
    background: #fffbeb;
    border: 1px solid #fbd38d;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-bottom: 1rem;
    font-size: 0.85rem;
    color: #744210;
}
.hint-box code {
    background: #fef3c7;
    border-radius: 4px;
    padding: 1px 6px;
    font-size: 0.78rem;
}

/* ══════════════════════════════════
   CHAT MESSAGES
══════════════════════════════════ */
.stChatMessage {
    border-radius: 14px !important;
    border: 1px solid #f0f4f8 !important;
}
/* Make tables inside chat messages scroll on mobile */
.stChatMessage table {
    display: block;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    max-width: 100%;
    font-size: 0.82rem;
}
.stChatMessage th, .stChatMessage td {
    padding: 6px 10px !important;
    white-space: nowrap;
}

/* ══════════════════════════════════
   SIDEBAR
══════════════════════════════════ */
section[data-testid="stSidebar"] {
    background: #f8faff;
    border-right: 1px solid #e2e8f0;
}
section[data-testid="stSidebar"] .stButton button {
    border-radius: 8px;
    font-size: 0.82rem;
    min-height: 40px;
    background: white;
    border: 1px solid #e2e8f0;
    color: #2d3748;
    text-align: left;
    width: 100%;
    transition: all 0.15s;
}
section[data-testid="stSidebar"] .stButton button:hover {
    background: #ebf4ff;
    border-color: #90cdf4;
    color: #2b6cb0;
}
.sidebar-section {
    background: white;
    border: 1px solid #e8edf5;
    border-radius: 12px;
    padding: 0.8rem;
    margin-bottom: 0.8rem;
}
.sidebar-label {
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #a0aec0;
    margin-bottom: 0.5rem;
}

/* ══════════════════════════════════
   TRAVELER BADGE
══════════════════════════════════ */
.traveler-badge {
    background: linear-gradient(135deg, #e6fffa, #b2f5ea);
    border: 1px solid #81e6d9;
    color: #234e52;
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 0.8rem;
    font-weight: 600;
    display: inline-block;
    margin: 0.3rem 0;
}

/* ══════════════════════════════════
   ACTION BUTTONS
══════════════════════════════════ */
.stButton button {
    min-height: 42px;       /* touch-friendly tap target */
    border-radius: 10px !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
}

/* ══════════════════════════════════
   MOBILE BOTTOM INFO BAR
══════════════════════════════════ */
.mobile-info {
    display: none;
    background: #1a1a2e;
    color: #a0aec0;
    text-align: center;
    font-size: 0.72rem;
    padding: 0.6rem;
    border-radius: 10px;
    margin-top: 1rem;
}

/* ══════════════════════════════════
   RESPONSIVE BREAKPOINTS
══════════════════════════════════ */

/* Tablet: 768px */
@media (max-width: 768px) {
    .block-container { padding: 0.5rem 0.6rem !important; }

    .hero { padding: 1.4rem 1rem; border-radius: 14px; }
    .hero h1 { font-size: 1.5rem; }
    .hero p  { font-size: 0.78rem; }
    .hero-badge { font-size: 0.65rem; padding: 2px 9px; }

    .feature-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 0.6rem;
    }
    .feature-card { padding: 0.8rem 0.6rem; }
    .feature-card .icon { font-size: 1.4rem; }
    .feature-card .title { font-size: 0.75rem; }
    .feature-card .sub { display: none; }   /* hide subtitle on tablet */

    .status-bar { font-size: 0.72rem; padding: 0.4rem 0.8rem; }

    /* Make chat input larger on touch */
    .stChatInputContainer textarea {
        font-size: 16px !important; /* prevents iOS zoom */
        min-height: 50px !important;
    }

    .mobile-info { display: block; }

    /* Scrollable tables */
    table { font-size: 0.75rem !important; }

    .api-banner { flex-direction: column; gap: 0.6rem; }
}

/* Phone: 480px */
@media (max-width: 480px) {
    .block-container { padding: 0.4rem !important; }

    .hero { padding: 1.1rem 0.8rem; border-radius: 12px; margin-bottom: 0.8rem; }
    .hero h1 { font-size: 1.25rem; }
    .hero-badges { gap: 0.35rem; margin-top: 0.6rem; }
    .hero-badge { font-size: 0.6rem; padding: 2px 8px; }

    .feature-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 0.5rem;
        margin-bottom: 0.8rem;
    }
    .feature-card { padding: 0.7rem 0.5rem; border-radius: 10px; }
    .feature-card .icon { font-size: 1.25rem; }
    .feature-card .title { font-size: 0.7rem; }

    .dest-chip { font-size: 0.72rem; padding: 5px 11px; }

    .hint-box { font-size: 0.78rem; padding: 0.8rem; }

    .stChatMessage { border-radius: 10px !important; }
    .stChatMessage table { font-size: 0.7rem; }

    .status-bar {
        font-size: 0.68rem;
        flex-direction: column;
        gap: 0.2rem;
        align-items: flex-start;
    }
}

/* Very small phones: 360px */
@media (max-width: 360px) {
    .hero h1 { font-size: 1.1rem; }
    .feature-grid { grid-template-columns: 1fr 1fr; }
    .hero-badges { display: none; }
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  SYSTEM PROMPT
# ─────────────────────────────────────────────
SYSTEM_PROMPT = """You are an intelligent Travel Planning Assistant.
Your job is to help users explore tourist destinations and generate structured, accurate, and budget-friendly travel plans.

RESPONSE FORMAT (MANDATORY) — always use markdown:

## 📍 Overview
| Detail | Info |
|--------|------|
| Location | ... |
| Best Time to Visit | ... |
| Language | ... |
| Currency | ... |

Short 2-line description of the place.

## ⭐ Top Attractions
- 🏛️ **Name** — short description
(list 5–7 attractions)

## 🏨 Accommodation Options
| Type | Options | Approx. Cost/Night |
|------|---------|-------------------|
| 💚 Budget | ... | ₹/$ range |
| 💛 Mid-range | ... | ₹/$ range |
| ❤️ Luxury | ... | ₹/$ range |

## 🍽️ Food & Local Experience
**Must-Try Foods:**
- emoji Food name — description

**Experiences:**
- bullet points

## 🚗 Transportation
| Mode | Details |
|------|---------|
| ✈️ Flight | ... |
| 🚂 Train | ... |
| 🚌 Bus | ... |

**Local Transport:** bullet points

## 💰 Estimated Budget (Per Person)
| Category | Budget | Mid-range | Luxury |
|----------|--------|-----------|--------|
| ✈️ Travel | ... | ... | ... |
| 🏨 Stay (5 nights) | ... | ... | ... |
| 🍽️ Food (5 days) | ... | ... | ... |
| 🎯 Activities | ... | ... | ... |

## 🔗 Useful Links
- 🌐 [Official Tourism Website](url)
- 🗺️ [Google Maps](url)
- 🏨 [Book Hotels](url)
- ✈️ [Flights](url)
- 📸 [Travel Guide](url)

---
After providing destination info, ALWAYS end with:
**👥 How many people are traveling?** (I'll calculate the group budget for you!)

WHEN USER GIVES NUMBER OF TRAVELERS:

## 💼 Group Budget Plan — [N] Travelers

### 💰 Total Estimated Cost
| Category | Per Person | Total ([N] people) |
|----------|-----------|------------------|
| Travel | ... | ... |
| Accommodation | ... | ... |
| Food | ... | ... |
| Activities | ... | ... |
| **GRAND TOTAL** | **...** | **...** |

### 💡 Cost-Saving Tips
- 3-5 practical tips

RULES:
- Use INR (₹) for Indian destinations, USD ($) for international
- Always use markdown tables and bullet points
- Keep responses scannable
- Include working hyperlinks
"""

# ─────────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────────
DESTINATIONS = {
    "🇮🇳 India": [
        ("🏖️", "Goa"), ("🏰", "Rajasthan"), ("🏔️", "Shimla"),
        ("🕌", "Agra"), ("🌿", "Kerala"), ("🏙️", "Mumbai"),
    ],
    "🌏 Asia": [
        ("🌴", "Bali"), ("🏯", "Kyoto"), ("🏖️", "Phuket"),
        ("🌆", "Singapore"), ("🏔️", "Nepal"),
    ],
    "🌍 World": [
        ("🗼", "Paris"), ("🗽", "New York"), ("🏙️", "Dubai"),
        ("🎭", "Rome"), ("🌉", "London"),
    ],
}

ALL_DESTINATIONS = [
    ("🏖️", "Goa"), ("🏰", "Rajasthan"), ("🌿", "Kerala"), ("🏔️", "Shimla"),
    ("🌴", "Bali"), ("🏯", "Kyoto"), ("🗼", "Paris"), ("🏙️", "Dubai"),
    ("🗽", "New York"), ("🏖️", "Phuket"), ("🎭", "Rome"), ("🌆", "Singapore"),
]

MODELS = {
    "⚡ Llama 3.3 70B (Best)": "llama-3.3-70b-versatile",
    "🚀 Llama 3.1 8B (Fast)": "llama-3.1-8b-instant",
    "💎 Gemma2 9B": "gemma2-9b-it",
    "🔥 Mixtral 8x7B": "mixtral-8x7b-32768",
}

# ─────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────
for k, v in {
    "messages": [],
    "travelers": 1,
    "current_dest": None,
    "quick_dest": None,
    "api_key": "",
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ✈️ Travel Planner")
    st.markdown("---")

    # ── API Key ──
    st.markdown('<div class="sidebar-label">🔑 API Configuration</div>', unsafe_allow_html=True)
    api_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="gsk_...",
        value=st.session_state.api_key,
        help="Free at https://console.groq.com",
        label_visibility="collapsed",
    )
    st.session_state.api_key = api_key

    if api_key:
        st.markdown('<div style="color:#276749;font-size:0.8rem;font-weight:600;">✅ Connected</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<a href="https://console.groq.com" target="_blank" style="font-size:0.78rem;color:#3182ce;">🆓 Get free API key →</a>',
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ── Model ──
    st.markdown('<div class="sidebar-label">🤖 Model</div>', unsafe_allow_html=True)
    model_label = st.selectbox(
        "Model",
        list(MODELS.keys()),
        label_visibility="collapsed",
    )
    model = MODELS[model_label]

    st.markdown("---")

    # ── Travelers ──
    st.markdown('<div class="sidebar-label">👥 Group Size</div>', unsafe_allow_html=True)
    travelers = st.number_input(
        "travelers",
        min_value=1, max_value=50,
        value=st.session_state.travelers,
        label_visibility="collapsed",
    )
    st.session_state.travelers = travelers

    if travelers == 1:
        st.markdown('<div class="traveler-badge">👤 Solo Traveler</div>', unsafe_allow_html=True)
    elif travelers <= 4:
        st.markdown(f'<div class="traveler-badge">👥 Group of {travelers}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="traveler-badge">🚌 Large Group ({travelers})</div>', unsafe_allow_html=True)

    if st.session_state.current_dest:
        if st.button(f"💰 Budget for {travelers} → {st.session_state.current_dest}", use_container_width=True):
            st.session_state.quick_dest = f"budget:{travelers}"

    st.markdown("---")

    # ── Destinations ──
    st.markdown('<div class="sidebar-label">🌍 Destinations</div>', unsafe_allow_html=True)
    for region, places in DESTINATIONS.items():
        with st.expander(region, expanded=(region == "🇮🇳 India")):
            for icon, place in places:
                if st.button(f"{icon} {place}", key=f"sb_{place}", use_container_width=True):
                    st.session_state.quick_dest = place
                    st.session_state.current_dest = place

    st.markdown("---")

    # ── Actions ──
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🗑️ Clear", use_container_width=True):
            st.session_state.messages = []
            st.session_state.current_dest = None
            st.rerun()
    with c2:
        st.download_button(
            "⬇️ Save",
            data="\n\n".join(f"[{m['role'].upper()}]\n{m['content']}" for m in st.session_state.messages) or "No chat yet.",
            file_name=f"trip_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
            mime="text/plain",
            use_container_width=True,
        )

    st.markdown(
        "<br><center><small style='color:#a0aec0;'>🚀 Powered by Groq · Free API<br>No credit card required</small></center>",
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
#  MAIN CONTENT
# ─────────────────────────────────────────────

# ── Hero ──
st.markdown(f"""
<div class="hero">
    <h1>✈️ AI Travel Planning Assistant</h1>
    <p>Explore destinations · Plan itineraries · Calculate group budgets</p>
    <div class="hero-badges">
        <span class="hero-badge">📍 Destination Info</span>
        <span class="hero-badge">⭐ Top Attractions</span>
        <span class="hero-badge">🏨 Hotels</span>
        <span class="hero-badge">💰 Budget Calculator</span>
        <span class="hero-badge">🚗 Transport</span>
        <span class="hero-badge">🍽️ Food Guide</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── API Key Banner (shown when no key) ──
if not api_key:
    st.markdown("""
    <div class="api-banner">
        <div class="api-banner-text">
            <b>🔑 No API Key found.</b> Get a free Groq API key to start planning your trips!
        </div>
        <a href="https://console.groq.com" target="_blank" class="api-banner-link">
            Get Free Key →
        </a>
    </div>
    """, unsafe_allow_html=True)

# ── Status bar (active session) ──
if api_key and st.session_state.messages:
    count = len([m for m in st.session_state.messages if m["role"] == "assistant"])
    dest_str = f"📍 {st.session_state.current_dest}" if st.session_state.current_dest else "🌍 Exploring"
    st.markdown(f"""
    <div class="status-bar">
        <span><span class="status-dot"></span>Connected · {model_label.split()[1]} model</span>
        <span>{dest_str}</span>
        <span>💬 {count} replies · 👥 {travelers} traveler(s)</span>
        <span>🕐 {datetime.now().strftime("%H:%M")}</span>
    </div>
    """, unsafe_allow_html=True)

# ── WELCOME SCREEN (no messages yet) ──
if not st.session_state.messages:

    # Feature cards
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <div class="icon">📍</div>
            <div class="title">Destination Info</div>
            <div class="sub">Overview · Climate · Culture</div>
        </div>
        <div class="feature-card">
            <div class="icon">⭐</div>
            <div class="title">Top Attractions</div>
            <div class="sub">5–7 must-visit spots</div>
        </div>
        <div class="feature-card">
            <div class="icon">🏨</div>
            <div class="title">Accommodation</div>
            <div class="sub">Budget to Luxury</div>
        </div>
        <div class="feature-card">
            <div class="icon">🍽️</div>
            <div class="title">Food Guide</div>
            <div class="sub">Local cuisine & tips</div>
        </div>
        <div class="feature-card">
            <div class="icon">💰</div>
            <div class="title">Budget Planner</div>
            <div class="sub">Per person & group</div>
        </div>
        <div class="feature-card">
            <div class="icon">🚗</div>
            <div class="title">Transport</div>
            <div class="sub">How to reach & move</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Quick Destination Chips (scrollable, mobile-friendly) ──
    st.markdown('<p style="font-size:0.82rem;font-weight:600;color:#4a5568;margin-bottom:0.4rem;">🌍 Quick Explore</p>', unsafe_allow_html=True)

    chips_html = '<div class="dest-scroll-wrapper"><div class="dest-chips">'
    for icon, place in ALL_DESTINATIONS:
        chips_html += f'<span class="dest-chip" onclick="">{icon} {place}</span>'
    chips_html += '</div></div>'
    st.markdown(chips_html, unsafe_allow_html=True)

    # Streamlit buttons for actual chip interaction (hidden visually as the HTML chips are decorative)
    chip_cols = st.columns(6)
    for i, (icon, place) in enumerate(ALL_DESTINATIONS[:6]):
        with chip_cols[i % 6]:
            if st.button(f"{icon} {place}", key=f"chip_{place}", use_container_width=True):
                st.session_state.quick_dest = place
                st.session_state.current_dest = place
                st.rerun()

    chip_cols2 = st.columns(6)
    for i, (icon, place) in enumerate(ALL_DESTINATIONS[6:]):
        with chip_cols2[i % 6]:
            if st.button(f"{icon} {place}", key=f"chip2_{place}", use_container_width=True):
                st.session_state.quick_dest = place
                st.session_state.current_dest = place
                st.rerun()

    # Hint box
    st.markdown("""
    <div class="hint-box">
        <b>💡 How to use:</b><br>
        1. Enter your <b>Groq API key</b> in the ☰ sidebar &nbsp;·&nbsp;
        2. Click a destination above or type below &nbsp;·&nbsp;
        3. Set <b>travelers</b> in sidebar for group budget<br><br>
        <b>Try:</b>
        <code>Tell me about Goa</code> &nbsp;
        <code>Plan a 5-day trip to Paris</code> &nbsp;
        <code>Budget for 4 people in Bali</code>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  HANDLE QUICK DESTINATION TRIGGER
# ─────────────────────────────────────────────
if st.session_state.quick_dest:
    qd = st.session_state.quick_dest
    if qd.startswith("budget:"):
        n = qd.split(":")[1]
        prompt = f"Calculate the complete group budget for {n} people traveling to {st.session_state.current_dest}."
    else:
        prompt = f"Tell me about {qd}"
        st.session_state.current_dest = qd
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.quick_dest = None

# ─────────────────────────────────────────────
#  CHAT HISTORY
# ─────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🧳" if msg["role"] == "user" else "✈️"):
        st.markdown(msg["content"])

# ─────────────────────────────────────────────
#  CHAT INPUT
# ─────────────────────────────────────────────
user_input = st.chat_input("✈️ Ask about any destination or trip...")

if user_input:
    # Auto-detect traveler count from message
    for w in user_input.split():
        if w.isdigit() and 1 <= int(w) <= 50:
            st.session_state.travelers = int(w)
            break
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="🧳"):
        st.markdown(user_input)

# ─────────────────────────────────────────────
#  AI RESPONSE — STREAMING
# ─────────────────────────────────────────────
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    if not api_key:
        with st.chat_message("assistant", avatar="✈️"):
            st.warning(
                "⚠️ **API Key Required**\n\n"
                "1. Open the **☰ sidebar** (top-left)\n"
                "2. Paste your Groq API key\n"
                "3. Get a free key at 👉 **https://console.groq.com**\n\n"
                "_100% free — no credit card needed!_"
            )
    else:
        try:
            client = Groq(api_key=api_key)
            system = (
                SYSTEM_PROMPT
                + f"\n\nGroup size: {st.session_state.travelers} traveler(s). "
                "Always tailor budget to this group size."
            )

            with st.chat_message("assistant", avatar="✈️"):
                stream = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system},
                        *[{"role": m["role"], "content": m["content"]}
                          for m in st.session_state.messages],
                    ],
                    temperature=0.7,
                    max_tokens=3000,
                    stream=True,
                )
                reply = st.write_stream(
                    chunk.choices[0].delta.content or ""
                    for chunk in stream
                    if chunk.choices[0].delta.content
                )

            st.session_state.messages.append({"role": "assistant", "content": reply})

            # Auto-detect destination
            last = st.session_state.messages[-2]["content"].lower()
            for places in DESTINATIONS.values():
                for _, p in places:
                    if p.lower() in last:
                        st.session_state.current_dest = p
                        break

        except Exception as e:
            err = str(e)
            with st.chat_message("assistant", avatar="✈️"):
                if "401" in err or "invalid_api_key" in err.lower():
                    st.error("❌ **Invalid API Key.** Please check your key in the sidebar.")
                elif "429" in err or "rate_limit" in err.lower():
                    st.warning("⏳ **Rate limit hit.** Please wait a moment and try again.")
                else:
                    st.error(f"❌ {err}")

# ── Mobile bottom note ──
st.markdown(
    '<div class="mobile-info">☰ Open sidebar for settings · 🌍 Destinations · 💰 Budget planner</div>',
    unsafe_allow_html=True,
)
