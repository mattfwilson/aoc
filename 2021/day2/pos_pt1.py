forwards = 0
up_down = 0

with open('inputs.txt', 'r') as file:
    imported = file.readlines()
    lst_inputs = [line.replace('\n', '').split(' ') for line in imported]

for pair in lst_inputs:
    pair[1] = int(pair[1])

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
