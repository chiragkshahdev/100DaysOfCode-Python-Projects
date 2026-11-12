# 53. Data Entry Automation

Automate repetitive manual data entry work using Python.
This project reads data from CSV / Excel, cleans it, validates it,
removes duplicates, and automatically saves it to a Database + Excel file.

## Features
- Load data from `.csv` / `.xlsx`
- Auto clean column names
- Remove empty rows & duplicates
- Validate Name, Email, Phone
- Save invalid rows separately for review
- Save cleaned data to SQLite Database + Excel
- Auto log file for every run

## Project Structure
53-data-entry-automation/
├── main.py
├── data.csv
├── README.md
├── requirements.txt
├── database.db (auto-created)
├── output_cleaned.xlsx (auto-created)
├── invalid_rows.csv (auto-created)
└── automation_log.txt (auto-created)

## Installation
pip install pandas openpyxl

## Sample data.csv
name,email,phone,age
Rahul Sharma,rahul@gmail.com,9876543210,21
Priya Singh,priya@gmail.com,9123456780,20

## How to Run
python main.py

## Run with Custom File
python main.py --input mydata.xlsx

## Output
- `database.db` -> Table: `entries`
- `output_cleaned.xlsx` -> Cleaned data
- `invalid_rows.csv` -> Rejected rows
- `automation_log.txt` -> Full automation log

## Future Scope
- Auto-fill Google Forms / Web Forms using Selenium
- OCR from scanned documents
- Email notification after automation
- GUI using Tkinter