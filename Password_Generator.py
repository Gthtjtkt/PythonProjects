"""
1/5/2026
password_generator.py

desc:
    generates a password based on user defined critera. user specifies the
    nnumber of letters, numbers, and symbols they want included. the probram
    randomly selects members of each list and appends them to a list
    called passwordChars. The program then shuffles the members of this list,
    converts it to a string, and gives it back to the user.

    inputs:
        - Number of letters (integer, user input)
        - Number of symbols (integer, user input)
        - Number of numbers (integer, user input)

    outputs:
        - Password (list, unshuffled)
        - Password (string, shuffled)

    dependencies:
        - random module

"""

import random

# -------------------------------------------------------------------
# Character pools used for password generation
# -------------------------------------------------------------------

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# -------------------------------------------------------------------
# User input
# -------------------------------------------------------------------

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# -------------------------------------------------------------------
# Password generation
# -------------------------------------------------------------------

passwordChars = [] # List so it can be appended to and shuffled

# Add random letters
for _ in range(nr_letters):
    passwordChars.append(random.choice(letters))

# Add random numbers
for char in range(nr_symbols):
    passwordChars.append(random.choice(numbers))

# Add random symbols
for char in range(nr_numbers):
    passwordChars.append(random.choice(symbols))

print(f"password: {passwordChars}")

random.shuffle(passwordChars)
password = "".join(passwordChars) # Call the join method, which turns a list into a string

print(f"the new password is {password}")
