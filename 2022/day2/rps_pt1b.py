with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip().replace(' ', ''))
