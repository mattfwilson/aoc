import numpy as np
import sys

player_score = 0

str_inputs = np.loadtxt('inputs.csv', delimiter=' ', dtype=str)
np.set_printoptions(threshold=sys.maxsize)

str_inputs[(str_inputs == 'A') | (str_inputs == 'X')] = 1
str_inputs[(str_inputs == 'B') | (str_inputs == 'Y')] = 2
str_inputs[(str_inputs == 'C') | (str_inputs == 'Z')] = 3
int_inputs = np.int_(str_inputs)

for throw in int_inputs:
    if (throw[0] + 1) % 3 == throw[1]: # you lose
        player_score += throw[0]
        print(f'{throw} Computer wins. (+{throw[0]})')
    elif (throw[1] + 1) % 3 == throw[0]: # you win
        player_score += 6
        player_score += throw[0]
        total_score = 6 + throw[0]
        print(f'{throw} Player wins. (+{total_score})')
    elif throw[0] == throw[1]: # you tie
        player_score += 3
        player_score += throw[0]
        total_score = 3 + throw[0]
        print(f'{throw} Tie game. (+{total_score})')

print(f'Player Score: {player_score}')