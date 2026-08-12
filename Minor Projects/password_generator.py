"""
Password Generator
-------------------
Generates a random, customizable password based on user preferences
(length, digits, symbols, uppercase letters).
"""

import random
import string


def generate_password(length=12, use_digits=True, use_symbols=True, use_upper=True):
    pool = list(string.ascii_lowercase)
    required = []

    if use_upper:
        pool += list(string.ascii_uppercase)
        required.append(random.choice(string.ascii_uppercase))
    if use_digits:
        pool += list(string.digits)
        required.append(random.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()-_=+"
        pool += list(symbols)
        required.append(random.choice(symbols))

    if length < len(required):
        length = len(required)

    remaining = [random.choice(pool) for _ in range(length - len(required))]
    password_chars = required + remaining
    random.shuffle(password_chars)
    return "".join(password_chars)


def get_yes_no(prompt):
    ans = input(prompt).strip().lower()
    return ans in ("y", "yes", "")


def main():
    print("=== PASSWORD GENERATOR ===")
    try:
        length = int(input("Password length (default 12): ") or 12)
    except ValueError:
        length = 12

    use_upper = get_yes_no("Include uppercase letters? (Y/n): ")
    use_digits = get_yes_no("Include digits? (Y/n): ")
    use_symbols = get_yes_no("Include symbols? (Y/n): ")

    how_many = input("How many passwords to generate? (default 1): ").strip()
    how_many = int(how_many) if how_many.isdigit() else 1

    print("\nGenerated password(s):")
    for _ in range(how_many):
        pwd = generate_password(length, use_digits, use_symbols, use_upper)
        print(pwd)


if __name__ == "__main__":
    main()
