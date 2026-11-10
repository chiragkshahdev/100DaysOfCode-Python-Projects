import pandas as pd
import datetime as dt

today = (dt.datetime.now().month, dt.datetime.now().day)
print(f"Today is: {today} - Month, Day")

data = pd.read_csv("birthdays.csv")
print(data)

birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}
print(f"Birthdays in file: {list(birthdays_dict.keys())}")

if today in birthdays_dict:
    print("FOUND! Birthday is Today!")
else:
    print("NOT FOUND - Date match not found in the birthdays file.")