# Day 51 - Twitter Complaint Bot (Safe Version)

A simple tool to generate professional Twitter complaints. This bot DOES NOT auto-post tweets.

It only creates a complaint draft and saves it to a CSV file. User will copy and post manually to keep account safe.

## Features
- Generates professional complaint in Twitter format
- Auto adds Company tag and Support tag
- Checks 280 character limit
- Saves all complaints to `complaints.csv` with date and time
- No Twitter API, No Selenium, No Login

## Requirements
- Python 3
- No extra library needed
- No Pip Install

## How To Use
1. Run the program:
```bash
py main.py