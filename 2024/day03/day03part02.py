import re

answer = 0

with open('./input.txt', 'r') as file:
    content = file.read()

regex = r"((?:do|don't)[^()\n]*?)?mul\(\d+,\s*\d+\)"

goodCode = re.findall(regex, content)

print(goodCode)
for x in goodCode:
    print(x)
    temp = re.findall("\d+", x)
    multTemp = int(temp[0]) * int(temp[1])
    answer += multTemp

