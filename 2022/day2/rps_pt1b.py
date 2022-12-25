with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    for char in line:
        char.replace('A', '1')
    
    print(line.strip().replace(' ', ''))

