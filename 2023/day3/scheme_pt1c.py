grid = []
grid_list = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]
grid_lst = [[index, line] for index, line in enumerate(grid)]

print(grid_lst)

for item in grid_lst:
    index = 0
    index_after = index + 1
    index_before = index - 1

    if item[index] == 0:
        print(f'current: {grid_lst[index]}\nafter: {grid_lst[index_after]}\n')
    elif item[index] >= len(grid_lst):
        print(f'before: {grid_lst[index_before]}\ncurrent: {grid_lst[index]}\n')
    else:
        print(f'before: {grid_lst[index_before]}\ncurrent: {grid_lst[index]}\nafter: {grid_lst[index_after]}\n')
    index += 1
