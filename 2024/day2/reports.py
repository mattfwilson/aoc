inputs = []
int_inputs = []
count = 0


with open('inputs.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip().split())

int_inputs = [(lst, int(num)) for lst in inputs for num in lst]

for lst in inputs:
    print(lst)


for lst in int_inputs:
    for num in lst:
        print(type(num))

print(type(int_inputs[0][0]))
print(type(int_inputs[1][1]))


