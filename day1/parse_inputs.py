blanks = 0
filled = 0
highest = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

for line in lines:
    if line.strip() == '':
        blanks += 1
    else:
        filled += 1

print(f'There are {blanks} blanks lines.')
print(f'There are {filled} filled lines.')

# for line add each line together
# if at blank line if {total} > {highest} replace [highest], then continue, else continue
