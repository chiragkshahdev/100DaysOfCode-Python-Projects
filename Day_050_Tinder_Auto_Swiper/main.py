"""
Day 50 - Tinder Auto Swiper (Safe Simulator Version)
No Selenium, No Login, No Auto Swipe on Real Tinder.
This is a UI Demo to learn swipe logic.
Uses only Python Standard Library - tkinter
"""

import tkinter as tk
import csv

# Dummy Profiles - Real Tinder se data nahi le rahe
profiles = [
    {"name": "Priya, 22", "bio": "Love travelling & Coffee", "interest": "Photography"},
    {"name": "Rahul, 24", "bio": "Python Developer | Gym", "interest": "Coding"},
    {"name": "Sneha, 21", "bio": "Music + Movies", "interest": "Singing"},
    {"name": "Aman, 23", "bio": "BSc IT Student", "interest": "Gaming"},
    {"name": "Ishita, 22", "bio": "Foodie | Reader", "interest": "Books"},
]

current = 0
liked = []

root = tk.Tk()
root.title("Tinder Swiper - Demo")
root.geometry("350x500")
root.configure(bg="#ff4458")

title_label = tk.Label(root, text="TINDER DEMO", font=("Arial", 18, "bold"), bg="#ff4458", fg="white")
title_label.pack(pady=20)

# Card
card_frame = tk.Frame(root, bg="white", width=280, height=280)
card_frame.pack(pady=10)
card_frame.pack_propagate(False)

name_label = tk.Label(card_frame, text="", font=("Arial", 16, "bold"), bg="white")
name_label.pack(pady=20)

bio_label = tk.Label(card_frame, text="", font=("Arial", 12), bg="white", wraplength=240)
bio_label.pack(pady=10)

interest_label = tk.Label(card_frame, text="", font=("Arial", 11), bg="white", fg="#ff4458")
interest_label.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#ff4458", fg="white")
status_label.pack(pady=10)

def show_profile():
    if current < len(profiles):
        p = profiles[current]
        name_label.config(text=p["name"])
        bio_label.config(text=p["bio"])
        interest_label.config(text=f"Interest: {p['interest']}")
        status_label.config(text=f"Profile {current+1} / {len(profiles)}")
    else:
        name_label.config(text="No More Profiles!")
        bio_label.config(text="You have seen all profiles.")
        interest_label.config(text="")
        save_liked()

def swipe_right():
    global current
    if current < len(profiles):
        liked.append(profiles[current])
        status_label.config(text=f"LIKED ❤️ {profiles[current]['name']}")
        current += 1
        root.after(500, show_profile)

def swipe_left():
    global current
    if current < len(profiles):
        status_label.config(text=f"PASSED ❌ {profiles[current]['name']}")
        current += 1
        root.after(500, show_profile)

def save_liked():
    with open("liked.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Bio", "Interest"])
        for p in liked:
            writer.writerow([p["name"], p["bio"], p["interest"]])
    print(f"Saved {len(liked)} liked profiles to liked.csv")

# Buttons
btn_frame = tk.Frame(root, bg="#ff4458")
btn_frame.pack(pady=20)

left_btn = tk.Button(btn_frame, text="❌ PASS", font=("Arial", 14, "bold"), bg="white", fg="red", width=10, command=swipe_left)
left_btn.grid(row=0, column=0, padx=10)

right_btn = tk.Button(btn_frame, text="❤️ LIKE", font=("Arial", 14, "bold"), bg="white", fg="green", width=10, command=swipe_right)
right_btn.grid(row=0, column=1, padx=10)

show_profile()
root.mainloop()