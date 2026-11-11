"""
Day 49 - LinkedIn Job Finder (No Selenium Version)
Uses only Python Standard Library.
No pip install, No login, No auto-apply.
100% Safe for LinkedIn account.
"""

import urllib.request
import re
import csv
import webbrowser

# 1. Kya job chahiye?
JOB_KEYWORD = "Python Developer"
LOCATION = "India"

# LinkedIn ka public job search link (login ke bina khulta hai)
search_url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={JOB_KEYWORD.replace(' ', '%20')}&location={LOCATION}"

print(f"Searching jobs for: {JOB_KEYWORD} in {LOCATION}...")
print("Please wait...")

# 2. Browser me bhi khol do taaki tu dekh sake
webbrowser.open(f"https://www.linkedin.com/jobs/search/?keywords={JOB_KEYWORD.replace(' ', '%20')}&location={LOCATION}")

# 3. Data mangao - bina login ke
headers = {'User-Agent': 'Mozilla/5.0'}
request = urllib.request.Request(search_url, headers=headers)

try:
    with urllib.request.urlopen(request) as response:
        html = response.read().decode('utf-8')
except Exception as e:
    print("Internet error, browser me check kar le.")
    html = ""

# 4. Title aur Company nikal lo
titles = re.findall(r'job-card-list__title.*?>(.*?)<', html)
companies = re.findall(r'job-card-container__company-name.*?>(.*?)<', html)
links = re.findall(r'data-tracking-control-name="public_jobs_jobrecommendations" href="(.*?)"', html)

# Saaf karo
titles = [t.strip() for t in titles if t.strip()]
companies = [c.strip() for c in companies if c.strip()]

print(f"Found {len(titles)} jobs. Saving to jobs.csv...")

# 5. CSV me save karo
with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Job Title", "Company", "Location", "Link"])

    for i in range(min(len(titles), len(companies))):
        link = links[i] if i < len(links) else "Check in browser"
        writer.writerow([titles[i], companies[i], LOCATION, link])
        print(f"Saved: {titles[i]} - {companies[i]}")

print("Done! jobs.csv check kar. Ab manual apply kar.")