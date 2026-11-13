from flask import Flask, render_template_string, redirect, url_for
import random

app = Flask(__name__)

# Sample dog profiles
dogs = [
    {"name": "Bruno", "age": 2, "breed": "Labrador", "bio": "Loves long walks and treats.", "image": "https://images.dog.ceo/breeds/labrador/n02099712_3868.jpg", "likes": 0},
    {"name": "Bella", "age": 3, "breed": "Pomeranian", "bio": "Queen of the park. Loves cuddles.", "image": "https://images.dog.ceo/breeds/pomeranian/n02112137_14112.jpg", "likes": 0},
    {"name": "Max", "age": 1, "breed": "Beagle", "bio": "Professional food thief.", "image": "https://images.dog.ceo/breeds/beagle/n02088364_11136.jpg", "likes": 0},
    {"name": "Coco", "age": 4, "breed": "Poodle", "bio": "Fashion icon. Hates rain.", "image": "https://images.dog.ceo/breeds/poodle-standard/n02113799_2287.jpg", "likes": 0},
]

current_index = 0
matches = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Tinder for Dogs</title>
    <style>
        body { font-family: Arial; text-align: center; background: #ffefef; }
        .card { background: white; width: 320px; margin: 20px auto; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        img { width: 100%; border-radius: 12px; height: 300px; object-fit: cover; }
        .btn { padding: 12px 25px; font-size: 18px; border: none; border-radius: 50px; cursor: pointer; margin: 10px; }
        .like { background: #ff4d6d; color: white; }
        .pass { background: #ddd; }
    </style>
</head>
<body>
    <h1>🐶 Tinder for Dogs</h1>
    <p>Matches: {{ matches }} | Dogs Left: {{ left }}</p>
    {% if dog %}
    <div class="card">
        <img src="{{ dog.image }}" alt="{{ dog.name }}">
        <h2>{{ dog.name }}, {{ dog.age }}</h2>
        <p><b>{{ dog.breed }}</b></p>
        <p>{{ dog.bio }}</p>
        <a href="/like"><button class="btn like">❤️ Like</button></a>
        <a href="/pass"><button class="btn pass">❌ Pass</button></a>
    </div>
    {% else %}
    <h2>No more dogs! Come back tomorrow.</h2>
    <a href="/reset"><button class="btn like">Start Again</button></a>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    global current_index
    if current_index < len(dogs):
        dog = dogs[current_index]
        return render_template_string(HTML, dog=dog, matches=len(matches), left=len(dogs)-current_index)
    return render_template_string(HTML, dog=None, matches=len(matches), left=0)

@app.route("/like")
def like():
    global current_index
    if current_index < len(dogs):
        # 50% chance of a match for fun
        if random.choice([True, False]):
            matches.append(dogs[current_index]["name"])
        current_index += 1
    return redirect(url_for("home"))

@app.route("/pass")
def pass_dog():
    global current_index
    if current_index < len(dogs):
        current_index += 1
    return redirect(url_for("home"))

@app.route("/reset")
def reset():
    global current_index, matches
    current_index = 0
    matches = []
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)