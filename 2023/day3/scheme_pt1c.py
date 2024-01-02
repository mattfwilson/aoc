grid = []
grid_list = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]

grid_lst = [[index, line] for index, line in enumerate(grid)]

print(grid_lst)

for item in grid_lst:
    for i in item:
        index = 0
        index_after = index + 1
        index_before = index - 1
        print(i)
        if i[0] == 0:
            print(f'current: {grid_lst[index]}, after: {grid_lst[index_after]}')
        elif i[0] == len(grid_lst):
            print(f'before: {grid_lst[index_before]}, current: {grid_lst[index]}')
        else:
            print(f'before: {grid_lst[index_before]}, current: {grid_lst[index]}, after: {grid_lst[index_after]}')

