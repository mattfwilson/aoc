with open('inputs.txt', 'r') as file:
    col1 = []
    col2 = []

    for line in file:
        columns = line.split()
        col1.append(int(columns[0]))
        col2.append(int(columns[1]))

lst1 = sorted(col1)
lst2 = sorted(col2)

count = 0
total = 0

for i in range(len(lst1)):
    res = abs(lst1[count] - lst2[count])
    print(f'{lst1[count]} - {lst2[count]} = {res}')
    total += res
    count += 1

print(f'Total distance between: {total}')
