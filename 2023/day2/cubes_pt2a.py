import math

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
totals = {'red': 12, 'green': 13, 'blue': 14}
ids = []
red_max = 0
green_max = 0
blue_max = 0
summed = 0

for line in inputs:
    game_id, draws = line.strip().split(': ')
    game_id = int(game_id.split(' ')[1])
    ids.append(game_id)
    draws = [[item.split(' ') for item in draw.split(', ')] for draw in draws.split('; ')]
    merged_draws = [item for sublist in draws for item in sublist]
    print(f'MERGED DRAWS: {merged_draws}')

    for draw in merged_draws:
        print(f'DRAW: {draw}')
        if draw[1] == 'red' and int(draw[0]) > red_max:
            red_max = int(draw[0])
        if draw[1] == 'green' and int(draw[0]) > green_max:
            green_max = int(draw[0])
        if draw[1]  == 'blue' and int(draw[0]) > blue_max:
            blue_max = int(draw[0])
        print(f'reds: {red_max}, greens: {green_max}, blues: {blue_max}')
    summed += red_max * green_max * blue_max
    red_max = 0
    green_max = 0
    blue_max = 0

print(f'Sum of powers: {summed}')
