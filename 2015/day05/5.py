file = open("./2015/day05/input.txt", 'r')
data = file.readlines()
file.close()

vowels = ['a', 'e', 'i', 'o', 'u']
naughty = {'a': 'b', 'c': 'd', 'p': 'q', 'x': 'y'}

total_nice = 0

# Check for 3 vowels
for presents in data:
    # remove new line characters
    no_newlines = presents.strip()
    
    # Check for three vowels

    counter = 0
    for char in no_newlines:
        
        if char in vowels:
            counter += 1

    # Remove naughty strings
    if counter < 3:
        data.remove(presents)
print(len(data))
# Check for two letters in a row
for presents in data:
    # remove new line characters
    no_newlines = presents.strip()

    counter = 0

    for i in range(len(no_newlines)):
        if i != 15 and no_newlines[i] == no_newlines[i + 1]:
            
            counter += 1


    if counter == 0:
        data.remove(presents)
print(len(data))
# Check for 'ab', 'cd', 'pq', 'xy'
for presents in data:
    # remove new line characters
    no_newlines = presents.strip()
    
    counter = 0
    for i in range(len(no_newlines)):
        
        if i != 15:
            if no_newlines[i] in naughty.keys():
                
                if naughty.get(no_newlines[i]) == no_newlines[i + 1]:
                    
                    counter += 1
    if counter > 0:
        data.remove(presents)


print(len(data))