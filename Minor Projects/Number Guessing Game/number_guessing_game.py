"""
Number Guessing Game
---------------------
The computer picks a random number and the player tries to guess it,
with difficulty levels controlling the range and attempt limit.

Usage: python 7_number_guessing_game.py
"""

import random

DIFFICULTIES = {
    "1": {"label": "Easy", "range": (1, 50), "attempts": 10},
    "2": {"label": "Medium", "range": (1, 100), "attempts": 7},
    "3": {"label": "Hard", "range": (1, 200), "attempts": 5},
}


def choose_difficulty():
    print("\nChoose difficulty:")
    for key, d in DIFFICULTIES.items():
        low, high = d["range"]
        print(f"{key}. {d['label']} (range {low}-{high}, {d['attempts']} attempts)")

    choice = input("Enter choice (1-3): ").strip()
    return DIFFICULTIES.get(choice, DIFFICULTIES["2"])


def play_round(difficulty):
    low, high = difficulty["range"]
    attempts_left = difficulty["attempts"]
    target = random.randint(low, high)

    print(f"\nI'm thinking of a number between {low} and {high}. "
          f"You have {attempts_left} attempts.")

    while attempts_left > 0:
        guess_input = input(f"Attempts left: {attempts_left}. Your guess: ").strip()
        if not guess_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess_input)
        attempts_left -= 1

        if guess == target:
            print(f"Correct! The number was {target}. You won! 🎉")
            return True
        elif guess < target:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Out of attempts! The number was {target}.")
    return False


def main():
    print("=== NUMBER GUESSING GAME ===")
    wins, total = 0, 0

    while True:
        difficulty = choose_difficulty()
        won = play_round(difficulty)
        total += 1
        if won:
            wins += 1

        print(f"\nScore: {wins}/{total} rounds won.")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
