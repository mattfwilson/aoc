grid = []
grid_list = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]
grid_lst = [[index, line] for index, line in enumerate(grid)]

for item in grid_lst:
    index = 0
    index_after = index + 1
    index_before = index - 1
    print(item)
    if item[0] == 0:
        print(f'current: {grid_lst[index]}, after: {grid_lst[index_after]}')
    elif item[0] == len(grid_lst):
        print(f'before: {grid_lst[index_before]}, current: {grid_lst[index]}')
    else:
        print(f'before: {grid_lst[index_before]}, current: {grid_lst[index]}, after: {grid_lst[index_after]}')

