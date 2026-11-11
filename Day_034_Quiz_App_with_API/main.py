# Day 34 - Quiz App with API
# API Used: Open Trivia DB (Free, No Key Needed)

import requests
import html
import random

def get_questions():
    url = "https://opentdb.com/api.php?amount=5&type=multiple"
    try:
        response = requests.get(url)
        data = response.json()
        return data["results"]
    except Exception as e:
        print("API Error:", e)
        return []

def run_quiz():
    print("=== Welcome to Quiz App ===")
    print("You will get 5 questions from API\n")

    questions = get_questions()

    if not questions:
        print("No questions found. Check your internet.")
        return

    score = 0

    for i, q in enumerate(questions, 1):
        question = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])
        options = [html.unescape(opt) for opt in q["incorrect_answers"]]
        options.append(correct)
        random.shuffle(options)

        print(f"Q{i}. {question}")
        for idx, opt in enumerate(options, 1):
            print(f"  {idx}. {opt}")

        try:
            choice = int(input("Your Answer (1-4): "))
            if options[choice - 1] == correct:
                print("Correct! +1\n")
                score += 1
            else:
                print(f"Wrong! Correct answer was: {correct}\n")
        except:
            print(f"Invalid input. Correct answer was: {correct}\n")

    print(f"=== Quiz Over ===")
    print(f"Your Final Score: {score}/5")
    if score == 5:
        print("Excellent! You are a Quiz Master")
    elif score >= 3:
        print("Good Job!")
    else:
        print("Keep Practicing!")

if __name__ == "__main__":
    run_quiz()