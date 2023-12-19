import hashlib

data = open('data.txt').read()

######### part one #########

int_to_add = 1
not_found_hash = False

while True:
    string_to_hash = data + str(int_to_add)
    hash_output = hashlib.md5(string_to_hash.encode('utf-8')).hexdigest()
    if hash_output[:5] == '00000':
        break
    int_to_add += 1
print(int_to_add)

######### part two #########

int_to_add = 1
not_found_hash = False

while True:
    string_to_hash = data + str(int_to_add)
    hash_output = hashlib.md5(string_to_hash.encode('utf-8')).hexdigest()
    if hash_output[:6] == '000000':
        break
    int_to_add += 1
print(int_to_add)