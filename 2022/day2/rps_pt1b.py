with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    for char in line:
        if char == 'A':
            char.replace('A', '1')
        if char == 'B':
            char.replace('A', '2')
        if char == 'C':
            char.replace('A', '3')
        if char == 'X':
            char.replace('A', '1')
        if char == 'Y':
            char.replace('A', '2')
        if char == 'Z':
            char.replace('A', '3')
    
    print(line.strip().replace(' ', ''))

