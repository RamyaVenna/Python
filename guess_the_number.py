# this is a guess the number game

import random

secretNumber=random.randint(1,20)
print("I am thinking of a number between 1 and 20")

# ask the player to guess the number 6 times

for guessesTaken in range(1,7):
    print("Guess the number:")
    guess=int(input())
    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break
if guess == secretNumber:
    print("Congrats, You guessed it right in " +str(guessesTaken)+ "times")
else:
    print("Nope, The number I was guessing is " +str(secretNumber))
