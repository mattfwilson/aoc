scores = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
numbered = []

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip().replace(' ', ''))
    for key, val in scores.items():
        for char in line:
            if char in key:
                with open('num_inputs.txt', 'w') as num_file:
                    num_file.write(str(val))

