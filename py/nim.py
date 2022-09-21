# nim.py
# Adam Prado
# CSCI 77800 Fall 2022
# 9/4/22
# This code plays the game of Nim against a computer.  The starting stones is 12 and then each player selects a number from 1 to 3.  Whomever takes the last stone wins. 
# Currently the computer selects a number 1 to 3 randomly. 
import random

  
stonesBag = 12
stonesTaken = 0
playerWin = False

while stonesBag > 0: #continues game until the bag is empty
    print('There are ' + str(stonesBag) + ' stones in the bag.')
    selection = int(input('How many stones do you want to take?\n'))
    while selection > 3 or selection < 1:
        print('You cannot select that ammount, please choose a number from 1 to 3')
        selection = int(input('How many stones do you want to take?\n'))
    stonesBag = stonesBag - selection
    print('There are ' + str(stonesBag) + ' stones in the bag.')
    if stonesBag <= 0:
        playerWin = True
    else:   
        CPselection = random.randint(1, 3)
        print('the computer player selected ' + str(CPselection) + ' stones.')
        stonesBag = stonesBag - CPselection
print ('Game Over')
if playerWin:
    print("Congradulations, you win!!")
else:
    print("Sorry, the Computer won.")
