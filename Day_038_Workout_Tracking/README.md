# Day 38 - Workout Tracking (No API Key Version)

No API Key Needed. Works Offline.

## Features
- Type any exercise in plain English
- Auto Calorie Calculation (approx per minute)
- Saves to workouts.csv (like Google Sheet)
- Shows Total Minutes and Total Calories
- Multiple entries in one run

## How to Run
1. Run the app:
   python main.py

2. Type:
   Exercise: running
   Minutes: 30

3. Type exit to stop

## Output Example
workouts.csv file will be created:
Date | Time | Exercise | Duration (min) | Calories
11/11/2026 | 10:00:00 | Running | 30 | 300

## Tech Used
- Python
- CSV Module
- Datetime

## Note
This version uses average calorie values.
API version uses Nutritionix for exact calories.
For learning and Day 38 completion, this version is perfect.