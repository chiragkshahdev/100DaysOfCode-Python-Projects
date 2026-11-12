# 53. Data Entry Automation - Fixed Version (Error Free)
# CSV / Excel -> Clean + Validate -> SQLite + Excel

import os
import sqlite3
import argparse
from datetime import datetime

import pandas as pd

INPUT_FILE = "data.csv"
OUTPUT_EXCEL = "output_cleaned.xlsx"
DB_FILE = "database.db"
LOG_FILE = "automation_log.txt"
INVALID_FILE = "invalid_rows.csv"

def log(message):
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")

    # FIX 1: dtype=str -> phone/email kabhi int/NaN nahi banega
    # FIX 2: keep_default_na=False -> khali cell "" rahega, NaN nahi
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path, dtype=str, keep_default_na=False)
    elif file_path.endswith((".xlsx", ".xls")):
        df = pd.read_excel(file_path, dtype=str, keep_default_na=False)
        df = df.fillna("")
    else:
        raise ValueError("Only .csv / .xlsx files supported")

    log(f"Loaded {len(df)} rows from {file_path}")
    return df

def clean_and_validate(df):
    # Column names clean karo
    df.columns = [str(c).strip().lower().replace(" ", "_") for c in df.columns]

    # Fully empty rows hatao
    df = df[df.apply(lambda row: "".join(row.astype(str)).strip() != "", axis=1)]

    # Duplicates hatao
    before = len(df)
    df = df.drop_duplicates()
    log(f"Removed {before - len(df)} duplicate rows")

    valid_rows = []
    invalid_rows = []

    for _, row in df.iterrows():
        name = str(row.get("name", "")).strip()
        email = str(row.get("email", "")).strip()
        # FIX 3: Phone se space / .0 / +91 hatao, sirf digits rakho
        phone = str(row.get("phone", "")).strip()
        phone = phone.replace(".0", "").replace("+91", "").replace(" ", "").replace("-", "")

        if not name:
            invalid_rows.append(row)
            continue
        if "@" not in email or "." not in email:
            invalid_rows.append(row)
            continue
        if not phone.isdigit() or len(phone) < 10:
            invalid_rows.append(row)
            continue

        # Cleaned phone wapas save karo
        row = row.copy()
        row["phone"] = phone
        valid_rows.append(row)

    clean_df = pd.DataFrame(valid_rows)
    log(f"Valid: {len(clean_df)} | Invalid: {len(invalid_rows)}")

    if invalid_rows:
        pd.DataFrame(invalid_rows).to_csv(INVALID_FILE, index=False)
        log(f"Invalid rows saved to {INVALID_FILE}")

    return clean_df

def save_to_database(df):
    conn = sqlite3.connect(DB_FILE)
    df.to_sql("entries", conn, if_exists="replace", index=False)
    conn.close()
    log(f"Saved {len(df)} rows to {DB_FILE} -> table: entries")

def save_to_excel(df):
    df.to_excel(OUTPUT_EXCEL, index=False)
    log(f"Saved cleaned data to {OUTPUT_EXCEL}")

def automate_entry(input_file=INPUT_FILE):
    # Purana log clear karo taaki har baar fresh log bane
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    log("=== Data Entry Automation Started ===")
    df = load_data(input_file)
    clean_df = clean_and_validate(df)

    if clean_df.empty:
        log("No valid data to save. Exiting.")
        return

    save_to_database(clean_df)
    save_to_excel(clean_df)
    log("=== Automation Completed Successfully ===")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Entry Automation")
    parser.add_argument("--input", default=INPUT_FILE, help="Input CSV/Excel file")
    args = parser.parse_args()

    try:
        automate_entry(args.input)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        print("Solution: data.csv ko main.py ke saath wale folder me rakho")
    except Exception as e:
        print(f"ERROR: {e}")