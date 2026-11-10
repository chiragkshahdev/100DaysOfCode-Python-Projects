import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn = {}

# ---------------------------- DATA ---------------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")

# ---------------------------- FUNCTIONS ---------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, fill="white")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, fill="#91C2AF")

def is_known():
    words_to_learn.remove(current_card)
    data = pd.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ---------------------------- #
window = tk.Tk()
window.title("Flash Card App - Learn French")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_rectangle(20, 20, 780, 506, fill="white", outline="")
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons with Text instead of Images
unknown_button = tk.Button(text="❌ DON'T KNOW", font=("Arial", 16, "bold"), bg="#FF6B6B", fg="white", width=18, command=next_card)
unknown_button.grid(row=1, column=0, pady=20)

known_button = tk.Button(text="✅ I KNOW", font=("Arial", 16, "bold"), bg="#51CF66", fg="white", width=18, command=is_known)
known_button.grid(row=1, column=1, pady=20)

next_card()

window.mainloop()