# Day 2 - Tip Calculator
print("Welcome to the Tip Calculator!")

# Inputs
Bill = float(input("what was the total Bill? $"))
tip = int(input("What Percentage tip would you like to give? 10, 12, or 15? "))
People = int(input("How many people tosplit the bill? "))

# Calculation
Tip_Percent = tip / 100
Total_Tip = Bill * Tip_Percent
Total_Bill = Bill + Total_Tip
Bill_Per_Person = Total_Bill / People
Final_Amount = round(Bill_Per_Person, 2)

# Output
print(f"Each Person should pay: ${Final_Amount}")