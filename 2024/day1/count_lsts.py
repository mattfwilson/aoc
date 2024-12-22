with open('inputs.txt', 'r') as file:
    col1 = []
    col2 = []

    for line in file:
        columns = line.split()
        col1.append(int(columns[0]))
        col2.append(int(columns[1]))

lst1 = sorted(col1)
lst2 = sorted(col2)

i = 0
num_i = 0
score = 0

for i in range(len(lst1)):
    res = lst2.i(lst1[i]) 
    score += lst1[i] * res
    print(f'{lst1[i]} * {res}')
    i += 1

print(f'Similarity score: {score}')
