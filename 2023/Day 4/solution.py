#import libraries

#read file line by line
file = open('data.txt','r')
strings = file.read().splitlines()
file.close()

######## Part 1 ########

part_one_sum = 0

for line in strings:
    line_clean = line[line.find(':')+1:]
    line_parts = line_clean.split('|')
    card_nums = line_parts[0].strip().split()
    winning_nums = line_parts[1].strip().split()
    matches = [num for num in card_nums if num in winning_nums]
    if len(matches) > 0:
        part_one_sum += 2 ** (len(matches) - 1)

######## Part 2 ########

part_two_sum = 0
num_dict = {}

for num in range(len(strings)):
    line_clean = strings[num][strings[num].find(':')+1:]
    line_parts = line_clean.split('|')
    card_nums = line_parts[0].strip().split()
    winning_nums = line_parts[1].strip().split()
    matches = [num for num in card_nums if num in winning_nums]
    num_dict[num + 1] = {'count': 1, 'matches': len(matches)}

for key in num_dict.keys():
    key_count = num_dict[key]['count']
    key_matches = num_dict[key]['matches']

    for count in range(key_count):
        range_to_add = key_matches

        for num in range(1,range_to_add + 1):
            num_dict[key + num]['count'] += 1

for num in num_dict.keys():
    part_two_sum += num_dict[num]['count']

print(f"Part one: {part_one_sum} | Part two: {part_two_sum}")