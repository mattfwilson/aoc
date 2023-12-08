games = []
inputs = [games.append(line) for line in open('inputs.txt').read().strip().split('\n')]

game_index = 0
red = 0
green = 0
blue = 0

for line in games:
    line = line.strip('Game: ')
    print(line)
