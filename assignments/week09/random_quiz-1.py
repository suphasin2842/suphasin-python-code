"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""

import random

def test_random():
    random_number = random.randint(1, 20)
    live=6
    while True:
       
        number = int(input(" Enter your number: "))
        if(number == random_number):
            print()
            print(f"Good job! my name is brian, i'm 24 year old ,i'm from korea.(You won in {live} attempts!)")
            break
        elif(number < random_number):
            live-=1
            print()
            print(f"you number is less then random number (your life now {live})")
        elif (number > random_number):
            live-=1
            print()
            print(f"you number is more then random number (your life now {live})")
        if(live==0):
            print()
            print(f"your live is {live} Game over")
            break
    print()
    print(f"THE RANDOM NUMBER ARE {random_number}")
test_random()