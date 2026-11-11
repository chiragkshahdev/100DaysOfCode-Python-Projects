"""
Day 51 - Twitter Complaint Bot (Safe Version)
No Selenium, No Twitter API, No Auto Post.
This bot only generates a professional complaint draft.
User will copy and post manually. 100% Safe.
Uses only Python Standard Library.
"""

import csv
from datetime import datetime

print("="*50)
print("TWITTER COMPLAINT BOT - SAFE VERSION")
print("="*50)

# 1. User se details lo
company = input("What is the company name? (ex: Jio, Zomato, Flipkart): ")
issue = input("What is the Problem? (ex: order has not come Yet, Network is not working): ")
order_id = input("Order ID / Account No. (If it is there or click Enter): ")
name = input("What is your name? (ex: John Doe): ")

# 2. Professional Complaint banao
if order_id:
    complaint = f"Hi @{company}, I am facing issue: {issue}. My Order ID is {order_id}. Please resolve this ASAP. I have been waiting for long. @{company}Support please help. #{company} #CustomerComplaint"
else:
    complaint = f"Hi @{company}, I am facing issue: {issue}. Please resolve this ASAP. I have been waiting for long. @{company}Support please help. #{company} #CustomerComplaint"

# 3. Twitter ka 280 character check
print("\n--- Tera Complaint Draft ---")
print(complaint)
print(f"\nCharacters: {len(complaint)} / 280")

if len(complaint) > 280:
    print("⚠️ Tweet is too long, please make it shorter.")
else:
    print("✅ Perfect! Tweet is Ready.")

# 4. CSV me save karo - Proof ke liye
with open("complaints.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), company, issue, order_id, name, complaint])

print("\nSaved to complaints.csv")
print("\nTake a screenshot for proof.")
print("Bot has generated a professional complaint draft.")