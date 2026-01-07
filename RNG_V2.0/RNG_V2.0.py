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
        # We try to convert input to an integer
        user_input = input("Guess a number: ")
        guess = int(user_input)

        # CONSTRAINT CHECK: This must be its own 'if' statement
        if guess < 1 or guess > max_range:
            raise IndexError(f"Out of range! Must be between 1 and {max_range}.")

        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! It took you {attempts} tries.")

    except ValueError:
        print(f"invalid input! Try again.")

    except IndexError as e:
        print(f"constraint error: {e}.")

    finally:
        print(f"(Current attempt count: {attempts}).")

