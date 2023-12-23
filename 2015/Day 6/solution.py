data = open('data.txt').read().splitlines()

######### part one #########
array = [['0'] * 1000 for i in range(1001)]

def boundaries(chunks, i):
    row_start = int(chunks[i].split(',')[0])
    row_end = int(chunks[i+2].split(',')[0])+1
    col_start = int(chunks[i].split(',')[1])
    col_end = int(chunks[i+2].split(',')[1])+1
    return row_start, row_end, col_start, col_end

for line in data:
    chunks = line.split()
    if chunks[0] == 'turn':
        if chunks[1] == 'on':
            row_start, row_end, col_start, col_end = boundaries(chunks, 2)
            for i in range(row_start, row_end):
                for j in range(col_start,col_end):
                    array[i][j] = '1'
        if chunks[1] == 'off':
            row_start, row_end, col_start, col_end = boundaries(chunks, 2)
            for i in range(row_start, row_end):
                for j in range(col_start,col_end):
                    array[i][j] = '0'
    if chunks[0] == 'toggle':
            row_start, row_end, col_start, col_end = boundaries(chunks, 1)
            for i in range(row_start, row_end):
                for j in range(col_start,col_end):
                    if array[i][j] == '0':
                        array[i][j] = '1'
                    else:
                        array[i][j] = '0'
on_count = 0
for i in array:
    for j in i:
        if j == '1':
            on_count += 1
print(on_count)

######### part two #########
array = [['0'] * 1000 for i in range(1001)]

for line in data:
    chunks = line.split()
    if chunks[0] == 'turn':
        if chunks[1] == 'on':
            row_start, row_end, col_start, col_end = boundaries(chunks, 2)
            for i in range(row_start, row_end):
                for j in range(col_start,col_end):
                    array[i][j] = str(int(array[i][j]) + 1)
        if chunks[1] == 'off':
            row_start, row_end, col_start, col_end = boundaries(chunks, 2)
            for i in range(row_start, row_end):
                for j in range(col_start,col_end):
                    if array[i][j] == '0':
                        continue
                    array[i][j] = str(int(array[i][j]) - 1)
    if chunks[0] == 'toggle':
            row_start, row_end, col_start, col_end = boundaries(chunks, 1)
            for i in range(row_start, row_end):
                for j in range(col_start,col_end):
                    array[i][j] = str(int(array[i][j]) + 2)
total_brightness = 0
for i in array:
    for j in i:
        total_brightness += int(j)
print(total_brightness)