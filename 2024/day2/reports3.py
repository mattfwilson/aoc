inputs = []
int_inputs = []

with open('inputs.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip().split())

for lst in inputs:
    int_inputs.append([int(num) for num in lst])

print(f'int_inputs after dupe removal: {len(int_inputs)}')

for lst in int_inputs:
    valid_range = [abs(lst[i] - lst[i + 1]) for i in range(len(lst) - 1)]

    for num in valid_range:
        if 0 < num < 4:
            continue
        else:
            valid_range.remove(num)

print(f'int_inputs after range check: {len(int_inputs)}')

for lst in int_inputs:
    if all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)):
        pass
    elif all(lst[i] > lst[i + 1] for i in range(len(lst) - 1)):
        pass
    else:
        int_inputs.remove(lst)

print(f'int_inputs after increasing/decreasing check: {len(int_inputs)}')
