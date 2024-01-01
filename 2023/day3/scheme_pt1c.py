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

index_choice = 0
index_after = index_choice + 1
index_before = index_choice - 1

for line in my_list:
    index_choice += 1
    print(line)
#    if index_choice < 0:
#        print(f'current: {index_choice}, after: {index_after}')
#    elif index_choice == len(my_list):
#        print(f'before: {index_before}, current: {index_choice}')
#    else:
#        print(f'before: {index_before}, current: {index_choice}, after: {index_after}')
