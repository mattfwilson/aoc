scores = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    for char in line:
        char.replace('A', '1')
        char.replace('X', '1')
        char.replace('B', '2')
        char.replace('Y', '2')
        char.replace('C', '3')
        char.replace('Z', '3')
    print(line.strip().replace(' ', ''))

