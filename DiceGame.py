# Nelson Oseguera

# March 30th, 2023

# Project 7

# This program is a game where two players roll a die. The program will generate random numbers, and based on the numbers it will print out who the winner is.

# the main function

import random

def main():
    # initialize the variables

    playerOne = 0

    playerTwo = 0

    winnerName = 0

    p1number = 0

    p2number = 0

    endProgram = "no"

    # call to the inputNames function

    inputNames()

    # while loop to run the program repeatedly:

    while endProgram == "no":

        #call to the rollDice function

        rollDice()

        #call to the displayInfo function

        displayInfo()

        #end the while loop or restart the program
        endProgram = input('Do you want to end the program? (Enter yes or no): ')


# this function will get the player names

def inputNames():

    global playerOne

    playerOne = input('Please enter the name of player one: ')

    global playerTwo

    playerTwo = input('Please enter the name of player two: ')

# this function will get the random values

def rollDice():

    global winnerName

    p1number = random.randint(1, 6)

    print(playerOne, '\'s number is', p1number)

    p2number = random.randint(1, 6)

    print(playerTwo, '\'s number is', p2number)

    if p1number == p2number:

        winnerName = "tie"

    if p1number > p2number:

        winnerName = playerOne

    if p1number < p2number:

        winnerName = playerTwo

# this function will display the winner

def displayInfo():

    print('The winner is', winnerName)

# start the program by calling the main function
main()
