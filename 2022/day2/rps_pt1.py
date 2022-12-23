scores = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
