import re

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

red = 12
green = 13
blue = 14

for line in inputs:
    game_id, rounds = line.strip().split(': ')
    game_id = int(game_id.split(' ')[1])

print(f'{game_id} - {type(game_id)}')
print(f'{rounds} - {type(rounds)}')
