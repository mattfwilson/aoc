blanks = 0
filled = 0
highest = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

for line in lines:
    total = 0
    print(type(line))
    if line == '':
        if total > highest:
            highest = total
        continue
    else:
        int_line = int(line)
        int_line += total
        continue

print(highest)