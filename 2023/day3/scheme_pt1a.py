schematic = []
inputs = [schematic.append(line) for line in open('inputs.txt').read().split('\n')]
symbols = []

def find_symbols(char):
    if char.isdigit() or char == '.':
        pass
    elif char not in symbols:
        symbols.append(char)

def check_for_symbols(line, index):
    top_left, top_center, top_right = (line - 1, index - 1), (line - 1, index), (line - 1, index + 1)
    left, center, right = (index - 1), index, (index + 1)
    bottom_left, bottom_center, bottom_right = (line + 1, index - 1), (line + 1, index), (line + 1, index + 1)
    print(top_left)

    return (top_left, top_center, top_right, left, center, right, bottom_left, bottom_center, bottom_right)

for line in schematic:
    for char in line:
        find_symbols(char)

for index, line in enumerate(schematic):
    print(f'index: {index}, line {line}')

