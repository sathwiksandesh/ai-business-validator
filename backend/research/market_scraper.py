import requests

def get_market_data(idea):

    url = "https://api.duckduckgo.com/?q=" + idea + "&format=json"

    r = requests.get(url)

    data = r.json()

    return data.get("Abstract","No data found")