import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game - Day 25")
screen.setup(width=725, height=491)

# If you have the image - uncomment these 2 lines
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

# If you DON'T have image, use this background
screen.bgcolor("#e6f7ff")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (Type Exit to quit)"
    )

    if answer_state is None:
        break

    answer_state = answer_state.title()

    if answer_state == "Exit":
        # Create csv of missing states to learn
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print("states_to_learn.csv created!")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))

# screen.exitonclick()