inputs = []
count = 0


with open('inputs.txt', 'r') as file:
    for line in file:
        inputs.append(line.strip().split())


for lst in inputs:
    for num in lst:
        print(num)
        num = int(num)
        count += 1

inputs[0][0] = int(inputs[0][0])

#print(inputs)
print(type(inputs[0][0]))
