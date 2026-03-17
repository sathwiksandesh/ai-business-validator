from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_pitch(idea):

    prompt = f"""
    Create a startup pitch deck outline.

    Idea: {idea}

    Slides:
    Problem
    Solution
    Market Opportunity
    Business Model
    Competitive Advantage
    Go To Market
    Financial Projection
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text