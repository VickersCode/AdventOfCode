# Grab the data from input2.txt
file = open("./2015/day02/input2.txt", 'r')
data = file.readlines()
file.close()

# Initialize the answer variable
answer = 0

for presents in data:
    # remove new line characters
    no_newlines = presents.strip()

    # Put dimensions into a list and convert to integers
    dim_data = no_newlines.split('x')
    
    answer += 2*(int(dim_data[0]) * int(dim_data[1])) + 2*(int(dim_data[1]) * int(dim_data[2])) + 2*(int(dim_data[0]) * int(dim_data[2])) + min(int(dim_data[1]) * int(dim_data[2]), int(dim_data[0]) * int(dim_data[2]), int(dim_data[0]) * int(dim_data[1]))

print(answer)
    

# PART TWO
answer = 0
for presents in data:
    # remove new line characters
    no_newlines = presents.strip()

    # Put dimensions into a list and convert to integers
    dim_data = no_newlines.split('x')

    for i in range(len(dim_data)):
        dim_data[i] = int(dim_data[i])

    volume = dim_data[0] * dim_data[1] * dim_data[2]
    smallestSide = min(dim_data)
    
    dim_data.pop(dim_data.index(smallestSide))
    secondSmallestSide = min(dim_data)

    answer += (2 * smallestSide) + (2 * secondSmallestSide) + volume
    

print(answer)



