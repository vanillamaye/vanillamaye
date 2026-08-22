import json
import requests
from bs4 import BeautifulSoup

USERNAME = "vanillamaye"
URL = f"https://github.com/users/{USERNAME}/contributions"

res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

days = []
for cell in soup.find_all("td", class_="ContributionCalendar-day"):
    date = cell.get("data-date")
    level = cell.get("data-level", "0")
    if date:
        days.append({"date": date, "level": int(level)})

with open("data/contributions.json", "w") as f:
    json.dump(days, f, indent=2)

print(f"Fetched {len(days)} contribution days.")
