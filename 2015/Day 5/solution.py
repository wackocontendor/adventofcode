data = open('data.txt').read().splitlines()

######### part one #########
nice_line = 0
for line in data:
    if line.find('ab') != -1 or line.find('cd') != -1 or line.find('pq') != -1 or line.find('xy') != -1:
        continue
    vowel_count = 0
    double_letter_count = False
    for i, char in enumerate(line):
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
        if i < len(line)-1:
            if char == line[i + 1]:
                double_letter_count = True
    if vowel_count >= 3 and double_letter_count:
        nice_line += 1
print(nice_line)

######### part two #########
nice_lines = 0
for line in data:
    double_letter_count = False
    double_double = False
    for i, char in enumerate(line):
        if i < len(line) - 2:
            if char == line[i + 2]:
                double_letter_count = True
        if i < len(line) - 1:
            pair = char + line[i + 1]
            if len(line) - len(line.replace(pair, '')) >= 4:
                double_double = True
    if double_double and double_letter_count:
        nice_lines += 1
print(nice_lines)