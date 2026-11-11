# Day 35 - Rain Alert App

A simple Python App that checks live weather and gives Rain Alert.

## Features
- Live Weather from Open-Meteo API
- Shows Temperature, Rain Chance, Wind Speed
- Gives Alert: Rain / No Rain / Light Rain Possible
- Umbrella Advice

## API Used
https://api.open-meteo.com/v1/forecast

No API Key Required.

## How to Run
1. Install requests:
   pip install requests

2. Run the app:
   python main.py

## Tech Used
- Python
- Requests Library
- Open-Meteo API

## Change City
Change lat and lon in main.py for your city.
Virar: lat = 19.47, lon = 72.80
Mumbai: lat = 19.07, lon = 72.87
Delhi: lat = 28.61, lon = 77.20