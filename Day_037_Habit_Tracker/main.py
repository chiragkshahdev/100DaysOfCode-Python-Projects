# Day 37 - Habit Tracker
# API Used: Pixela - https://pixe.la (Free, No Key Needed)

import requests
from datetime import datetime

USERNAME = "virarboy123"  # Change to your unique username
TOKEN = "mysecret123"     # Change to your secret token
GRAPH_ID = "graph1"       # Your habit graph id

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}

def create_user():
    params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=params)
    print("Create User:", response.text)

def create_graph():
    graph_config = {
        "id": GRAPH_ID,
        "name": "Coding Habit",
        "unit": "hours",
        "type": "float",
        "color": "green"
    }
    response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
    print("Create Graph:", response.text)

def add_pixel():
    today = datetime.now().strftime("%Y%m%d")
    quantity = input("How many hours did you code today? ")

    pixel_data = {
        "date": today,
        "quantity": quantity,
    }
    response = requests.post(url=PIXEL_ENDPOINT, json=pixel_data, headers=headers)
    print("Add Pixel:", response.text)
    print(f"\nCheck your graph here: https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html")

def update_pixel():
    date = input("Enter date to update (YYYYMMDD): ")
    quantity = input("New hours: ")
    pixel_data = {"quantity": quantity}
    response = requests.put(url=f"{PIXEL_ENDPOINT}/{date}", json=pixel_data, headers=headers)
    print("Update Pixel:", response.text)

def delete_pixel():
    date = input("Enter date to delete (YYYYMMDD): ")
    response = requests.delete(url=f"{PIXEL_ENDPOINT}/{date}", headers=headers)
    print("Delete Pixel:", response.text)

def main():
    print("=== Day 37 - Habit Tracker ===")
    print("1. Create User (Run Only First Time)")
    print("2. Create Graph (Run Only First Time)")
    print("3. Add Today's Habit")
    print("4. Update Habit")
    print("5. Delete Habit")

    choice = input("\nChoose (1-5): ")

    if choice == "1":
        create_user()
    elif choice == "2":
        create_graph()
    elif choice == "3":
        add_pixel()
    elif choice == "4":
        update_pixel()
    elif choice == "5":
        delete_pixel()
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()