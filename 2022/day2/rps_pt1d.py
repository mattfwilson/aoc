map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
shape_pts = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
game_pts = {'Lose': 0, 'Draw': 3, 'Win': 6}

with open('inputs.txt', 'r') as file:
    lines = file.readlines()
    rounds = [entry.strip(' ').replace(' ', '').replace('\n', '') for entry in lines]

def points_per_round(throw):
    opp_shape = map_input[throw[0]]
    our_shape = map_input[throw[1]]
    print(throw)

    if opp_shape == our_shape:
        return game_pts['Draw'] + shape_pts[our_shape]
    elif (opp_shape, our_shape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
        return game_pts['Lose'] + shape_pts[our_shape]
    else:
        return game_pts['Win'] + shape_pts[our_shape]

total = 0
for throw in rounds:
    total += points_per_round(throw)
print(total)