forwards = 0
depth = 0
aim = 0

with open('inputs.txt', 'r') as file:
    imported = file.readlines()
    inputs = [line.replace('\n', '').split(' ') for line in imported]

for pair in inputs:
    pair[1] = int(pair[1])

def move_down(direction):
    global depth
    global aim
    depth += direction[1]
    aim += direction[1]
    print(depth)
    return depth

def move_up(direction):
    global depth
    global aim
    depth -= direction[1]
    aim -= direction[1]
    print(depth)
    return depth

def move_forward(direction):
    global depth
    global forwards
    global aim
    forwards += direction[1]
    depth += aim * direction[1]
    print(forwards)
    return forwards

for direction in inputs:
    if direction[0] == 'down':
        move_down(direction)
    elif direction[0] == 'up':
       move_up(direction)
    else:
        move_forward(direction)

final_pos = forwards * depth
print(final_pos)
