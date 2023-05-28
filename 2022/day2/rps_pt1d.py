import numpy as np
import sys

inputs = []
player_score = 0
shape_points = 0
line_count = 0
item_count = 0

inputs = np.loadtxt('inputs.csv', delimiter=' ', dtype=str)
inputs[(inputs == 'A') | (inputs == 'X')] = 1
inputs[(inputs == 'B') | (inputs == 'Y')] = 2
inputs[(inputs == 'C') | (inputs == 'Z')] = 3
np.set_printoptions(threshold=sys.maxsize)
int_inputs = np.int_(inputs)

for item in int_inputs:
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
