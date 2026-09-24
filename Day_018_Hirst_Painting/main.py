import turtle as t
import random

# Hirst ke famous colors
color_list = [
    (222, 16, 33), (230, 229, 22), (35, 94, 167), (198, 12, 85),
    (48, 201, 233), (248, 158, 16), (27, 159, 70), (238, 24, 33),
    (19, 125, 72), (248, 222, 22), (44, 57, 139), (240, 146, 178),
    (19, 20, 18), (236, 239, 243)
]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Starting position set karo
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()