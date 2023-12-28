# Grab the data from input2.txt
file = open("./2015/input2.txt", 'r')
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

