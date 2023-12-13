inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
totals = {'red': 12, 'green': 13, 'blue': 14}
ids = []
reds = []
greens = []
blues = []
mins = []

for line in inputs:
    game_id, draws = line.strip().split(': ')
    game_id = int(game_id.split(' ')[1])
    ids.append(game_id)
    draws = [[item.split(' ') for item in draw.split(', ')] for draw in draws.split('; ')]
    merged_draws = [item for sublist in draws for item in sublist]
    for draw in merged_draws:
        if 'red' in draw[1]:
            reds.append(int(draw[0]))
        if 'green' in draw[1]:
            greens.append(int(draw[0]))
        if 'blue' in draw[1]:
            blues.append(int(draw[0]))

        min_reds = min(reds)
        min_greens = min(greens)
        min_blues = min(blues)

    print(type(mins))
print(type(mins))

print(sum(mins))
