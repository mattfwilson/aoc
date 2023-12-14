schematic = []
inputs = [schematic.append(line) for line in open('inputs.txt').read().split('\n')]
symbols = []

def find_symbols(char):
    if char.isdigit() or char == '.':
        pass
    elif char not in symbols:
        symbols.append(char)

def check_for_symbols(line, index):
    top_left = (line - 1, index - 1)
    top_center = (line - 1, index)
    top_right = (line - 1, index + 1)
    left = (index - 1)
    center = index
    right = (index + 1)
    bottom_left = (line + 1, index - 1)
    bottom_center = (line + 1, index)
    bottom_right = (line + 1, index + 1)

    print(top_left)

    return (top_left, top_center, top_right, left, center, right, bottom_left, bottom_center, bottom_right)

for line in schematic:
    for char in line:
        find_symbols(char)

print(symbols)

for index, line in enumerate(schematic):
    print(index)
    print(f'index: {index}, line {line[0]}')

