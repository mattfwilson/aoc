with open('inputs.txt', 'r') as file:
    imported = file.readlines()
    lst_inputs = [line.replace('\n', '').split(' ') for line in imported]

for pair in lst_inputs:
    pair[1] = int(pair[1])

forwards = 0
ups_downs = 0

def move_sub(direction):
    global forwards
    global ups_downs
    if direction[0] == 'forward':
        forwards += direction[1]
        return forwards
    elif direction[0] == 'up':
        ups_downs += direction[1]
        return ups_downs
    else:
        ups_downs -= direction[1]
        return ups_downs

for i in lst_inputs:
    move_sub(i)
    
print(forwards)
print(ups_downs)

position = forwards * ups_downs
print(position)
