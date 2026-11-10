# Day 33 - ISS Overhead Notifier 🛰️

## 📌 Project Overview
An automated notifier that tells you when the International Space Station (ISS) is flying directly overhead AND it's dark outside, so you can actually go out and see it!

It checks the ISS position every 60 seconds and sends you an email when the conditions are perfect.

## 🎯 What I Learned
- **API Requests** - Using `requests` to get live data from ISS API
- **Sunrise-Sunset API** - Getting sunrise and sunset time for any location
- **SMTP** - Sending email alerts automatically
- **While Loop** - Running code continuously with `time.sleep(60)`
- **Error Handling** - Using `try/except` and `raise_for_status()`

## 🚀 How To Run
```bash
cd Day_033_ISS_Overhead_Notifier
pip install requests
python main.py