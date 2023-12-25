import numpy as np

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

def updateinstruction(index):
    x = words[index]
    return var_dict[x] if x in var_dict.keys() and var_dict[x].isdigit() else x

data = open('data.txt').read().splitlines()
not_correct = True
key_digit_count = {}
var_dict = {}
for line in data:
    instruction, output_var = line.split(' -> ')
    var_dict[output_var] = instruction
while not_correct:
    for key in var_dict.keys():
        words = var_dict[key].split()
        if len(words) == 1:
            var_dict[key] = updateinstruction(0)
            if words[0].isdigit():
                key_digit_count[key] = words[0]
                if len(key_digit_count) == len(var_dict):
                    not_correct = False
                continue
        elif 'AND' in words:
            words[0] = updateinstruction(0)
            words[2] = updateinstruction(2)
            if words[0].isdigit() and words[2].isdigit():
                var_dict[key] = bitwiseand(int(words[0]), int(words[2]))
        elif 'OR' in words:
            words[0] = updateinstruction(0)
            words[2] = updateinstruction(2)
            if words[0].isdigit() and words[2].isdigit():
                var_dict[key] = bitwiseor(int(words[0]), int(words[2]))
        elif 'LSHIFT' in words:
            words[0] = updateinstruction(0)
            words[2] = updateinstruction(2)
            if words[0].isdigit() and words[2].isdigit():
                var_dict[key] = leftshift(int(words[0]), int(words[2]))
        elif 'RSHIFT' in words:
            words[0] = updateinstruction(0)
            words[2] = updateinstruction(2)
            if words[0].isdigit() and words[2].isdigit():
                var_dict[key] = rightshift(int(words[0]), int(words[2]))
        elif 'NOT' in words:
            words[1] = updateinstruction(1)
            if words[1].isdigit():
                var_dict[key] = bitwisecomplement(words[1])
print(var_dict)

######### part two #########