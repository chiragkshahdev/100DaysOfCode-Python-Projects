# Day 25 - U.S. States Game

An educational geography game built with Python Turtle & Pandas.

## How to Play
1. A blank US map appears
2. Popup asks "What's another state's name?"
3. Type a state name (e.g. Texas)
4. If correct, name appears on map at its location
5. Type "Exit" to quit and generate states_to_learn.csv

## Features
- 50 states with x,y coordinates
- Real-time score: 0/50, 1/50...
- Writes correct guess on map using turtle.write()
- Creates CSV of missing states to study
- Case-insensitive using .title()

## Concepts Used
- Pandas: read_csv(), to_list(), DataFrame, filtering data[data.state == answer]
- Turtle: Screen, textinput(), goto(), write()
- List Comprehension: [state for state in all_states if state not in guessed_states]
- File Handling

## Requirements
pip install pandas

## How to Run
python main.py

Author: Chirag Kiran Shah - FYBScIT A
Day 25 / 100 Days of Code