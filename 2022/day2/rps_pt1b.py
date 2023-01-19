results = []
player_score = 0
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
        player_score += item[1]
        print(f'Computer wins. Score +{item[1]}')
    elif (item[1] + 1) % 3 == item[0]:
        player_score += 6
        player_score += item[1]
        total_score = 6 + item[1]
        print(f'Player wins. Score +{total_score}')
    else:
        player_score += 3
        player_score += item[1]
        total_score = 3 + item[1]
        print(f'Tie. Score +{total_score}')

print(f'Player Score: {player_score}')
