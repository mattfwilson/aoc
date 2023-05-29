import numpy as np
import sys

player_score = 0

str_inputs = np.loadtxt('inputs.csv', delimiter=' ', dtype=str)
np.set_printoptions(threshold=sys.maxsize)

str_inputs[(str_inputs == 'A') | (str_inputs == 'X')] = 1
str_inputs[(str_inputs == 'B') | (str_inputs == 'Y')] = 2
str_inputs[(str_inputs == 'C') | (str_inputs == 'Z')] = 3
int_inputs = np.int_(str_inputs)

for shape in int_inputs:
    if (shape[0] + 1) % 3 == shape[1]: # you lose
        player_score += shape[0]
        print(f'{shape} Computer wins. (+{shape[0]})')
    elif (shape[1] + 1) % 3 == shape[0]: # you win
        player_score += 6
        player_score += shape[0]
        total_score = 6 + shape[0]
        print(f'{shape} Player wins. (+{total_score})')
    elif shape[0] == shape[1]: # you tie
        player_score += 3
        player_score += shape[0]
        total_score = 3 + shape[0]
        print(f'{shape} Tie game. (+{total_score})')

print(f'Player Score: {player_score}')
