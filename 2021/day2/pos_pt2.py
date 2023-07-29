forwards = 0
up_down = 0
aim = 0

with open('inputs.txt', 'r') as file:
    imported = file.readlines()
    inputs = [line.replace('\n', '').split(' ') for line in imported]

for pair in inputs:
    pair[1] = int(pair[1])

def move_down(direction, up_down):
    up_down += direction[1]
    aim += direction[1]
    print(up_down)
    return up_down

def move_up(direction, up_down):
    up_down -= direction[1]
    aim -= direction[1]
    print(up_down)
    return up_down

def move_forward(direction, forwards, up_down):
    forwards += direction[1]
    up_down += aim * direction[1]
    print(forwards)
    return forwards

for direction in inputs:
    move_sub(direction, forwards, up_down)
    
print(forwards)
print(up_down)

position = forwards * up_down
print(position)
