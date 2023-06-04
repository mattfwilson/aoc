map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
shape_pts = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
game_pts = {'Lose': 0, 'Draw': 3, 'Win': 6} 
score = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()
    rounds = [entry.strip(' ').replace(' ', '').replace('\n', '') for entry in lines]

def calc_win(opp_shape):    
    print(opp_shape)
    if opp_shape == 'Rock':
        return shape_pts.get('Paper') + 6
    elif opp_shape == 'Paper':
        return shape_pts.get('Scissors') + 6
    elif opp_shape == 'Scissors':
        return shape_pts.get('Rock') + 6

def calc_draw(opp_shape):
    print(opp_shape)
    if opp_shape == 'Rock':
        return shape_pts.get('Rock') + 1
    elif opp_shape == 'Paper':
        return shape_pts.get('Paper') + 1
    elif opp_shape == 'Scissors':
        return shape_pts.get('Scissors') + 1

def calc_loss(opp_shape):
    print(opp_shape)
    if opp_shape == 'Rock':
        return shape_pts.get('Scissors')
    elif opp_shape == 'Paper':
        return shape_pts.get('Rock')
    elif opp_shape == 'Scissors':
        return shape_pts.get('Paper')

def points_per_round(throw):
    opp_shape = map_input[throw[0]]
    our_shape = map_input[throw[1]]
    
    if our_shape == 'X':
        calc_win(opp_shape)
    elif our_shape == 'Y':
        calc_draw(opp_shape)
    else:
        calc_loss(opp_shape)

for throw in rounds:
    score = sum(points_per_round(throw))
print(score)
