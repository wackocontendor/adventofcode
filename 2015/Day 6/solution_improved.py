#import libraries
import numpy as np

data = open('data.txt').read().splitlines()

######### part one #########
array = np.full((1000,1000), 0)

for line in data:
    chunks = line.split()
    from_x, from_y = map(int, chunks[-3].split(','))
    to_x, to_y = map(int, chunks[-1].split(','))
    if chunks[0] == 'turn':
        if chunks[1] == 'on':
            array[from_x:to_x+1, from_y:to_y+1] = 1
        if chunks[1] == 'off':
            array[from_x:to_x+1, from_y:to_y+1] = 0
    if chunks[0] == 'toggle':
            array[from_x:to_x+1, from_y:to_y+1] = 1 - array[from_x:to_x+1, from_y:to_y+1]
print(array.sum())

######### part two #########
array = np.full((1000,1000), 0)

for line in data:
    chunks = line.split()
    from_x, from_y = map(int, chunks[-3].split(','))
    to_x, to_y = map(int, chunks[-1].split(','))
    if chunks[0] == 'turn':
        if chunks[1] == 'on':
            array[from_x:to_x+1, from_y:to_y+1] += 1
        if chunks[1] == 'off':
            array[from_x:to_x+1, from_y:to_y+1] -= 1
            array[from_x:to_x+1, from_y:to_y+1] = array[from_x:to_x+1, from_y:to_y+1].clip(0)
    if chunks[0] == 'toggle':
            array[from_x:to_x+1, from_y:to_y+1] += 2
print(array.sum())