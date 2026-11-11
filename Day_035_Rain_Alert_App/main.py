# Day 35 - Rain Alert App
# API Used: Open-Meteo (Free, No API Key Needed)
# City: Virar, Maharashtra - You can change lat/lon for your city

import requests

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,precipitation,weather_code,wind_speed_10m&hourly=precipitation_probability&forecast_days=1"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print("API Error:", e)
        return None

def check_rain():
    print("=== Rain Alert App ===")
    print("Checking weather for Virar, Maharashtra...\n")

    # Virar Coordinates
    lat = 19.47
    lon = 72.80

    data = get_weather(lat, lon)

    if not data:
        print("Could not fetch weather. Check your internet.")
        return

    current = data["current"]
    temp = current["temperature_2m"]
    rain = current["precipitation"]
    code = current["weather_code"]
    wind = current["wind_speed_10m"]
    rain_chance = data["hourly"]["precipitation_probability"][0]

    print(f"Temperature: {temp}°C")
    print(f"Precipitation: {rain} mm")
    print(f"Rain Chance: {rain_chance}%")
    print(f"Wind Speed: {wind} km/h")
    print(f"Weather Code: {code}\n")

    # Rain Alert Logic
    if rain > 0 or rain_chance > 50 or code in [51, 53, 55, 61, 63, 65, 80, 81, 82]:
        print("ALERT: It is Raining / Rain Expected!")
        print("Advice: Take Umbrella / Raincoat. Don't forget!")
    elif rain_chance > 20:
        print("WARNING: Light Rain Possible Today.")
        print("Advice: Keep Umbrella with you.")
    else:
        print("NO RAIN: Weather is Clear.")
        print("Advice: No need for Umbrella. Enjoy your day!")

if __name__ == "__main__":
    check_rain()