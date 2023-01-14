results = []
player_wins = 0
shape_points = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    results.append(line.strip().split(' '))

for item in results:
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

for item in results:
    if (item[0] + 1) % 3 == item[1]:
        shape_points += item[1]
        print(f'Computer wins.')
    elif (item[1] + 1) % 3 == item[0]:
        player_wins += 6
        shape_points += item[1]
        print(f'Player wins.')
    else:
        player_wins += 3
        shape_points += item[1]
        print('It was a tie.')

print(results)
print(f'\nShape points: {shape_points}')
print(f'Player Wins: {player_wins}')
