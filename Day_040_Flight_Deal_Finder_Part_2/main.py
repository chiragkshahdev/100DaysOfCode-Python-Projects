# Day 40 - Flight Deal Finder - Part 2
# Part 2 = Check Deals + Send Alert (No API Key Version)

import csv
import os
from datetime import datetime

DESTINATIONS_FILE = "destinations.csv"
ALERTS_FILE = "alerts.txt"

# Fake Live Prices - Part 2 me isko Real API samajh
# IATA : [Live Price, Airline, Departure Date]
LIVE_FLIGHTS = {
    "DEL": [4500, "IndiGo", "2026-11-20"],
    "GOA": [5500, "Air India", "2026-11-25"],
    "DXB": [14000, "Emirates", "2026-12-01"],
    "BKK": [13000, "Thai Airways", "2026-12-05"],
    "LHR": [32000, "British Airways", "2026-12-10"],
    "BOM": [3500, "IndiGo", "2026-11-18"],
}

def get_destinations():
    if not os.path.exists(DESTINATIONS_FILE):
        print(f"{DESTINATIONS_FILE} not found! First Day 039 Run The code.")
        return []
    with open(DESTINATIONS_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

def send_alert(city, iata, lowest, live, airline, date, savings):
    message = f"""
    ✈️ FLIGHT DEAL ALERT! ✈️

    {city} ({iata}) is CHEAP NOW!

    Your Target Price: Rs.{lowest}
    Live Price: Rs.{live}
    You Save: Rs.{savings}

    Airline: {airline}
    Departure: {date}

    Book Fast Before Price Goes Up!
    """
    print(message)

    # Save alert like Email / SMS
    with open(ALERTS_FILE, mode="a", encoding="utf-8") as file:
        file.write(f"\n--- {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ---\n")
        file.write(message)

    print("Alert Saved in alerts.txt (Email/SMS Simulation)")

def check_and_alert():
    print("=== Day 40 - Flight Deal Finder (Part 2) ===\n")
    print("Checking All Destinations for Deals...\n")

    destinations = get_destinations()
    if not destinations:
        return

    deals_found = 0

    for row in destinations:
        city = row["City"]
        iata = row["IATA"]
        lowest = int(row["Lowest Price"])

        if iata not in LIVE_FLIGHTS:
            print(f"{city} ({iata}) - No flight data available.\n")
            continue

        live, airline, date = LIVE_FLIGHTS[iata]

        print(f"{city} ({iata}) - Target: Rs.{lowest} | Live: Rs.{live} | {airline}")

        if live < lowest:
            savings = lowest - live
            print(f"  -> DEAL FOUND! Saving Rs.{savings}\n")
            send_alert(city, iata, lowest, live, airline, date, savings)
            deals_found += 1
        else:
            print(f"  -> No Deal.\n")

    print(f"Done! Total Deals Found: {deals_found}")
    if deals_found > 0:
        print("Check alerts.txt for all alerts.")

def main():
    check_and_alert()

if __name__ == "__main__":
    main()