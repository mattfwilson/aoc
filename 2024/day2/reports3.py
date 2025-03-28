inputs = []

with open('inputs.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip().split())

int_inputs = []

for lst in inputs:
    int_inputs.append([int(num) for num in lst])

print(f'int_inputs after dupe removal: {len(int_inputs)}')

for lst in int_inputs:
    check_range = all(abs(lst[i] - lst[i + 1]) for i in range(len(lst) - 1))

    if 0 < check_range < 4:
        pass
    else:
        int_inputs.remove(lst)

print(f'int_inputs after range check: {len(int_inputs)}')

for lst in int_inputs:
    less_than = [lst[i] < lst[i + 1] for i in range(len(lst) - 1)]
    greater_than = [lst[i] > lst[i + 1] for i in range(len(lst) - 1)]
    print(less_than)
    print(greater_than)

print(f'int_inputs after increasing/decreasing check: {len(int_inputs)}')
print(int_inputs)

ui = int(input("enter num: "))

if 0 < ui < 4:
    print("in between 0 and 4")
else:
    print("outside of 0 and 4")
