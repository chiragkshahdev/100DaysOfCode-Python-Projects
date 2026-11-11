# Day 38 - Workout Tracking (No API Key Version)
# No Nutritionix, No Sheety - Works Offline, Saves to CSV

import csv
import os
from datetime import datetime

FILE_NAME = "workouts.csv"

# Calories burned per minute (approx) for average 65kg person
CALORIES_PER_MIN = {
    "running": 10,
    "walking": 4,
    "cycling": 8,
    "pushups": 7,
    "pullups": 8,
    "squats": 6,
    "yoga": 3,
    "gym": 6,
    "swimming": 9,
    "skipping": 11,
    "plank": 4,
    "dance": 6
}

def get_calories(exercise, duration):
    exercise = exercise.lower().strip()
    # Find closest match
    for key in CALORIES_PER_MIN:
        if key in exercise:
            return CALORIES_PER_MIN[key] * duration
    # Default if exercise not in list
    return 5 * duration

def save_to_csv(date, time, exercise, duration, calories):
    file_exists = os.path.exists(FILE_NAME)
    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Time", "Exercise", "Duration (min)", "Calories"])
        writer.writerow([date, time, exercise.title(), duration, calories])

def show_total():
    if not os.path.exists(FILE_NAME):
        return
    total_cal = 0
    total_min = 0
    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_cal += int(row["Calories"])
            total_min += int(row["Duration (min)"])
    print(f"\nTotal Till Now: {total_min} min | {total_cal} Calories Burned")

def main():
    print("=== Day 38 - Workout Tracking (No API) ===")
    print("Examples: running, walking, cycling, pushups, yoga, gym")
    print("Type 'exit' to stop\n")

    while True:
        exercise = input("What exercise did you do? ")
        if exercise.lower() == "exit":
            break

        try:
            duration = int(input("How many minutes? "))
        except:
            print("Please enter number for minutes\n")
            continue

        calories = get_calories(exercise, duration)

        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")

        save_to_csv(date, time, exercise, duration, calories)

        print(f"\nSaved! {exercise.title()} - {duration} min - {calories} kcal")
        print(f"Saved in workouts.csv file\n")

    show_total()
    print("\nDone! Open workouts.csv to see your Google Sheet style data.")

if __name__ == "__main__":
    main()