#import libraries

#read file line by line
file = open('data.txt','r')
strings = file.read().splitlines()
file.close()

conversion_index = 0
conversion_order = ['seed-to-soil','soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
conversion_dict = {
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': []
    }        

for line in strings[2:]:
    if conversion_order[conversion_index] in line:
        current_key = conversion_order[conversion_index]
        if conversion_index < len(conversion_order)-1:
            conversion_index += 1
    elif line == '':
        continue
    else:
        values = [int(x) for x in line.split()]
        conversion_dict[current_key].append(values)

seeds = [int(x) for x in strings[0][strings[0].find(':')+1:].split()]
min_location = 0
for seed in seeds:
    current_conversion = seed
    for conversion in conversion_order:
        lists = conversion_dict[conversion]
        for list in lists:
            destination_range_start = list[0]
            source_range_start = list[1]
            range_length = list[2]
            if source_range_start <= current_conversion < source_range_start + range_length:
                current_conversion = destination_range_start - source_range_start + current_conversion
                break
    if min_location == 0:
        min_location = current_conversion
    elif current_conversion < min_location:
        min_location = current_conversion
print(min_location)


####### Part 2 #######

min_location = 0
for pair in range(len(seeds)//2):
    start_num = seeds[2*pair]
    num_range = seeds[2*pair+1]
    for seed in range(start_num, start_num + num_range):
        current_conversion = seed
        for conversion in conversion_order:
            lists = conversion_dict[conversion]
            for list in lists:
                destination_range_start = list[0]
                source_range_start = list[1]
                range_length = list[2]
                if source_range_start <= current_conversion < source_range_start + range_length:
                    current_conversion = destination_range_start - source_range_start + current_conversion
                    break
        if min_location == 0:
            min_location = current_conversion
        elif current_conversion < min_location:
            min_location = current_conversion
print(min_location)