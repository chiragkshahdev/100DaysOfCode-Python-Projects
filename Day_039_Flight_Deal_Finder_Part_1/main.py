# Day 39 - Flight Deal Finder - Part 1
# Part 1 = Setup Data + Check Prices (No API Key Version)

import csv
import os

FILE_NAME = "destinations.csv"

# Our Dream Destinations with Lowest Price We Want
# City, IATA Code, Lowest Price (INR)
DEFAULT_DATA = [
    ["City", "IATA", "Lowest Price"],
    ["Delhi", "DEL", "5000"],
    ["Goa", "GOA", "4000"],
    ["Dubai", "DXB", "15000"],
    ["Bangkok", "BKK", "12000"],
    ["London", "LHR", "35000"],
]

# Fake Live Prices for Testing (Part 2 me isko Real API se replace karenge)
LIVE_PRICES = {
    "DEL": 4500,
    "GOA": 5500,
    "DXB": 14000,
    "BKK": 13000,
    "LHR": 32000,
}

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(DEFAULT_DATA)
        print(f"Created {FILE_NAME} with 5 destinations.")
    else:
        print(f"{FILE_NAME} already exists.")

def check_deals():
    print("\n=== Day 39 - Flight Deal Finder (Part 1) ===\n")
    print("Checking Flight Deals...\n")

    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row["City"]
            iata = row["IATA"]
            lowest = int(row["Lowest Price"])
            live = LIVE_PRICES.get(iata, 99999)

            print(f"{city} ({iata}) - Your Price: Rs.{lowest} | Live Price: Rs.{live}")

            if live < lowest:
                print(f"  -> DEAL FOUND! {city} is CHEAPER by Rs.{lowest - live}! Book Now!\n")
            else:
                print(f"  -> No Deal. Still Expensive.\n")

def add_destination():
    city = input("Enter City Name: ")
    iata = input("Enter IATA Code (e.g. BOM): ").upper()
    price = input("Enter Lowest Price You Want (INR): ")

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([city, iata, price])
    print(f"Added {city} ({iata}) successfully!")

def main():
    create_file()
    print("\n1. Check Deals")
    print("2. Add New Destination")
    choice = input("\nChoose (1-2): ")

    if choice == "1":
        check_deals()
    elif choice == "2":
        add_destination()
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()