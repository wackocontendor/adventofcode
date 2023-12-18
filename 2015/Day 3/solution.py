data = open('data.txt').read()


mapping = {
    '>': {'axis': 'x', 'direction': 1},
    '<': {'axis': 'x', 'direction': -1},
    '^': {'axis': 'y', 'direction': 1},
    'v': {'axis': 'y', 'direction': -1}
    }

######### part one #########
coords = [(0, 0)]
x, y = (0, 0)
for char in data:
    direction = mapping[char]['direction']
    axis = mapping[char]['axis']
    if axis == 'x':
        x += direction
    else:
        y += direction
    coords.append((x, y))
print(len(set(coords)))

######### part two #########
coords = [(0, 0)]
sx, sy = (0, 0)
rx, ry = (0, 0)
for i, char in enumerate(data):
    direction = mapping[char]['direction']
    axis = mapping[char]['axis']
    if i % 2 == 0:
        if axis == 'x':
            sx += direction
        if axis == 'y':
            sy += direction
        coords.append((sx, sy))
    else:
        if axis == 'x':
            rx += direction
        if axis == 'y':
            ry += direction
        coords.append((rx, ry))    
print(len(set(coords)))