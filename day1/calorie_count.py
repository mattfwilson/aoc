highest = 0
total = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    line = int(float(line.strip()))
    print(line)
    print(type(line))
    if line == '': # if line is empty
        if total > highest: 
            highest = total # replace highest with new total
        else:
            continue
    else: # if line has a value
        line += total
    continue

print(f'Current Total: {total}')
print(f'Highest Calories: {highest}')