blanks = 0
filled = 0
highest = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

for line in lines:
    total = 0
    int_line = int(line.strip())
    if int_line == '':
        if total > highest:
            highest = total
        continue
    else:
        int_line += total
        continue

print(f'There are {blanks} blanks lines.')
print(f'There are {filled} filled lines.')