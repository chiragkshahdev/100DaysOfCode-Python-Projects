# Day 20 - Snake Game Part 1 | Python

A classic Snake Game built using Python Turtle module.
This is Part 1 of the build.

### What I Learned in Part 1
- Screen setup with `turtle.Screen()`
- How to use `screen.tracer(0)` for smooth animation
- OOP concept - Creating a Snake class
- How to make the snake move as a chain

### How Part 1 Works
1. We create 3 white squares as the snake's body.
2. The last segment moves to the second-last's position, and so on.
3. The head moves forward by 20px.
4. Arrow keys control the direction.

### How to Run
```bash
python Main.py