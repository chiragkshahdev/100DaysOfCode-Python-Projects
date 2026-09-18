# Day 13 - Debugging Exercise

This day is all about finding and fixing bugs.

## 🐞 Bugs Fixed

**1. Odd / Even Cheker**
- Bug: 'if number % 2 == 0:' used '=' instead of '=='
- Fix: Changed to '=='

**2. Leap Year**
- Bug: Missing 'else' conditions and wrong print
- Fix: Correct nested 'if-else' Logic
    - Divisible by 4 -> Leap
    - But if divisible by 100 -> Not Leap
    - Unless also divisible by 400 -> Leap

**3. FizzBuzz**
- Bug: 'for number in range(1,100)' should be 101, 'FizzBuzz' condition at last
- Fix:
    - Range '1 to 101'
    - Check 'FizzBuzz' (3 and 5) FIRST, then Fizz, then Buzz

## 🧠 Debugging Steps Learned
1. Describes the problem
2. Reproduce the bug
3. play computer - run code manually
4. Fix the error
5. Use print() statement
6. Use a Debugger

## ▶️ Run