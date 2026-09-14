# Day 006 - Escaping The Maze

A playable maze game made in Python (Tkinter) as part of 100 Days of Code.

### 🎮 Game Description
A random maze is generated every time you run the game. You start at `S` (green) and need to find your way to `E` (red).

### 🕹️ How to Play
- Run the game: `python main.py`
- Controls:
    - `W` or `Up Arrow` = Move Up
    - `S` or `Down Arrow` = Move Down
    - `A` or `Left Arrow` = Move Left
    - `D` or `Right Arrow` = Move Right

### 🧠 How it Works
- Maze Generation: Randomized Depth-First Search (DFS) algorithm
- Player Movement: Collision detection with walls
- Win Condition: Reach the End point (E)

### 📁 Files
- `main.py` - Main game logic
- `README.md` - Project info

### 🚀 Future Improvements
- Add timer and step counter
- Add BFS auto-solver (press 'H' for hint)
- Add multiple levels

Made with ❤️ for Day 6 Challenge