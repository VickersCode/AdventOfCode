import re

answer = 0

with open('./input.txt', 'r') as file:
    content = file.read()

regex = r"don't|do|mul\(\d+,\s*\d+\)"

goodCode = re.findall(regex, content)


enable = True
for x in goodCode:
    print(x)
    if x == "don't":
        enable = False
    if x == "do":
        enable = True
    if enable == False:
        continue
    temp = re.findall("\d+", x)
    if temp:
        multTemp = int(temp[0]) * int(temp[1])
        answer += multTemp
        print("multiplied by:" + str(multTemp))


print(answer)

