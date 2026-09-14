import tkinter as tk
import random
from collections import deque

WIDTH, HEIGHT = 21, 21
CELL_SIZE = 25

class MazeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Day_006 - Escaping The Maze")
        self.maze = self.create_maze(WIDTH, HEIGHT)
        self.player = [1, 0]
        self.end = [WIDTH-2, HEIGHT-1]

        self.canvas = tk.Canvas(root, width=WIDTH*CELL_SIZE, height=HEIGHT*CELL_SIZE, bg="white")
        self.canvas.pack()

        self.draw_maze()
        self.root.bind("<KeyPress>", self.move_player)

        tk.Label(root, text="Use WASD / Arrow Keys to reach E from S", font=("Arial", 10)).pack(pady=5)

    def create_maze(self, width, height):
        maze = [[1 for _ in range(width)] for _ in range(height)]
        stack = [(0, 0)]
        maze[0][0] = 0
        while stack:
            x, y = stack[-1]
            neighbors = []
            for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                    neighbors.append((nx, ny, x + dx//2, y + dy//2))
            if neighbors:
                nx, ny, wx, wy = random.choice(neighbors)
                maze[wy][wx] = 0
                maze[ny][nx] = 0
                stack.append((nx, ny))
            else:
                stack.pop()
        maze[0][1] = 0
        maze[height-1][width-2] = 0
        return maze

    def draw_maze(self):
        self.canvas.delete("all")
        for y in range(HEIGHT):
            for x in range(WIDTH):
                x1, y1 = x*CELL_SIZE, y*CELL_SIZE
                x2, y2 = x1+CELL_SIZE, y1+CELL_SIZE
                if self.maze[y][x] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="#2c3e50", outline="")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="#ecf0f1")

        # Start & End
        self.canvas.create_rectangle(1*CELL_SIZE, 0*CELL_SIZE, 2*CELL_SIZE, 1*CELL_SIZE, fill="#2ecc71")
        self.canvas.create_text(1.5*CELL_SIZE, 0.5*CELL_SIZE, text="S", font=("bold", 12))
        self.canvas.create_rectangle(self.end[0]*CELL_SIZE, self.end[1]*CELL_SIZE, (self.end[0]+1)*CELL_SIZE, (self.end[1]+1)*CELL_SIZE, fill="#e74c3c")
        self.canvas.create_text((self.end[0]+0.5)*CELL_SIZE, (self.end[1]+0.5)*CELL_SIZE, text="E", font=("bold", 12), fill="white")

        # Player
        self.canvas.create_oval(self.player[0]*CELL_SIZE+5, self.player[1]*CELL_SIZE+5,
                                (self.player[0]+1)*CELL_SIZE-5, (self.player[1]+1)*CELL_SIZE-5,
                                fill="#3498db", outline="")

    def move_player(self, event):
        key = event.keysym.lower()
        nx, ny = self.player[0], self.player[1]
        if key in ['w', 'up']: ny -= 1
        elif key in ['s', 'down']: ny += 1
        elif key in ['a', 'left']: nx -= 1
        elif key in ['d', 'right']: nx += 1
        else: return

        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and self.maze[ny][nx] == 0:
            self.player = [nx, ny]
            self.draw_maze()
            if self.player == self.end:
                self.canvas.create_text(WIDTH*CELL_SIZE//2, HEIGHT*CELL_SIZE//2, text="YOU ESCAPED! 🎉", font=("Arial", 24, "bold"), fill="black", tags="win")
                self.root.after(100, lambda: self.root.bell())

if __name__ == "__main__":
    root = tk.Tk()
    game = MazeGame(root)
    root.mainloop()