import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

art = {
    "R": rock,
    "P": paper,
    "S": scissors
}

userChoice = input("Do you want to play rock, paper or scissors? Type (R/P/S): ").upper()
computerChoice = random.choice(["R", "P", "S"])

print("You chose:")
print(art[userChoice])

print("The computer chose:")
print(art[computerChoice])

if userChoice == computerChoice:
    print("Tie!")
elif userChoice == "R" and computerChoice == "P":
    print("You lose!")
elif userChoice == "R" and computerChoice == "S":
    print("You win!")
elif userChoice == "P" and computerChoice == "R":
    print("You win!")
elif userChoice == "P" and computerChoice == "S":
    print("You lose!")
elif userChoice == "S" and computerChoice == "P":
    print("You win!")
elif userChoice == "S" and computerChoice == "R":
    print("You lose!")
else:
    print("Incorrect input!")