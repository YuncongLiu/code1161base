"""Week 3, Exercise 3.
Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
from exercise1 import not_number_rejector
import random


def advancedGuessingGame():
    """Play a guessing game with a user.
    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)
    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("Welcome to my guessing game")
    print("Let's pick both of the bounds")

    check = False

    lowerBound = not_number_rejector("Enter the lower bound: ")
    while check is False:
        try:
            upperBound = int(raw_input("Enter the upper bound: "))
            if upperBound > (lowerBound + 1):
                print("Ok you need to guess " +
                      "between {} and {}".format(lowerBound, upperBound))
                check = True
            elif upperBound == (lowerBound + 1):
                print("Numbers too close together")
            else:
                print("{} isn't higher than {}, try again".format(upperBound,
                                                                  lowerBound))
        except:
            print("Not an Integer")
            continue

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        try:
            guessedNumber = int(raw_input("Have a guess: "))
            if guessedNumber == actualNumber:
                print("Wow, {} was the answer!".format(actualNumber))
                guessed = True
            elif guessedNumber <= lowerBound:
                print("No, {} is too low!".format(guessedNumber))
            elif guessedNumber >= upperBound:
                print("No, {} is too high!".format(guessedNumber))
            elif guessedNumber < actualNumber:
                print("Guess higher!")
            elif guessedNumber > actualNumber:
                print("Guess lower!")
        except:
            print("Not an Integer")
            continue
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
