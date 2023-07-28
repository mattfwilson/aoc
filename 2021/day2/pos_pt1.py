forwards = 0
ups = 0
downs = 0

with open('inputs.txt', 'r') as file:
    imported = file.readlines()
    lst_inputs = [line.replace('\n', '').split(' ') for line in imported]
<<<<<<< HEAD

for pair in lst_inputs:
    pair[1] = int(pair[1])

forwards = 0
up_down = 0

def move_sub(direction):
    global forwards
    global up_down
    if direction[0] == 'forward':
        forwards += direction[1]
        return forwards
    elif direction[0] == 'up':
        up_down -= direction[1]
        return up_down
    else:
        up_down += direction[1]
        return up_down

for i in lst_inputs:
    move_sub(i)
    
print(forwards)
print(up_down)

position = forwards * up_down
print(position)
=======
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
>>>>>>> ac991efb7198e3c4ab09d749561f854b4e24f2ac
