inputs = []
int_inputs = []


with open('inputs.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip().split())

def has_dupes(lst):
    return len(lst) != len(set(lst))

# convert strs to ints
for lst in inputs:
    int_inputs.append([int(num) for num in lst])

print(f'int_inputs: {len(int_inputs)}')

# remove lsts that have dupes
for lst in int_inputs:
    if has_dupes(lst):
        int_inputs.remove(lst)

print(f'int_inputs after dupe removal: {len(int_inputs)}')

# remove lsts not in valid range
for lst in int_inputs:
    valid_range = all(abs(lst[i] - lst[i + 1]) for i in range(len(lst) - 1))

    if 0 > valid_range < 4:
        pass
    else:
        int_inputs.remove(lst)

print(f'int_inputs after range check: {len(int_inputs)}')

# remove lsts that are not strictly increasing/decreasing
for lst in int_inputs:
    if all(lst[i] < lst[i + 1] for i in range(len(lst) - 1)):
        pass
    elif all(lst[i] > lst[i + 1] for i in range(len(lst) - 1)):
        pass
    else:
        int_inputs.remove(lst)

print(f'int_inputs after increasing/decreasing check: {len(int_inputs)}')
