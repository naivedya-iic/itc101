"""
Password Strength Checker
--------------------------
Scores a password based on length and character variety,
and gives feedback on how to improve it.

Usage: python 6_password_strength_checker.py
"""

import re


COMMON_PASSWORDS = {
    "123456", "password", "123456789", "qwerty", "abc123",
    "111111", "letmein", "welcome", "admin", "iloveyou"
}


def check_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return 0, ["This is a very common password. Avoid it entirely."]

    # Length checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("12+ characters is stronger.")

    # Character variety checks
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*()\-_=+\[\]{};:,.<>?/]", password):
        score += 1
    else:
        feedback.append("Add symbols (e.g. !@#$%).")

    return score, feedback


def score_label(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    elif score <= 5:
        return "Strong"
    else:
        return "Very Strong"


def main():
    print("=== PASSWORD STRENGTH CHECKER ===")
    while True:
        password = input("\nEnter a password to check (or 'q' to quit): ")
        if password.lower() == "q":
            print("Goodbye!")
            break

        score, feedback = check_strength(password)
        label = score_label(score)
        print(f"Strength: {label}  (score: {score}/6)")

        if feedback:
            print("Suggestions:")
            for tip in feedback:
                print(f"  - {tip}")
        else:
            print("Great password!")


if __name__ == "__main__":
    main()
