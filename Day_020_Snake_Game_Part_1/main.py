from turtle import Screen
from snake import Snake
import time

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Day 20 - Snake Game Part 1")
screen.tracer(0) # Turns off animation for smooth movement

snake = Snake()

# Controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game Loop - Part 1
game_is_on = True
while game_is_on:
    screen.update() # Updates the screen after all segments move
    time.sleep(0.1) # Controls snake speed
    snake.move()

screen.exitonclick()