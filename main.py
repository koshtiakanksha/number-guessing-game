import random
from art import logo
print(logo)
number = random.randint(1,100)
print("Welocome to number guessing game!")
print("I'm thinking of a number between 1 and 100. Guess the number I'm thinking.")
difficulty = input("Choose the difficulty level, Easy or Hard:\n").lower()


def diff(difficulty):
    if difficulty == "easy":
        no_of_chances = 10
    else:
        no_of_chances = 5
    return no_of_chances
def playGame(no_of_chances):
    diff(difficulty)
    guess = 0
    print(f"You have {no_of_chances} chances to guess the correct number")

    while no_of_chances > 0 and  guess != number:
        guess = int(input("Please guess a number:\n"))
        if guess == number:
            print("You win. You guessed the correct number")
        elif guess > number:
            print(f"Too high! Please choose a smaller number. You have {no_of_chances-1} left")
        else:
            print(f"Too low! Please choose a bigger number. You have {no_of_chances-1} left")
        no_of_chances -= 1
playGame(diff(difficulty))
