inputs = []

with open('inputs.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip().split())

int_inputs = []

for lst in inputs:
    int_inputs.append([int(num) for num in lst])

def increase(report):
    return all(x < y for x, y in zip(report, report[1:]))

def decrease(report):
    return all(x > y for x, y in zip(report, report[1:]))

def no_dupes(report):
    return all(x != y for x, y in zip(report, report[1:]))

for report in int_inputs:
    if increase(report) or decrease(report):
        pass
    else:
        int_inputs.remove(report)

for report in int_inputs:
    if no_dupes(report):
        pass
    else:
        int_inputs.remove(report)

for i in int_inputs:
    print(increase(i))
print(f'Remaining levels: {len(int_inputs)}')

