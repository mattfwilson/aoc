forwards = 0
depth = 0
aim = 0

with open('inputs.txt', 'r') as file:
    imported = file.readlines()
    inputs = [line.replace('\n', '').split(' ') for line in imported]

for pair in inputs:
    pair[1] = int(pair[1])

def move_sub(direction):
    global depth
    global forwards
    global aim
    if direction[0] == 'down':
        aim += direction[1]
        print(depth)
        return aim
    elif direction[0] == 'up':
        aim -= direction[1]
        print(depth)
        return aim
    else:
        if aim == 0:
            forwards += direction[1]
            return forwards
        else:
            forwards += direction[1]
            depth += aim * direction[1]
            print(forwards)
            return forwards

for direction in inputs:
    move_sub(direction)

final_pos = forwards * depth
print(final_pos)
