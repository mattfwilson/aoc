grid = []
symbols = []
grid_lines = []
my_list = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]

for line in grid:
    grid_lines.append(line)

for i in enumerate(grid_lines):
    value = i
    my_list.append(value)

index = 0
index_after = index + 1
index_before = index - 1


for index in my_list:
    if index == 0:
        print(f'current: {my_list[index]}, after: {my_list[index_after]}')
    elif index == len(my_list):
        print(f'before: {my_list[index_before]}, current: {my_list[index]}')
    else:
        print(f'before: {my_list[index_before]}, current: {my_list[index]}, after: {my_list[index_after]}')

print(len(my_list))
