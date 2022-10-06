#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Oct 5th, 2022
# This program asks the user for a number 0 and 9
# It then displays if they guessed the correct number
# and the total.
import constants


def main():
    # get the users input (users guessed number)
    guessed_number = int(input("Choose a number between 0 and 9 : "))

    # check if the user selected the correct number
    if guessed_number == constants.CORRECT_GUESS:
        # if the user guessed correctly, tell them
        print("You guessed correctly.")

    # check if the user selected the correct number
    if guessed_number != constants.CORRECT_GUESS:
        # if the user guessed incorrectly, tell them
        print("You guessed wrong.")


if __name__ == "__main__":
    main()
