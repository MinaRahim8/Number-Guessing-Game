# Coding Project Number 1 : Number Guessing Game
import random

#global variable for the guess

def is_correct_number(val: int, secret : int) -> bool:
    if val is secret:
        return True
    else:
        return False

def return_hint(val: int, secret: int) -> str:
    if val < secret:
        return "Thats too low"
    else:
        return "Thats too high"

def main():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess a number between 1-100 in a the fewest guesses possible.")
    name = input("What is your name? ")
    secret = random.randint(1, 100) # gets the target number

    while True:
        try:
            guess = int(input(f"Okay {name}, what is your guess? "))
        except ValueError:
            print("Invalid Input")
            continue

        while guess is not secret:
            if not is_correct_number(guess, secret):
                print(return_hint(guess, secret))
                guess = int(input(f"Okay {name}, what is your next guess? "))

        print("Thats correct!")
        play = input("Play Again? Type yes/no :  ").lower().strip()

        if play == "yes":
            secret = random.randint(1, 100)
        else:
            print("Exiting game. Thank you for playing")
            break


if __name__ == "__main__":
    main()

