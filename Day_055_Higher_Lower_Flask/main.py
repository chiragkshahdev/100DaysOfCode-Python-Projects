from flask import Flask
import random

app = Flask(__name__)

# Generate a random number between 0 and 9
random_number = random.randint(0, 9)
print(f"Correct Number is: {random_number}")

@app.route("/")
def home():
    return """
    <h1>Guess a number between 0 and 9</h1>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC0/giphy.gif" width="400">
    <p>Enter your guess in the URL like this:</p>
    <p><b>/3</b> &nbsp; Example: http://127.0.0.1:5000/3</p>
    """

@app.route("/<int:guess>")
def guess_number(guess):
    if guess < random_number:
        return """
        <h1 style='color:red'>Too Low, Try Again!</h1>
        <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="400">
        """
    elif guess > random_number:
        return """
        <h1 style='color:purple'>Too High, Try Again!</h1>
        <img src="https://media.giphy.com/media/3o6ZtaO9U2gQQsYc9m/giphy.gif" width="400">
        """
    else:
        return """
        <h1 style='color:green'>You Found Me!</h1>
        <img src="https://media.giphy.com/media/4T7e4DmPJ2P9O/giphy.gif" width="400">
        """

if __name__ == "__main__":
    app.run(debug=True)