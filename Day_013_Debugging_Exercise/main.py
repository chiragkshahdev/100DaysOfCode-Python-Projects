# Day 013 - Debugging Exercise
# 100 Days of Code Python

# Exercise 1: Odd or Even
print("--- Exercise 1: Odd / Even ---")
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")   

# Exercise 2: Leap Year
print("\n--- Exercise 2: Leap Year ---")
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not Leap Year.")

# Exercise 3: FizzBuzz
print("\n--- Exercise 3: FizzBuzz ---")
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)    