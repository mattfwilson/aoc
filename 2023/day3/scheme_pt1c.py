grid = []
grid_list = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]
grid_lst = [[index, line] for index, line in enumerate(grid)]

print(grid_lst)

for item in grid_lst:
    index = 0
    index_after = int(index + 1)
    index_before = int(index - 1)
    count = 0
    print(item)
    if item[count] == 0:
        print(f'current: {grid_lst[index]}\nafter: {grid_lst[index_after]}\n')
        count += 1
    elif item[count] == len(grid_lst):
        print(f'before: {grid_lst[index_before]}\ncurrent: {grid_lst[index]}\n')
        count += 1
    else:
        print(f'before: {grid_lst[index_before]}\ncurrent: {grid_lst[index]}\nafter: {grid_lst[index_after]}\n')
        count += 1
