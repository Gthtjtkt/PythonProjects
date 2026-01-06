import random

print("--- Welcome to the Advanced Number Guesser ---")

while True:
    try:

        max_range = int(input("Enter the maximum number for the range (e.g., 50, 100): "))

        if max_range < 2:

            raise ValueError("The range is too small, must be at least 2.")
        break

    except ValueError as e:

        print(f"Invalid setup: {e}")

number_to_guess = random.randint(1, max_range)

print(f"Have chosen a number between 1 and {max_range}")

attempts = 0
guess = None

while guess != number_to_guess:
    try:
        user_guess = int(input("Guess a number: "))
        guess = user_guess


