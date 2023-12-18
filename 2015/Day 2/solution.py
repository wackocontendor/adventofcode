import math

data = open('data.txt').read().splitlines()

######### part one #########
total = 0
for line in data:
    dimensions = list(map(int, line.split('x')))
    l, w, h = dimensions
    surface_area = (2 * l * w) + (2 * w * h) + (2 * h * l)
    extra_paper = math.prod(sorted(dimensions)[:2])
    total += surface_area + extra_paper
print(total)

######### part two #########
total = 0
for line in data:
    dimensions = list(map(int, line.split('x')))
    wrap_length = math.prod(dimensions)
    bow_length = 2 * sum(sorted(dimensions)[:2])
    total += wrap_length + bow_length
print(total)