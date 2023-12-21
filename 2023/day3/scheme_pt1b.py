grid = []
symbols = []
targets = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]

def check_for_symbols(line, char):
    return line, char

for line_i, line in enumerate(grid):
    for char_i, char in enumerate(line):
        print(f'line index: {line_i}, char index: {char_i}')
        if not char.isnumeric() and char != '.' and char not in symbols:
            symbols.append(char)
        elif char != '.' and char not in symbols:
            targets.append((char_i, char))

print(symbols)
print(targets)
