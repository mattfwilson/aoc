map_input = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
shape_pts = {'rock': 1, 'paper': 2, 'scissors': 3}
game_pts = {'lose': 0, 'draw': 3, 'win': 6} 
wins = 0
losses = 0
draws = 0

with open('inputs.txt', 'r') as file:
    lines = file.readlines()
    rounds = [entry.strip(' ').replace(' ', '').replace('\n', '') for entry in lines]

def calc_win(opp_shape):
    print('You win.')
    if opp_shape == 'rock':
        return shape_pts.get('paper') + game_pts.get('win')
    elif opp_shape == 'paper':
        return shape_pts.get('scissors') + game_pts.get('win')
    else:
        return shape_pts.get('rock') + game_pts.get('win')

def calc_draw(opp_shape):
    print('Draw.')
    if opp_shape == 'rock':
        return shape_pts.get('rock') + game_pts.get('draw')
    elif opp_shape == 'paper':
        return shape_pts.get('paper') + game_pts.get('draw')
    else:
        return shape_pts.get('scissors') + game_pts.get('draw')

def calc_loss(opp_shape):
    print('You lost')
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

    result = 0
    if our_shape == 'X':
        result = calc_loss(opp_shape)
        return result
    elif our_shape == 'Y':
        result = calc_draw(opp_shape)
        return result    
    else:
        result = calc_win(opp_shape)
        return result

total = 0
count = 0
accrued = []
for shapes in rounds:
    total += points_per_round(shapes)
    accrued.append(total)
    delta = accrued[count] - accrued[count - 1]
    assert delta <= 9
    print(f'Iteration: {count}')
    print(f'Points: {total} - Delta: {delta} \n')
    count += 1

print(f'Your score: {total}')
print(f'Total rounds: {count}')
print(f'Avg. pts per round: {total / count}')
