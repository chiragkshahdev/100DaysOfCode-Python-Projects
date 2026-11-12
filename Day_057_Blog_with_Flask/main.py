from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts
posts = [
    {
        "id": 1,
        "title": "My First Blog with Flask",
        "author": "Your Name",
        "date": "Nov 12, 2026",
        "content": "This is my first blog post created using Flask and Python."
    },
    {
        "id": 2,
        "title": "Why I Love Python",
        "author": "Your Name",
        "date": "Nov 12, 2026",
        "content": "Python is simple, powerful and perfect for beginners to build web apps."
    }
]

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)