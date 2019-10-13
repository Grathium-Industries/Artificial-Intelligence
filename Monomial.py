#!/usr/bin/env python3
import random

#initialization
favNumber = 0
generations = 0
maxNumber = 1000
dialationFactor = maxNumber

print("\nPick a number between 1 and ,", maxNumber)
number = int(input())
while True:
    generations += 1

    if number > maxNumber:
        continue

    if (favNumber == 0):
        favNumber = random.randint(-1,maxNumber)
    print(favNumber) #output the number guess

    if number < favNumber:
        favNumber -= (1 * (dialationFactor / generations))
    elif number > favNumber:
        favNumber += (1 * (dialationFactor / generations))
