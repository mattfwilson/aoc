forwards = 0
ups = 0
downs = 0

with open('inputs.txt', 'r') as file:
    imported = file.readlines()
    lst_inputs = [line.replace('\n', '').split(' ') for line in imported]
    print(dict_inputs)
    counter = 0
    for key_val in lst_inputs:
        counter += 1
        dict_inputs[key_val[0]] = key_val[1]
        print(key_val)
    print(counter)
    print(dict_inputs)

def move_sub(direction):
    if direction[0] == 'forward':
        return forwards += direction[1]
    elif direction[0] == 'up':
        return ups += direction[1]
    else:
        return downs -= direction[1]

for pair in lst_inputs:
    pair[1] = int(pair[1])

for action in lst_inputs:
    print(type(action[0]))
    print(type(action[1]))

print(forwards)
print(ups)
print(downs)
