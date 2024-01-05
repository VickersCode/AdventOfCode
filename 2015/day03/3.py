import re
from collections import defaultdict

with open('./2015/day03/input3.txt') as f:
    data = f.read()

# ------- PART ONE ------------
    
gridList = ['0, 0']
santa = [0, 0, 's']

for x in range(len(data)):

    mover = santa
    if data[x] == '<':
        mover = [mover[0] - 1, mover[1], mover[2]]
    elif data[x] == '>':
        mover = [mover[0] + 1, mover[1], mover[2]]
    elif data[x] == '^':
        mover = [mover[0], mover[1] + 1, mover[2]]
    elif data[x] == 'v':
        mover = [mover[0], mover[1] - 1, mover[2]]

    if not str(mover[0]) + ',' + str(mover[1]) in gridList:
        gridList.append(str(mover[0]) + ',' + str(mover[1]))

    santa = mover
    
    answer = len(gridList) - 1

print(answer)

# --------- PART TWO ------------

gridList = ['0, 0']
santa = [0, 0, 's']
roboSanta = [0, 0, 'r']

for x in range(len(data)):

    if x == 0 or x % 2 == 0:
        mover = santa
    else:
        mover = roboSanta

    if data[x] == '<':
        mover = [mover[0] - 1, mover[1], mover[2]]
    elif data[x] == '>':
        mover = [mover[0] + 1, mover[1], mover[2]]
    elif data[x] == '^':
        mover = [mover[0], mover[1] + 1, mover[2]]
    elif data[x] == 'v':
        mover = [mover[0], mover[1] - 1, mover[2]]

    if not str(mover[0]) + ',' + str(mover[1]) in gridList:
        gridList.append(str(mover[0]) + ',' + str(mover[1]))

    if x == 0 or x % 2 == 0:
        santa = mover
    else:
        roboSanta = mover

    answer = len(gridList) - 1

print(answer)