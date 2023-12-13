inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
totals = {'red': 12, 'green': 13, 'blue': 14}
ids = []

for line in inputs:
    game_id, draws = line.strip().split(': ')
    game_id = int(game_id.split(' ')[1])
    ids.append(game_id)
    draws = [[item.split(' ') for item in draw.split(', ')] for draw in draws.split('; ')]
    merged_draws = [item for sublist in draws for item in sublist]
    for draw in merged_draws:
        if 'red' in draw[1] and int(draw[0]) > totals['red']:
            if game_id in ids:
                ids.remove(game_id)
            else:
                continue
        if 'green' in draw[1] and int(draw[0]) > totals['green']:
            if game_id in ids:
                ids.remove(game_id)
            else:
                continue

        if 'blue' in draw[1] and int(draw[0]) > totals['blue']:
            if game_id in ids:
                ids.remove(game_id)
            else:
                continue
            
print(ids)
print(sum(ids))
