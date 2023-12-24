import numpy as np

data = open('data.txt').read().splitlines()
var_dict = {}

######### part one #########
def bitwiseand(x, y):
    return str(np.bitwise_and(x, y))

def bitwiseor(x, y):
    return str(np.bitwise_or(x, y))

def leftshift(x, num):
    return str(np.left_shift(x, num))

def rightshift(x, num):
    return str(np.right_shift(x, num))

def bitwisecomplement(x):
    return str(np.invert(np.array(x, dtype=np.uint16)))

for line in data:
    instruction, output_var = line.split(' -> ')
    var_dict[output_var] = instruction

not_correct = True
key_digit_count = {}
while not_correct:
    for key in var_dict.keys():
        words = var_dict[key].split()
        if len(words) == 1:
            if words[0] in var_dict.keys():
                if var_dict[words[0]].isdigit():
                    var_dict[key] = var_dict[words[0]]
            if words[0].isdigit():
                key_digit_count[key] = words[0]
                if len(key_digit_count) == len(var_dict):
                    not_correct = False
                continue
        elif 'AND' in words:
            if words[0] in var_dict.keys():
                if var_dict[words[0]].isdigit():
                    words[0] = var_dict[words[0]]
            if words[2] in var_dict.keys():
                if var_dict[words[2]].isdigit():
                    words[2] = var_dict[words[2]]
            if words[0].isdigit() and words[2].isdigit():
                var_dict[key] = bitwiseand(int(words[0]), int(words[2]))
        elif 'OR' in words:
            if words[0] in var_dict.keys():
                if var_dict[words[0]].isdigit():
                    words[0] = var_dict[words[0]]
            if words[2] in var_dict.keys():
                if var_dict[words[2]].isdigit():
                    words[2] = var_dict[words[2]]
            if words[0].isdigit() and words[2].isdigit():
                var_dict[key] = bitwiseor(int(words[0]), int(words[2]))
        elif 'LSHIFT' in words:
            if words[0] in var_dict.keys():
                if var_dict[words[0]].isdigit():
                    words[0] = var_dict[words[0]]
            if words[2] in var_dict.keys():
                if var_dict[words[2]].isdigit():
                    words[2] = var_dict[words[2]]
            if words[0].isdigit() and words[2].isdigit():
                var_dict[key] = leftshift(int(words[0]), int(words[2]))
        elif 'RSHIFT' in words:
            if words[0] in var_dict.keys():
                if var_dict[words[0]].isdigit():
                    words[0] = var_dict[words[0]]
            if words[2] in var_dict.keys():
                if var_dict[words[2]].isdigit():
                    words[2] = var_dict[words[2]]
            if words[0].isdigit() and words[2].isdigit():
                var_dict[key] = rightshift(int(words[0]), int(words[2]))
        elif 'NOT' in words:
            if words[1] in var_dict.keys():
                if var_dict[words[1]].isdigit():
                    words[1] = var_dict[words[1]]
            if words[1].isdigit():
                var_dict[key] = bitwisecomplement(words[1])
print(var_dict['a'])

######### part two #########