highest = 0
total = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if line == '':
        print(f'EMPTY LINE - {type(line)}')
        if total > highest:
            highest = total
            total = 0
        else:
            total = 0
    if line != '':
        line = int(line)
        print(f'{line} - {type(line)}')
        total += line
            
print(f'Current Group Total: {total}')
print(f'Highest Calories: {highest}')