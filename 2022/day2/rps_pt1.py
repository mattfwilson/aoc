scores = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
numbered = []

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip().replace(' ', ''))
    for key, val in scores.items():
        for char in line:
            if key in char:
                res = numbered.append(val)
                print(res)
