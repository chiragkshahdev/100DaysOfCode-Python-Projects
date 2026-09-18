import random
import os

# Logo
logo = """
    __  ___       __  __           __    __                      
   / / / (_)___ _/ / / /_  ___  __/ /___/ /      ____ _____ ___  ___ 
  / /_/ / / __ `/ / / / / /_/ / __  / | /| / / __ `/ __ `__ \/ _ \\
 / __  / / /_/ / / / / /_/ / __/ / /_/ /| |/ |/ / /_/ / / / / / /  __/
/_/ /_/_/\__, /_/_/_/\__,_/_/  /_/\__,_/ |__/|__/\__,_/_/ /_/ /_/\___/ 
        /____/                                                         
"""
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

# Game Data - 50 followers data
data = [
    {'name': 'Cristiano Ronaldo', 'follower_count': 615, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Lionel Messi', 'follower_count': 490, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Selena Gomez', 'follower_count': 430, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Kylie Jenner', 'follower_count': 400, 'description': 'Reality TV personality and businesswoman', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'follower_count': 390, 'description': 'Actor and professional wrestler', 'country': 'United States'},
    {'name': 'Ariana Grande', 'follower_count': 380, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Kim Kardashian', 'follower_count': 364, 'description': 'Reality TV personality and businesswoman', 'country': 'United States'},
    {'name': 'Beyonce', 'follower_count': 320, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Khloe Kardashian', 'follower_count': 311, 'description': 'Reality TV personality', 'country': 'United States'},
    {'name': 'Nike', 'follower_count': 306, 'description': 'Sportswear multinational', 'country': 'United States'},
]

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

game()