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
# GLOBAL STYLES
# ─────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Layout ── */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* ── Typography ── */
    .page-title {
        font-size: 2.4rem;
        font-weight: 700;
        color: #4F8BF9;
        margin-bottom: 0.2rem;
    }

    .page-subtitle {
        font-size: 1rem;
        color: #94a3b8;
        margin-bottom: 1.5rem;
    }

    .section-label {
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #64748b;
        margin-bottom: 0.4rem;
    }

    .card-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #e2e8f0;
        margin-bottom: 0.75rem;
    }

    /* ── Cards ── */
    .card {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 14px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 1.25rem;
        height: 100%;
    }

    .card-accent-blue  { border-left: 4px solid #4F8BF9; }
    .card-accent-green { border-left: 4px solid #22c55e; }
    .card-accent-amber { border-left: 4px solid #f59e0b; }
    .card-accent-rose  { border-left: 4px solid #f43f5e; }
    .card-accent-purple{ border-left: 4px solid #a855f7; }

    /* ── Score badge ── */
    .score-badge {
        display: inline-block;
        font-size: 2.5rem;
        font-weight: 700;
        color: #4F8BF9;
        line-height: 1;
    }

    .verdict-pill {
        display: inline-block;
        padding: 0.35rem 1rem;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 600;
        background: #166534;
        color: #bbf7d0;
        margin-top: 0.5rem;
    }

    /* ── Divider ── */
    hr { border-color: #1e293b !important; margin: 1.5rem 0; }
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
    placeholder="e.g. An AI-powered tool that helps freelancers write better proposals",
    label_visibility="visible"
)

analyze_clicked = st.button("🔍 Analyze Startup Idea", type="primary", use_container_width=False)


# ─────────────────────────────────────────────
# ANALYSIS RESULTS
# ─────────────────────────────────────────────
if analyze_clicked:
    if not idea.strip():
        st.warning("Please enter a startup idea before analyzing.")
        st.stop()

    with st.spinner("Running AI analysis — this may take a moment…"):

        # ── Fetch all data ──────────────────────────────
        analysis       = analyze_idea(idea)
        advice         = mentor_advice(idea)
        market         = get_market_data(idea)
        competitors_df = find_competitors()
        pitch          = generate_pitch(idea)
        score, verdict = generate_score()

    st.divider()

    # ── Row 1 : Idea Analysis  |  Mentor Advice ─────────
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown(
            '<div class="card card-accent-blue">'
            '<p class="section-label">AI Analysis</p>'
            '<p class="card-title">📊 Idea Breakdown</p>',
            unsafe_allow_html=True
        )

        with st.expander("⚠️ Risks", expanded=True):
            st.info("Potential challenges the startup might face.")

        with st.expander("🌟 Opportunities", expanded=True):
            st.success("Possible growth opportunities.")

        st.markdown("**Detailed analysis**")
        st.write(analysis)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            '<div class="card card-accent-purple">'
            '<p class="section-label">Strategy</p>'
            '<p class="card-title">🧠 Mentor Advice</p>',
            unsafe_allow_html=True
        )
        st.write(advice)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Row 2 : Market Research  |  Competitors ─────────
    col3, col4 = st.columns(2, gap="medium")

    with col3:
        st.markdown(
            '<div class="card card-accent-green">'
            '<p class="section-label">Research</p>'
            '<p class="card-title">📈 Market Research</p>',
            unsafe_allow_html=True
        )
        st.write(market)
        st.markdown("</div>", unsafe_allow_html=True)

    with col4:
        st.markdown(
            '<div class="card card-accent-amber">'
            '<p class="section-label">Landscape</p>'
            '<p class="card-title">🏢 Competitor Analysis</p>',
            unsafe_allow_html=True
        )
        st.dataframe(competitors_df, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Row 3 : Feasibility Score ────────────────────────
    st.markdown(
        '<div class="card card-accent-rose">'
        '<p class="section-label">Evaluation</p>'
        '<p class="card-title">⚡ Feasibility Score</p>',
        unsafe_allow_html=True
    )

    score_col, verdict_col, spacer = st.columns([1, 2, 3])

    with score_col:
        st.markdown(f'<span class="score-badge">{score}</span>', unsafe_allow_html=True)
        st.caption("Overall score")

    with verdict_col:
        st.markdown(f'<span class="verdict-pill">✅ {verdict}</span>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── Row 4 : Pitch Deck ───────────────────────────────
    st.markdown(
        '<div class="card card-accent-blue">'
        '<p class="section-label">Pitch</p>'
        '<p class="card-title">🎤 Startup Pitch Deck</p>',
        unsafe_allow_html=True
    )
    st.write(pitch)
    st.markdown("</div>", unsafe_allow_html=True)