blanks = 0
filled = 0
highest = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(type(line))
    # if isinstance(line, int):
    #     print(f'Is int')    
    # else:
    #     print(f'Not int')
    print(line.strip())

for line in lines:
    total = 0
    int_line = int(line)
    print(type(int_line))
    if line.strip() == '':
        if total > highest:
            highest = total
        continue
    else:
        int_line += total
        continue

print(f'There are {blanks} blanks lines.')
print(f'There are {filled} filled lines.')

# for line add each line together
# if at blank line if {total} > {highest} replace [highest], then continue, else continue
