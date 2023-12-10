#import libraries
import math

#read file line by line
file = open('data.txt','r')
strings = file.read().splitlines()
file.close()

######## Part 1 ########

part_one_sum = 0

for string in strings:
    game_id = int(string[5:int(string.find(":"))])

    string = string[string.find(":")+2:].replace(';', ',').split(', ')

    game_possible = True

    for count_colour in string:
        cube_count = int(count_colour[:count_colour.find(' ')])
        cube_colour = count_colour[count_colour.find(' ')+1:]
        if cube_count > 14:
            game_possible = False
        elif cube_count > 13 and cube_colour != 'blue':
            game_possible = False
        elif cube_count > 12 and cube_colour not in ('green', 'blue'):
            game_possible = False
    
    if game_possible == True:
        part_one_sum += game_id

######## Part 2 ########

part_two_sum = 0

for string in strings:
    game_id = int(string[5:int(string.find(":"))])

    string = string[string.find(":")+2:].replace(';', ',').split(', ')

    min_colour_counts = {'red': 0, 'green': 0, 'blue': 0}

    for count_colour in string:
        cube_count = int(count_colour[:count_colour.find(' ')])
        cube_colour = count_colour[count_colour.find(' ')+1:]
        if cube_count > min_colour_counts[cube_colour]:
            min_colour_counts[cube_colour] = cube_count
    
    part_two_sum += math.prod(min_colour_counts.values())

print(f"Part one: {part_one_sum} | Part two: {part_two_sum}")