grid = []
symbols = []
grid_lines = []
my_list = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]
index = 0
index_after = index + 1
index_before = index - 1

for line in grid:
    grid_lines.append(line)

for i in enumerate(grid_lines):
    val = i
    my_list.append(val)

for index in my_list:
    if index[0] == 0:
        print(f'current: {my_list[index]}, after: {my_list[index_after]}')
    elif index[0] == len(my_list):
        print(f'before: {my_list[index_before]}, current: {my_list[index]}')
    else:
        print(f'before: {my_list[index_before]}, current: {my_list[index]}, after: {my_list[index_after]}')

