# Day 32 - Birthday Wisher

## 📌 Project Overview
An automated Birthday Wisher that checks a CSV file every day. If today is someone's birthday, it automatically picks a random birthday letter and sends it via email.

No more forgetting birthdays!

## 🎯 What I Learned
- `datetime` - Getting current month and day
- `pandas` - Reading CSV and creating Dictionary with Iterrows
- `smtplib` - Sending emails using Gmail SMTP
- `random` - Picking a random letter template
- String Replacement - Replacing `[NAME]` with actual name

## 🚀 How To Run
```bash
cd Day_032_Birthday_Wisher
python main.py