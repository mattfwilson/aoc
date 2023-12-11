import re

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

red = 12
green = 13
blue = 14

for line in inputs:
    game_id, draws = line.strip().split(': ')
    game_id = int(game_id.split(' ')[1])
    games = draws.split('; ')

    #draws = [[item.split(' ') for item in draw.split(', ')] for draw in draws.split('; ')]

    for game in games:
        game.split('; ')
        for item in game.split(', '):
            item.split(' ')
        print(game)
