grid = []
grid_list = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]

index = 0
index_after = index + 1
index_before = index - 1

grid_lst = [[index, line] for index, line in enumerate(grid)]

print(grid_lst)
print(len(grid_lst))

#for index in my_list:
#    if index[0] == 0:
#        print(f'current: {my_list[index]}, after: {my_list[index_after]}')
#    elif index[0] == len(my_list):
#        print(f'before: {my_list[index_before]}, current: {my_list[index]}')
#    else:
#        print(f'before: {my_list[index_before]}, current: {my_list[index]}, after: {my_list[index_after]}')

