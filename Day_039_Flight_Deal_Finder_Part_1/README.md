# Day 39 - Flight Deal Finder - Part 1

Part 1 is for Data Setup. We create a list of destinations and check if flight price is lower than our target price.

## Features
- Creates destinations.csv automatically
- Stores City, IATA Code, Lowest Price
- Checks Live Price vs Your Price
- Shows DEAL FOUND if price is cheaper
- Add New Destination option

## How to Run
1. Run the app:
   python main.py

2. Choose 1 to Check Deals
   Choose 2 to Add New Destination

## Output Example
Delhi (DEL) - Your Price: Rs.5000 | Live Price: Rs.4500
-> DEAL FOUND! Delhi is CHEAPER by Rs.500!

## Tech Used
- Python
- CSV Module

## Part 1 vs Part 2
- Part 1 (This File): Data Setup + Fake Live Prices for Testing
- Part 2 (Next Day): Real Amadeus Flight API + Email / SMS Alert

## IATA Codes
- Mumbai - BOM
- Delhi - DEL
- Goa - GOA
- Dubai - DXB
- Bangkok - BKK
- London - LHR