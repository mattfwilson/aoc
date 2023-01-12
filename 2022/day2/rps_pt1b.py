res_lst = []
count = 0 
player_wins = 0
comp_wins = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    res_lst.append(line.strip().split(' '))

for item in res_lst:
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
        comp_wins += 1
        print(f'Computer wins.')
    elif (item[1] + 1) % 3 == item[0]:
        player_wins += 6
        player_wins += item[1]
        print(f'Computer wins.')
    else:
        player_wins += 3
        print('It was a tie.')

print(res_lst)
print(f'\nPlayer Wins: {player_wins}')
print(f'Computer Wins: {comp_wins}\n')
