#!/usr/bin/env python3
import random
import os

#initialization
goal = 100
paramiters = [1, 29, 3]
plus = True
generations = 0

def check():
    tempi = 0
    for x in range(len(paramiters)):
        tempi += paramiters[x]
    print(round(tempi, 1)) # print output to screen
    if (tempi < 100):
        return True
    else:
        return False


print("\nEnter Dialation Factor:")
dialationFactor = int(input())
while True:
    generations += 1
    itemEdit = random.randint(0, len(paramiters) - 1)

    plus = check()
    if plus == True:
        paramiters[itemEdit] += (1 * (dialationFactor / generations))
    else:
        paramiters[itemEdit] -= (1 * (dialationFactor / generations))
