#import libraries
import re

#read file line by line
file = open('data.txt','r')
strings = file.read().splitlines()
file.close()

######## Part 1 ########

#initialise the scoring
part_one_sum = 0

#loop through each item in the list, strip all the letters out, add the first and last numbers, and add the row number to the total sum
for item in strings:
    num = re.sub(r'[^\d]+', '', item)
    first_num = num[0]
    last_num =  num[-1]
    line_sum = int(first_num + last_num)
    part_one_sum += line_sum

######## Part 2 ########
# Confession: I had to copy the .replace idea from someone else. It's day one I'll let myself off (:

part_two_sum = 0

for string in strings:
    string_new = string.replace('one', 'one1one').replace('two', 'two2two').replace('three', 'three3three').replace('four', 'four4four').replace('five', 'five5five').replace('six', 'six6six').replace('seven', 'seven7seven').replace('eight', 'eight8eight').replace('nine', 'nine9nine')
    num = re.sub(r'[^\d]+', '', string_new)
    first_num = num[0]
    last_num = num[-1]
    line_sum = int(first_num + last_num)
    part_two_sum += line_sum

print(f"Part one: {part_one_sum} | Part two: {part_two_sum}")