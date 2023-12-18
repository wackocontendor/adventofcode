data = open('data.txt').read()

######### part one #########
floor = 0
for char in data:
    if char == '(':
        floor += 1
    if char == ')':
        floor -= 1
print(floor)

######### part two #########
floor = 0
for i, char in enumerate(data):
    if char == '(':
        floor += 1
    if char == ')':
        floor -= 1
    if floor < 0:
        print(i + 1)
        break