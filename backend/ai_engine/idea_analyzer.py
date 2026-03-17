import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def analyze_idea(idea):

    prompt = f"""
    Analyze this startup idea:

    {idea}

    Provide:
    - Market demand
    - Competition
    - Risks
    - Opportunities
    - Feasibility score
    """

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return "⚠️ AI analysis temporarily unavailable due to API limits. Please try again."
