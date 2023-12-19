grid = []
inputs = [grid.append(line) for line in open('inputs.txt').read().split('\n')]
symbols = []

def find_symbols(char):
    if char.isdigit() or char == '.':
        pass
    elif char not in symbols:
        symbols.append(char)

def check_for_symbols(line, char):
    top_left, top_center, top_right = (line - 1, char - 1), (line - 1, char), (line - 1, char + 1)
    left, center, right = (char - 1), char, (char + 1)
    bottom_left, bottom_center, bottom_right = (line + 1, char - 1), (line + 1, char), (line + 1, char + 1)
    print(char)

for line in grid:
    for char in line:
        find_symbols(char)
        if not char.isnumeric() and char != '.':
            check_for_symbols(line, char)

print(symbols)
