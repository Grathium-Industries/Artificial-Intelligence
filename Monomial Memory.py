#!/usr/bin/env python3
import random
import linecache
from difflib import SequenceMatcher

memory = ["Hello", "fuck off", "how are you"]
output = ["Hello Grathium", "no u", "why'd you do this to me"]
responceDone = False
# get how many words there are
# NOTE: this is initilized because it would take to long to read the file every time
totalResponces = len(open("words.txt").readlines())

# creating new responce initilization
NewresponceLength = 0

while True:
    responceDone = False
    query = input()
    for i in range(len(memory)):
        if (SequenceMatcher(None, query, memory[i]).ratio() >= 0.8):
            print(output[i])
            responceDone = True

    # if no responce was done, make a new responce
    if responceDone == False:
        memory.append(query) # set a new memory block to the query
        NewresponceLength = random.randint(1,5)

        wordConstruction = ""
        for i in range(NewresponceLength):
            # create new responce string
            word = random.randint(0,totalResponces)
            wordConstruction += " " + linecache.getline('words.txt',word)

        # remove new lines from strings
        wordConstruction = wordConstruction.replace('\n', '')
        wordConstruction = wordConstruction.translate({ord('\n'): None})
        # set and output the new responce
        output.append(wordConstruction)
        print(wordConstruction)
