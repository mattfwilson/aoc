inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
input_lst = [line for line in inputs]

game_index = 0
red = 0
green = 0
blue = 0

for line in input_lst:
    temp_lst = []
    temp_lst2 = []

    temp_lst.append(line)
    print(temp_lst)
    for line in temp_lst:
        line = line.strip('Game: ')
    print(line)



