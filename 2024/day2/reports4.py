inputs = []

with open('inputs.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip().split())

int_inputs = []

for lst in inputs:
    int_inputs.append([int(num) for num in lst])

def levels_increasing(lst):
    return all(x < y for x, y in zip(lst, lst[1:]))

def levels_decreasing(lst):
    return all(x < y for x, y in zip(lst, lst[1:]))

def levels_not_same(lst):
    return all(x != y for x, y in zip(lst, lst[1:]))

for report in int_inputs:
    if levels_not_same(report):
        pass
    else:
        int_inputs.remove(report)

for report in int_inputs:
    if levels_increasing(report):
        pass
    else:
        int_inputs.remove(report)

for report in int_inputs:
    if levels_decreasing(report):
        pass
    else:
        int_inputs.remove(report)

print(int_inputs)
print(f'len of int_inputs: {len(int_inputs)}')

