map_input = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'Rock', 'Y': 'paper', 'Z': 'scissors'}
shape_pts = {'rock': 1, 'paper': 2, 'scissors': 3}
game_pts = {'loss': 0, 'draw': 3, 'win': 6} 
score = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()
    rounds = [entry.strip(' ').replace(' ', '').replace('\n', '') for entry in lines]

def calc_win(opp_shape): 
    if opp_shape == 'rock':
        return shape_pts.get('paper') + 6
    elif opp_shape == 'paper':
        return shape_pts.get('scissors') + 6
    elif opp_shape == 'scissors':
        return shape_pts.get('rock') + 6

def calc_draw(opp_shape):
    if opp_shape == 'rock':
        return shape_pts.get('rock') + 1
    elif opp_shape == 'paper':
        return shape_pts.get('paper') + 1
    elif opp_shape == 'scissors':
        return shape_pts.get('scissors') + 1

def calc_loss(opp_shape):
    if opp_shape == 'rock':
        return shape_pts.get('scissors')
    elif opp_shape == 'paper':
        return shape_pts.get('rock')
    elif opp_shape == 'scissors':
        return shape_pts.get('paper')

def points_per_round(throw, score):
    opp_shape = map_input[throw[0]]
    our_shape = map_input[throw[1]]
    print(f'Opp shape: {opp_shape}') 
    print(f'Our shape: {our_shape}') 

    if our_shape == 'X':
        score += calc_win(opp_shape)
    elif our_shape == 'Y':
        score += calc_draw(opp_shape)
    else:
        score += calc_loss(opp_shape)

print('Before loop')
for throw in rounds:
    points_per_round(throw, score)
print(score)

print('End of file')
