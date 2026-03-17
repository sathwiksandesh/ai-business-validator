from groq import Groq
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Create Groq client securely
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_idea(idea):

    prompt = f"""
    You are a startup analyst.

    Analyze this idea:

    {idea}

    Give structured output:

    Market Demand:
    - 4 points

    Competition:
    - 4 points

    Risks:
    - 4 points

    Opportunities:
    - 4 points

    Feasibility Score:
    Score out of 10 with reason.
    """

    for attempt in range(2):
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",   # ✅ fast + stable
                messages=[
                    {"role": "system", "content": "You are an expert startup analyst."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6
            )

            result = response.choices[0].message.content

            if result:
                return result.strip()

            return "⚠️ Empty response. Try again."

        except Exception as e:
            error_msg = str(e)
            print(f"Attempt {attempt+1} failed:", error_msg)

            # 🚨 Safe fallback (for demo)
            return """
⚠️ API temporarily unavailable.

Sample Analysis:

Market Demand:
- Growing demand in digital-first markets
- Increasing adoption among young users
- Gap in underserved regions
- Rising need for scalable solutions

Competition:
- Moderate startup competition
- Few dominant players
- Scope for innovation
- Market still evolving

Risks:
- High acquisition costs
- Technical scalability issues
- Funding dependency
- User retention challenges

Opportunities:
- Expansion into new markets
- Strong scalability
- Strategic partnerships
- First-mover advantage

Feasibility Score:
7/10 – Good potential with execution focus needed.
"""

    return "⚠️ AI analysis temporarily unavailable."
