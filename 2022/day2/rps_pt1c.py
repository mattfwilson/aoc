inputs = []
player_score = 0
shape_points = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        inputs.append(line.strip().split(' '))

def convert(pair):
    if pair[0] == 'A':
        pair[0] = 1
    if pair[0] == 'B':
        pair[0] = 2
    if pair[0] == 'C':
        pair[0] = 3
    if pair[1] == 'X':
        pair[1] = 1
    if pair[1] == 'Y':
        pair[1] = 2
    if pair[1] == 'Z':
        pair[1] = 3
    
for pair in inputs:
    convert(pair)

print(inputs)

for item in inputs:
    if (item[0] + 1) % 3 == item[1]:
        player_score += item[1]
        print(f'Computer wins. (+{item[1]})')
    elif (item[1] + 1) % 3 == item[0]:
        player_score += 6
        player_score += item[1]
        total_score = 6 + item[1]
        print(f'Player wins. (+{total_score})')
    else:
        player_score += 3
        player_score += item[1]
        total_score = 3 + item[1]
        print(f'Tie game. (+{total_score})')

print(f'Player Score: {player_score}')
