from groq import Groq
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Create Groq client using .env key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_pitch(idea):

    prompt = f"""
    Create a startup pitch for:

    {idea}

    Format:

    Problem:
    - 4 points

    Solution:
    - 4 points

    Market Opportunity:
    - 4 points

    Business Model:
    - 4 points

    Competitive Advantage:
    - 4 points

    Go To Market:
    - 4 points

    Financial Projection:
    - 4 points
    """

    for attempt in range(2):
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are an expert startup pitch creator."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6
            )

            result = response.choices[0].message.content

            if result:
                return result.strip()

            return "⚠️ Empty response. Try again."

        except Exception as e:
            print(f"Attempt {attempt+1} failed:", str(e))

            return """
⚠️ API temporarily unavailable.

Sample Pitch:

Problem:
- Lack of efficient solutions
- High cost of alternatives
- Limited accessibility
- Fragmented experience

Solution:
- Centralized platform
- Affordable solution
- Easy-to-use interface
- Real-time services

Market Opportunity:
- Growing digital demand
- Large untapped users
- Expanding internet access
- Global scalability

Business Model:
- Subscription model
- Freemium upgrades
- Partner integrations
- Commission-based revenue

Competitive Advantage:
- Unique value proposition
- Better UX
- Scalable tech
- Strong differentiation

Go To Market:
- Social media marketing
- Influencer campaigns
- Referral programs
- Target niche users

Financial Projection:
- Break-even in 2–3 years
- Steady growth
- Low initial cost
- High scalability
"""

    return "⚠️ Pitch generation failed."
