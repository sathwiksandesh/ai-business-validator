from google import genai
import os
from dotenv import load_dotenv
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def mentor_advice(idea):

    prompt = f"""
    You are a startup mentor.

    Provide strategic advice for this idea:

    {idea}

    Include:
    - Business Model
    - Revenue Streams
    - Go To Market Strategy
    - Growth Plan
    """

    for attempt in range(3):   # retry 3 times
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text

        except Exception as e:
            time.sleep(2)

    return "⚠️ Mentor advice temporarily unavailable due to high AI demand. Please try again."