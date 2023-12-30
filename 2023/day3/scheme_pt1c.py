grid = []
symbols = []
grid_lines = []
my_list = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]

for line in grid_lines:
    for char in line:
        if not char.isnumeric() and char != '.' and char not in symbols:
            symbols.append(char)

for i, value in enumerate(inputs):
    index = i
    my_list.append(value)
    print(f'Normal index: {index}')
    neg_index = i - 1
    print(f'Negative index: {neg_index}')
    pos_index = i + 1
    print(f'Positive index: {pos_index}')

print(symbols)
