grid = []
symbols = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]

for line_i, line in enumerate(grid):
    for char_i, char in enumerate(line):
        print(f'line index: {char_i}, char index: {char_i}')
        if not char.isnumeric() and char != '.' and char not in symbols:
            symbols.append(char)

print(symbols)
