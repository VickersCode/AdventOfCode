# PART 1

# Grab the data from input1.txt
file = open("./2015/day01/input1.txt", 'r')
data = file.read()
file.close()

# Initialize final variable
res = 0

# Loop through input data, increment for '(' and decrement for ')'
for char in data:
    if char == '(':
        res += 1
    if char == ')':
        res -= 1

print(res)

# ----------------------------------------------
# PART 2

counter = 0
floors = 0


for char in data:
    if floors == -1:
        break
    if char == '(':
        floors += 1
        counter += 1
    if char == ')':
        floors -= 1
        counter += 1
    
    

print(counter)