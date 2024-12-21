lst1 = []
lst2 = []

with open("inputs.txt", "r") as file:
    line = file.read().strip('\n').split()
    lst1.append(int(line[0]))

for i in lst1:
    print(type(i))

