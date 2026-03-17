import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.ai_engine.idea_analyzer import analyze_idea
from backend.ai_engine.mentor_agent import mentor_advice
from backend.ai_engine.pitch_generator import generate_pitch
from backend.research.market_scraper import get_market_data
from backend.research.competitor_finder import find_competitors
from backend.scoring.feasibility_score import generate_score

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AI Startup Validator",
    page_icon="🚀",
    layout="wide"
)

# ─────────────────────────────────────────────
# GLOBAL STYLES (FIXED + PREMIUM)
# ─────────────────────────────────────────────
st.markdown("""
<style>
.block-container {
    padding-top: 4rem !important;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Title */
.page-title {
    font-size: 4.2rem;
    font-weight: 900;
    background: linear-gradient(90deg, #4F8BF9, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.page-subtitle {
    font-size: 1.2rem;
    color: #94a3b8;
    margin-bottom: 2rem;
}

/* Labels */
.section-label {
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #64748b;
    margin-bottom: 0.5rem;
}

/* Card titles */
.card-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 0.8rem;
}

/* Cards */
.card {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 18px;
    padding: 1.8rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.25);
}

.card-accent-blue  { border-left: 4px solid #4F8BF9; }
.card-accent-green { border-left: 4px solid #22c55e; }
.card-accent-amber { border-left: 4px solid #f59e0b; }
.card-accent-rose  { border-left: 4px solid #f43f5e; }
.card-accent-purple{ border-left: 4px solid #a855f7; }

/* Button */
.stButton > button {
    font-size: 1rem;
    font-weight: 600;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
}

/* Score */
.score-badge {
    font-size: 3.2rem;
    font-weight: 800;
    color: #4F8BF9;
}

.verdict-pill {
    padding: 0.45rem 1.2rem;
    font-size: 0.95rem;
    border-radius: 999px;
}

/* Divider */
hr {
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown('<p class="page-title">🚀 AI Business Idea Validator</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="page-subtitle">Validate your startup idea in seconds — '
    'AI-powered market research, competitive analysis, and strategy advice.</p>',
    unsafe_allow_html=True
)
st.divider()

# ─────────────────────────────────────────────
# INPUT
# ─────────────────────────────────────────────
idea = st.text_input(
    label="Your Startup Idea",
    placeholder="e.g. AI agriculture assistant for farmers"
)

analyze_clicked = st.button(
    "🔍 Analyze Startup Idea",
    type="primary",
    use_container_width=True
)

# ─────────────────────────────────────────────
# ANALYSIS
# ─────────────────────────────────────────────
if analyze_clicked:
    if not idea.strip():
        st.warning("Please enter a startup idea before analyzing.")
        st.stop()

    with st.spinner("Running AI analysis — please wait..."):

        analysis       = analyze_idea(idea)
        advice         = mentor_advice(idea)
        market         = get_market_data(idea)
        competitors_df = find_competitors()
        pitch          = generate_pitch(idea)
        score, verdict = generate_score()

    st.divider()

    # ── Row 1 ─────────────────────────────
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card card-accent-blue">', unsafe_allow_html=True)
        st.markdown('<p class="section-label">AI Analysis</p>', unsafe_allow_html=True)
        st.markdown('<p class="card-title">📊 Idea Breakdown</p>', unsafe_allow_html=True)

        st.write(analysis)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card card-accent-purple">', unsafe_allow_html=True)
        st.markdown('<p class="section-label">Strategy</p>', unsafe_allow_html=True)
        st.markdown('<p class="card-title">🧠 Mentor Advice</p>', unsafe_allow_html=True)

        st.write(advice)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Row 2 ─────────────────────────────
    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="card card-accent-green">', unsafe_allow_html=True)
        st.markdown('<p class="section-label">Research</p>', unsafe_allow_html=True)
        st.markdown('<p class="card-title">📈 Market Research</p>', unsafe_allow_html=True)

        st.write(market)
        st.markdown("</div>", unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card card-accent-amber">', unsafe_allow_html=True)
        st.markdown('<p class="section-label">Landscape</p>', unsafe_allow_html=True)
        st.markdown('<p class="card-title">🏢 Competitor Analysis</p>', unsafe_allow_html=True)

        st.dataframe(competitors_df, width="stretch", hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Score ─────────────────────────────
    st.markdown('<div class="card card-accent-rose">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Evaluation</p>', unsafe_allow_html=True)
    st.markdown('<p class="card-title">⚡ Feasibility Score</p>', unsafe_allow_html=True)

    score_col, verdict_col = st.columns([1, 3])

    with score_col:
        st.markdown(f'<span class="score-badge">{score}</span>', unsafe_allow_html=True)
        st.caption("Overall score")

    with verdict_col:
        st.markdown(f'<span class="verdict-pill">✅ {verdict}</span>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── Pitch ─────────────────────────────
    st.markdown('<div class="card card-accent-blue">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Pitch</p>', unsafe_allow_html=True)
    st.markdown('<p class="card-title">🎤 Startup Pitch Deck</p>', unsafe_allow_html=True)

    st.write(pitch)
    st.markdown("</div>", unsafe_allow_html=True)
