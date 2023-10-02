# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 08:36:53 2023

@author: Jinjia
"""

"""
In Bagels, a deductive logic game, you must guess a secret three-digit 
number based on clues. The game offers one of the following hints in response
to your guess: "Pico" when your guess has a correct digit in the wrong place.
"Fermi" when your guess has a correct digit in the correct place, and "Bagels"
if your guess has no correct digits. You have 10 times to guess the secret number.
"""

import random

def randomThreeDigit():
    # create a random 3 digit number
    return str(random.randint(100, 999))

def getInputNumber():
    # get the input 3-digit number from user
    userInput = input("Please guess a three-digit number: ")
    
    numberList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    if len(userInput) != 3:
        getInputNumber()
    
    for char in userInput:
        if char not in numberList:
            getInputNumber()
            
    return userInput

    

getInputNumber()