import numpy as np
import sys

player_score = 0

str_inputs = np.loadtxt('inputs.csv', delimiter=' ', dtype=str)
np.set_printoptions(threshold=sys.maxsize)

str_inputs[(str_inputs == 'A') | (str_inputs == 'X')] = 1
str_inputs[(str_inputs == 'B') | (str_inputs == 'Y')] = 2
str_inputs[(str_inputs == 'C') | (str_inputs == 'Z')] = 3
int_inputs = np.int_(str_inputs)

for item in int_inputs:
    if (item[0] + 1) % 3 == item[1]:
        player_score += item[1]
        print(f'{item} Computer wins. (+{item[1]})')
    elif (item[1] + 1) % 3 == item[0]:
        player_score += 6
        player_score += item[1]
        total_score = 6 + item[1]
        print(f'{item} Player wins. (+{total_score})')
    elif item[0] == item[1]:
        player_score += 3
        player_score += item[1]
        total_score = 3 + item[1]
        print(f'{item} Tie game. (+{total_score})')

print(f'Player Score: {player_score}')
