map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
shape_pts = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
game_pts = {'Lose': 0, 'Draw': 3, 'Win': 6}

with open('inputs.txt', 'r') as file:
    lines = file.readlines()
    rounds = [entry.strip(' ').replace(' ', '').replace('\n', '') for entry in lines]

def calc_outcome(opp_shape):    
    if opp_shape == 'Rock':
        pass
    elif opp_shape == 'Scissors':
        pass
    else: 
        pass

def points_per_round(throw):
    opp_shape = map_input[throw[0]]
    our_shape = map_input[throw[1]]
    print(throw)
       
    if our_shape == 'X': # need to lose
        calc_outcome()
    elif our_shape == 'Y': # need to draw
        calc_outcome()
    else: # need to win
        calc_outcome()

total = 0
for throw in rounds:
    total += points_per_round(throw)
print(total)