split_lst = []
count = 0 
wins = 0
losses = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    split_lst.append(line.strip().split(' '))

for item in split_lst:
    count += 1

    if item[0] == 'A':
        item[0] = 1
    if item[0] == 'B':
        item[0] = 2
    if item[0] == 'C':
        item[0] = 3
    if item[1] == 'X':
        item[1] = 1
    if item[1] == 'Y':
        item[1] = 2
    if item[1] == 'Z':
        item[1] = 3

    if (item[0] + 1) % 3 == item[1]:
        print(f'You lost.')
        losses += 1
    elif (item[1] + 1) % 3 == item[0]:
        print(f'You won!')
        wins += 1
    else:
        print('It was a tie.')

print(split_lst)
print(f'Wins: {wins}')
print(f'Losses: {losses}')