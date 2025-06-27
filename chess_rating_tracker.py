#!/usr/bin/env python3 # If you ever run the script directly (not via python3 ...)
# Make sure to update the data placed between square brackets (username and path)

import requests
import csv
from datetime import datetime
from pytz import timezone
from pathlib import Path

ct = timezone("America/Chicago")
now = datetime.now(ct)

headers = {
    "User-Agent": "Mozilla/5.0"
} # Some websites block requests that don’t include a User-Agent header (which browsers send by default).

url = "https://api.chess.com/pub/player/[USERNAME]/stats"
response = requests.get(url, headers=headers)

if response.ok:
    data = response.json()
    rapid_rating = data["chess_rapid"]["last"]["rating"]
    blitz_rating = data["chess_blitz"]["last"]["rating"]

    print(f"Rapid Rating: {rapid_rating}")
    print(f"Blitz Rating: {blitz_rating}")
    print(data)
else:
    print("Error fetching data:", response.status_code)

csv_path = Path([LIST ABSOLUTE PATH BETWEEN QUOTES TO CSV FILE TO SAVE THE DATA]
with open(csv_path, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([now.strftime("%Y-%m-%d %H:%M:%S %Z"), rapid_rating, blitz_rating])
