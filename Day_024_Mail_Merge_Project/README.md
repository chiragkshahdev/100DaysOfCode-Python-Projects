# Day 24 - Mail Merge Project

Automated letter generator using Python File Handling.

## What it Does
- Reads names from invited_names.txt
- Reads a template letter with [name] placeholder
- Creates personalized letter for each name
- Saves all letters to Output/ReadyToSend/

## Concepts Used
- File Handling: open(), read(), readlines(), write()
- String Methods: strip(), replace()
- Relative File Paths:./Input/...
- For Loops

## How to Run
1. Create folder structure as given
2. Add names to invited_names.txt (one per line)
3. Edit starting_letter.txt with [name] placeholder
4. Run: python main.py
5. Check Output/ReadyToSend/

## Key Learning
- `strip()` removes \n from names
- `replace()` replaces placeholder
- Using `with open()` automatically closes files

Author: Chetag Kiran Shah - FYBScIT A - Roll 08
Day 24 / 100 Days of Code - Python