import re

# Grab the data from input.txt
file = open("./2015/day06/input.txt", 'r')
data = file.readlines()
file.close()

#----------------PART ONE-------------------------

# Initialize the grid with all zeros, lights are off
grid = [[0 for _ in range(1000)] for _ in range(1000)]

for presents in data:
    presents = presents.strip()

    #REGEX
    turnOn = re.search("^turn on", presents)
    toggle = re.search("^toggle", presents)
    turnOff = re.search("^turn off", presents)
    coord = re.findall("\d{1,3}", presents)

    
    if turnOn:
        for i in range(int(coord[0]), int(coord[2]) + 1):
            for j in range(int(coord[1]), int(coord[3]) + 1):
                grid[i][j] = 1
    if turnOff:
        for i in range(int(coord[0]), int(coord[2]) + 1):
            for j in range(int(coord[1]), int(coord[3]) + 1):
                grid[i][j] = 0
    if toggle:
        for i in range(int(coord[0]), int(coord[2]) + 1):
            for j in range(int(coord[1]), int(coord[3]) + 1):
                grid[i][j] = 1 - grid[i][j]


counter = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j] == 1:
            counter += 1

print(counter)

#----------------PART TWO----------------------

# Initialize the grid with all zeros, lights are off
grid = [[0 for _ in range(1000)] for _ in range(1000)]

for presents in data:
    presents = presents.strip()

    #REGEX
    turnOn = re.search("^turn on", presents)
    toggle = re.search("^toggle", presents)
    turnOff = re.search("^turn off", presents)
    coord = re.findall("\d{1,3}", presents)

    
    if turnOn:
        for i in range(int(coord[0]), int(coord[2]) + 1):
            for j in range(int(coord[1]), int(coord[3]) + 1):
                grid[i][j] += 1
    if turnOff:
        for i in range(int(coord[0]), int(coord[2]) + 1):
            for j in range(int(coord[1]), int(coord[3]) + 1):
                if grid[i][j] > 0:
                    grid[i][j] -= 1
                else:
                    grid[i][j] = 0
    if toggle:
        for i in range(int(coord[0]), int(coord[2]) + 1):
            for j in range(int(coord[1]), int(coord[3]) + 1):
                grid[i][j] += 2


counter = 0
for i in range(1000):
    for j in range(1000):
        counter += grid[i][j]

print(counter)
