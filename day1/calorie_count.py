highest = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    total = 0
    line = line.strip()
    print(line)
    if line == '':
        if total > highest:
            highest = total
        else:
            continue
    else:
        line = int(line)
        line += total
        continue
    print(total)
print(highest)