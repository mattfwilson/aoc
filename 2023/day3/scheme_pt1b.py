grid = []
symbols = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]

def check_for_symbols(line, char):
    if char != '.':
        print(f'{char} - {line}')

for index, line in enumerate(grid):
    for char in line:
        check_for_symbols(line, char)
        if not char.isnumeric() and char != '.' and char not in symbols:
            symbols.append(char)

print(symbols)
