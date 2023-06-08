map_input = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
shape_pts = {'rock': 1, 'paper': 2, 'scissors': 3}
game_pts = {'lose': 0, 'draw': 3, 'win': 6} 

with open('inputs.txt', 'r') as file:
    lines = file.readlines()
    rounds = [entry.strip(' ').replace(' ', '').replace('\n', '') for entry in lines]

def calc_win(opp_shape):
    if opp_shape == 'rock':
        return shape_pts.get('paper') + game_pts.get('win')
    elif opp_shape == 'paper':
        return shape_pts.get('scissors') + game_pts.get('win')
    else:
        return shape_pts.get('rock') + game_pts.get('win')

def calc_draw(opp_shape):
    if opp_shape == 'rock':
        return shape_pts.get('rock') + game_pts.get('draw')
    elif opp_shape == 'paper':
        return shape_pts.get('paper') + game_pts.get('draw')
    else:
        return shape_pts.get('scissors') + game_pts.get('draw')

def calc_loss(opp_shape):
    if opp_shape == 'rock':
        return shape_pts.get('scissors')
    elif opp_shape == 'paper':
        return shape_pts.get('rock')
    else:
        return shape_pts.get('paper')

def points_per_round(shapes):
    opp_shape = map_input[shapes[0]]
    our_shape = map_input[shapes[1]]
    print(f'{opp_shape} ({shapes[0]}) vs {our_shape} ({shapes[1]})') 

    if our_shape == 'X':
        return calc_loss(opp_shape)
    elif our_shape == 'Y':
        return calc_draw(opp_shape)
    else:
        return calc_win(opp_shape)

score = 0
for shapes in rounds:
    score += points_per_round(shapes)
    print(score)
print(f'Your score: {score}')

