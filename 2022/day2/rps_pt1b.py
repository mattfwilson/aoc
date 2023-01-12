split_lst = []
count = 0 
player_wins = 0
comp_wins = 0
rock = 0
paper = 0
scissors = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    split_lst.append(line.strip().split(' '))

for item in split_lst:
    count += 1

    if item[0] == 'A':
        item[0] = 1
        rock += 1
    if item[0] == 'B':
        item[0] = 2
        paper += 1
    if item[0] == 'C':
        item[0] = 3
        scissors += 1
    if item[1] == 'X':
        item[1] = 1
        rock += 1
    if item[1] == 'Y':
        item[1] = 2
        paper += 1
    if item[1] == 'Z':
        item[1] = 3
        scissors += 1

    if (item[0] + 1) % 3 == item[1]:
        print(f'Computer wins.')
        comp_wins += 1
    elif (item[1] + 1) % 3 == item[0]:
        print(f'You won!')
        player_wins += 6
        player_wins += item[1]
    else:
        print('It was a tie.')
        player_wins += 3

print(split_lst)
print(f'\nPlayer Wins: {player_wins}')
print(f'Computer Wins: {comp_wins}\n')
print(f'Rocks played: {rock}')
print(f'Papers played: {paper}')
print(f'Scissors played: {scissors}\n')
