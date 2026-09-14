import random

# Hangman arts
HANGMAN_PICS = [
'''
  +---+
  | |
      |
      |
      |
      |
=========''', '''
  +---+
  | |
  O |
      |
      |
      |
=========''', '''
  +---+
  | |
  O |
  | |
      |
      |
=========''', '''
  +---+
  | |
  O |
 /| |
      |
      |
=========''', '''
  +---+
  | |
  O |
 /|\ |
      |
      |
=========''', '''
  +---+
  | |
  O |
 /|\ |
 / |
      |
=========''', '''
  +---+
  | |
  O |
 /|\ |
 / \ |
      |
========='''
]

WORDS = ["python", "developer", "hangman", "challenge", "programming", "laptop", "keyboard"]

def play():
    word = random.choice(WORDS)
    guessed = ["_"] * len(word)
    guessed_letters = []
    lives = 6

    print("=== Day 007 - Hangman Game ===")

    while lives > 0 and "_" in guessed:
        print(HANGMAN_PICS[6 - lives])
        print(f"\nWord: {' '.join(guessed)}")
        print(f"Lives: {lives} | Guessed: {', '.join(guessed_letters)}")

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess)!= 1:
            print("Please enter a single letter!")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            print(f"Oops! '{guess}' not in word.")
            lives -= 1

    if "_" not in guessed:
        print(f"\n🎉 YOU WIN! Word was: {word}")
    else:
        print(HANGMAN_PICS[6])
        print(f"\n💀 GAME OVER! Word was: {word}")

if __name__ == "__main__":
    play()