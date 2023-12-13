inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
totals = {'red': 12, 'green': 13, 'blue': 14}
ids = []
red_max = 0
green_max = 0
blue_max = 0

reds = []
greens = []
blues = []

for line in inputs:
    game_id, draws = line.strip().split(': ')
    game_id = int(game_id.split(' ')[1])
    ids.append(game_id)
    draws = [[item.split(' ') for item in draw.split(', ')] for draw in draws.split('; ')]
    merged_draws = [item for sublist in draws for item in sublist]
    print(merged_draws)
    for draw in merged_draws:
        if 'red' in draw[1] and int(draw[0]) > red_max:
            red_max = int(draw[0])
            reds.append(red_max)
        if 'green' in draw[1] and int(draw[0]) > green_max:
            green_max = int(draw[0])
            greens.append(green_max)
        if 'blue' in draw[1] and int(draw[0]) > blue_max:
            blue_max = int(draw[0])
            blues.append(blue_max)

print(reds)
print(greens)
print(blues)
