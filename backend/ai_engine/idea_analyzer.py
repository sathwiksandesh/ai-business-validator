import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def analyze_full_idea(idea):

    prompt = f"""
    Analyze this startup idea:

    {idea}

    Return structured output with:

    1. Market Demand
    2. Competition
    3. Risks
    4. Opportunities
    5. Business Model
    6. Revenue Streams
    7. Growth Strategy
    8. Feasibility Score (0-100)
    9. Pitch Summary
    """

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception:
        return "⚠️ AI service temporarily unavailable. Please try again."
