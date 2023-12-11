import re

games = []
inputs = [games.append(line) for line in open('inputs.txt').read().strip().split('\n')]

game_index = 0
red = 0
green = 0
blue = 0

def extract(string):
    return ''.join(re.findall(r'\d', string))

sep_games = []

for string in games:
    sep_games.append(re.split(': |; ', string))

print(sep_games)

for i in sep_games:
    print(i)

#for lst in sep_games:
#    for line in lst:
#        line = re.sub(r'Game ', '', string)
#print(sep_games)

