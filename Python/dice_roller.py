# Automatic Dice Roller
# Written by [piper]

from random import randint #imports random number generator 

print ("Automatic Dice Roller")

repeat = True #repeats function if true
while repeat:
    print("You rolled",randint(1,6)) #prints your number, sets range 
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower() #repeats function if Y
