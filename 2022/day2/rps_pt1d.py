import numpy as np
import sys

inputs = []
player_score = 0
shape_points = 0
line_count = 0
item_count = 0

inputs = np.loadtxt('inputs.csv', delimiter=' ', dtype=str)
for line in inputs:
    for item in line:
        item_count += 1
    line_count += 1
print(f'Line count: {line_count}')
print(f'Item_count: {item_count}')

A_convert = inputs[inputs == 'A'] = 1
B_convert = inputs[inputs == 'B'] = 2
C_convert = inputs[inputs == 'C'] = 3
X_convert = inputs[inputs == 'X'] = 1
Y_convert = inputs[inputs == 'Y'] = 2
Z_convert = inputs[inputs == 'Z'] = 3
np.set_printoptions(threshold=sys.maxsize)
print(inputs)

# for item in inputs:
#     if (item[0] + 1) % 3 == item[1]:
#         player_score += item[1]
#         print(f'Computer wins. (+{item[1]})')
#     elif (item[1] + 1) % 3 == item[0]:
#         player_score += 6
#         player_score += item[1]
#         total_score = 6 + item[1]
#         print(f'Player wins. (+{total_score})')
#     else:
#         player_score += 3
#         player_score += item[1]
#         total_score = 3 + item[1]
#         print(f'Tie game. (+{total_score})')

# print(f'Player Score: {player_score}')
