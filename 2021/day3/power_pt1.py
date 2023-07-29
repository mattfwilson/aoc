inputs = []

with open('inputs.txt', 'r') as file:
    imported = file.readlines()
    stripped = [line.replace('\n', '').split(' ') for line in imported]

print(stripped)

for item in stripped:
    print(item)
    inputs.append(item[0])

print(inputs)
