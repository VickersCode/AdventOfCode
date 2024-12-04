import re

answer = 0

with open('./input.txt', 'r') as file:
    content = file.read()

goodCode = re.findall("mul\(\d+,\s*\d+\)", content)

for x in goodCode:
    temp = re.findall("\d+", x)
    multTemp = int(temp[0]) * int(temp[1])
    answer += multTemp

print(answer)