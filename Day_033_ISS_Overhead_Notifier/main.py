import requests
from datetime import datetime
import smtplib
import time

# Your Location - Virar, Maharashtra
MY_LAT = 19.4554  # Your latitude
MY_LONG = 72.8112  # Your longitude

# Your Email Details
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"  # Use Gmail App Password, not normal password

def is_iss_overhead():
    """Check if ISS is within +/- 5 degrees of my position."""
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        print(f"ISS Position: Lat {iss_latitude}, Long {iss_longitude}")

        # If ISS is within 5 degrees of my position
        if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error fetching ISS position: {e}")
        return False

def is_night():
    """Check if it is currently dark at my location."""
    try:
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()

        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now().hour

        print(f"Sunrise: {sunrise}, Sunset: {sunset}, Now: {time_now}")

        # If it's night time
        if time_now >= sunset or time_now <= sunrise:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error fetching sunrise/sunset: {e}")
        return False

# ---------------------------- MAIN LOOP ---------------------------- #
print("ISS Notifier Started... Looking for ISS overhead...")

while True:
    time.sleep(5)  # Check every 60 seconds

    if is_iss_overhead() and is_night():
        print("ISS IS OVERHEAD AND IT'S NIGHT! Sending email...")

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Look Up! 🛰️ ISS is Overhead!\n\nThe ISS is above you in the sky. Go outside and look up!"
            )
        print("Email Sent!")
    else:
        print("ISS not overhead or it's daytime. Waiting...")