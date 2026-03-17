from groq import Groq
import os
from dotenv import load_dotenv
import time

load_dotenv()

# ✅ secure key usage
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def mentor_advice(idea):

    prompt = f"""
    You are a startup mentor.

    Give practical advice for:

    {idea}

    Format:

    Business Model:
    - 4 points

    Revenue Streams:
    - 4 points

    Go To Market Strategy:
    - 4 points

    Growth Plan:
    - 4 points
    """

    for attempt in range(2):
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are an expert startup mentor."},
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

            return "⚠️ API temporarily unavailable."

    return "⚠️ Mentor advice temporarily unavailable."
