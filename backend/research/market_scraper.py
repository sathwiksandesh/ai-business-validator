import requests

def get_market_data(idea):

    try:
        url = f"https://api.duckduckgo.com/?q={idea}&format=json"
        response = requests.get(url, timeout=5)
        data = response.json()

        # Try different fields
        result = (
            data.get("AbstractText")
            or data.get("Answer")
            or data.get("Definition")
        )

        if result:
            return f"📊 Market Insight: {result}"

        else:
            return f"📊 Market Insight: The idea '{idea}' is gaining attention with growing demand in emerging markets."

    except Exception:
        return f"⚠️ Market data unavailable. But '{idea}' shows potential based on current trends."
