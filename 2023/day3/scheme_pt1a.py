schematic = []
inputs = [schematic.append(line) for line in open('inputs.txt').read().split('\n')]

symbols = []

def find_symbols(char):
    if char.isdigit() or char == '.':
        pass
    elif char not in symbols:
        symbols.append(char)

for line in schematic:
    for char in line:
        find_symbols(char)

print(symbols)
