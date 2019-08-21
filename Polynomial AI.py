#!/usr/bin/env python3
import random
import os

#initialization
generations = 0
correct = [45, 368, 972]
plus = True

items = [1, 1, 1]
itemEdit = 0

print("\nEnter Dialation Factor:")
dialationFactor = int(input())

# this is where it checks if it should go lower or higher
# NOTE: this can also be used for feedback
def check(x):
    if items[x] > correct[x]:
        return False
    elif items[x] < correct[x]:
        return True
    pass

def UI():
    os.system('cls')
    for i in range(len(items)):
        print(i, ":  ", items[i])
    print("gen: ", round(generations, 1))


#randomly set inital item variables
for i in range(len(items)):
    items[i] = random.randint(1, 10)

while True:
    generations += 1
    itemEdit = random.randint(0, len(items) - 1) # pick random item to edit
    itemNumber = items[itemEdit]
    UI() # display user readable data

    # editing of the item value
    plus = check(itemEdit) # get if you need to go higher or lower
    if (plus == True):
        itemNumber += (1 * (dialationFactor / round(generations / len(items), 1)))
    else:
        itemNumber -= (1 * (dialationFactor / round(generations / len(items), 1)))

    items[itemEdit] = abs(itemNumber) # remove abs() for negitave vales
