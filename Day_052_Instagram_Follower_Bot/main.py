"""
Day 52 - Instagram Follower Tracker (Safe Version)
No Selenium, No Instagram Login, No Auto Follow.
This only tracks your followers manually and gives growth ideas.
Uses only Python Standard Library.
"""

import csv
from datetime import datetime

print("="*50)
print("INSTAGRAM FOLLOWER TRACKER - SAFE VERSION")
print("="*50)

# 1. Aaj ka data daalo
username = input("Your Instagram username: ")
followers = input("How many followers do you have today? : ")
following = input("How many accounts are you following? : ")
posts = input("Total posts? : ")

# 2. Growth Idea nikalna
print("\n--- Your Daily Growth Plan ---")

try:
    followers = int(followers)
    following = int(following)
    posts = int(posts)

    if posts == 0:
        print("⚠️ First make 3-4 Reels and post them, without posts followers won't increase.")
    elif followers < 100:
        print("Tip 1: Everyday 1 Reel post - Trending audio use it")
        print("Tip 2: Make a 10 big Comment list - comment on 10 posts daily")
        print("Tip 3: Write Bio Clearly - What are you Doing")
    elif followers < 1000:
        print("Tip 1: Every Week  4 Reels + 2 Carousel post on Instagram")
        print("Tip 2: Collab Reel make it - small creator collab with them")
        print("Tip 3: Add Story daily poll / Q&A - Engage with audience")
    else:
        print("Tip 1: Make Consistency, Everyweek 5 posts")
        print("Tip 2: Make a Viral Reels on Pin")
        print("Tip 3: Make a Broadcast Channel on Telegram - Share your content there")

    # Follow Ratio
    ratio = round(followers / max(1, following), 2)
    print(f"\nYour Follow Ratio: {ratio} (if it is high from 1 then it is good, if it is low then you need to improve your content)")

    # 3. CSV me save karo - History ke liye
    with open("followers.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), username, followers, following, posts, ratio])

    print("\nSaved to followers.csv")
    print("Come Tomorrow and put your Data, Your Growth Graph will be ready.")

except:
    print("put your Numbers correctly!")

print("\nBot has not followed anyone with auto-follow. Your account is 100% Safe.")