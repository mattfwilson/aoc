blanks = 0
filled = 0

with open('inputs.txt', 'r', encoding="utf-8") as file:
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