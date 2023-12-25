grid = []
symbols = []
targets = []
grid_lines = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]

def check_for_symbols(line_i, line, char_i, char):
    if char.isnumeric():
        return char
    return line

for line_i, line in enumerate(grid):
    for char_i, char in enumerate(line):
        print(f'line index: {line_i}, char index: {char_i}')
        if not char.isnumeric() and char != '.' and char not in symbols:
            symbols.append(char)
        elif char != '.' and char not in symbols:
            check_for_symbols(line_i, line, char_i, char)
            targets.append((line_i, char_i))

for line_i, line in enumerate(grid):
    grid_lines.append(line)

print(grid_lines)
