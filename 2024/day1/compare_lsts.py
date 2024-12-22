inputs = []
lst1 = []
lst2 = []

inputs = [lst1.append(line) for line in open('inputs.txt').read().strip().split('\n')]
lst1 = [lst2.append(int(line)) for line in inputs]

for string in inputs:
    int(string)

print(type(lst1[0]))


#with open("inputs.txt", "r") as file:
#    for line in file:
#        line = file.read().strip('\n').split()
#        inputs.append(int(line[0]))


#lst1 = [inputs[i] for i in range(len(inputs)) if i % 2 == 0]
#lst2 = [inputs[i] for i in range(len(inputs)) if i % 2 != 0]

