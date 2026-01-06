import random
number_to_guess = random.randint(1, 100)
print(f"(Debug) Number to guess: {number_to_guess}")


isCorrect = False

while isCorrect == False:

    user_guess = int(input("Guess: "))

    if user_guess < number_to_guess:
        print(f"(Debug) Number too low")
    elif user_guess > number_to_guess:
        print(f"(Debug) Number too high")
    else:
        print(f"(Debug) Number equals {number_to_guess}")
        isCorrect = True
