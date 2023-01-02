with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip().replace(' ', ''))
    for char in line:
        if char == 'A':
            print(f'There is an A.')
