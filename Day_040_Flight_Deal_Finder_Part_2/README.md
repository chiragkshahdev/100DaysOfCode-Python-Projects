# Day 40 - Flight Deal Finder - Part 2

Part 2 adds Alert System. If flight price is lower than your target, it sends an alert.

## Features
- Reads destinations.csv from Day 39
- Checks Live Flight Price vs Your Target Price
- Sends Flight Deal Alert if cheaper
- Saves all alerts in alerts.txt (Email/SMS Simulation)
- Shows Airline Name, Date, Savings

## How to Run
1. Make sure destinations.csv exists from Day 39
   If not, run Day 39 code first

2. Run the app:
   python main.py

## Output Example
Delhi (DEL) - Target: Rs.5000 | Live: Rs.4500 | IndiGo
-> DEAL FOUND! Saving Rs.500

Alert Saved in alerts.txt

## Files Created
- destinations.csv (from Day 39)
- alerts.txt (All Deal Alerts)

## Tech Used
- Python
- CSV Module
- Datetime

## Part 1 vs Part 2
- Part 1: Data Setup + Check Prices
- Part 2: Check Prices + Send Alert (Email/SMS)

## Real Project Me Kya Hota?
Real project me Amadeus API se live price aata hai
aur Twilio / SMTP se Email/SMS jata hai.
Yaha humne usko bina key ke simulate kiya hai.