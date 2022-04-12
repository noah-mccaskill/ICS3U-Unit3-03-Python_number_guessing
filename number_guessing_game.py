#!/usr/bin/env python3

# Created by: Noah McCaskill
# Created on: April 2022
# This is a guess the random number program

import random


def main():

    # This is a random number guesser

    # input
    guess_number = int(input("Enter your first guess here (0-9): "))

    random_number = random.randint(0, 9)  # a number between 0 and 9

    # process & output
    if guess_number == random_number:
        print("\nGuess is correct!")
        print("\nDone!")
    else:
        print("\nYour guess is incorrect!")
        print("\nThe correct number is {0}.".format(random_number))
        print("\nDone.")


if __name__ == "__main__":
    main()
