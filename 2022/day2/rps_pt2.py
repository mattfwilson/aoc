map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
shape_pts = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
game_pts = {'Lose': 0, 'Draw': 3, 'Win': 6} 
score = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()
    rounds = [entry.strip(' ').replace(' ', '').replace('\n', '') for entry in lines]

def calc_win(our_shape):    
    return int(shape_pts.get(our_shape) + 6)

def calc_draw(our_shape):
    return int(shape_pts.get(our_shape) + 3)

def calc_loss(our_shape):
    return int(shape_pts.get(our_shape))
    
def points_per_round(throw):
    opp_shape = map_input[throw[0]]
    our_shape = map_input[throw[1]]
    print(shape_pts.get(our_shape))
    return our_shape
    
for throw in rounds:
    points_per_round(throw)

    if our_shape == 'X':
        calc_win(our_shape)
    elif our_shape == 'Y':
        calc_draw(our_shape)
    else:
        calc_loss(our_shape)
