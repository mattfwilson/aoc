from itertools import chain

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
totals = {'red': 12, 'green': 13, 'blue': 14}

for line in inputs:
    game_id, draws = line.strip().split(': ')
    game_id = int(game_id.split(' ')[1])
    draws = [[item.split(' ') for item in draw.split(', ')] for draw in draws.split('; ')]
    merged_draws = [item for sublist in draws for item in sublist]
    print(f'Game {game_id} - {merged_draws}\n')
    for draw in merged_draws:
        if 'red' in draw[1]:
            if int(draw[0]) > totals['red']:
                print(f'Game id {game_id}')

   
