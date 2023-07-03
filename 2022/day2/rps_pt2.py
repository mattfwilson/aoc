map_input = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
shape_pts = {'rock': 1, 'paper': 2, 'scissors': 3}
game_pts = {'lose': 0, 'draw': 3, 'win': 6} 

with open('inputs.txt', 'r') as file:
    lines = file.readlines()
    rounds = [entry.strip(' ').replace(' ', '').replace('\n', '') for entry in lines]

def calc_win(opp_shape):
    print('You win.')
    match opp_shape:
        case 'rock':
            return shape_pts.get('paper') + game_pts.get('win')
        case 'paper':
            return shape_pts.get('scissors') + game_pts.get('win')
        case 'scissors':
            return shape_pts.get('rock') + game_pts.get('win')

def calc_draw(opp_shape):
    print('Draw.')
    match opp_shape:
        case 'rock':
            return shape_pts.get('rock') + game_pts.get('draw')
        case 'paper':
            return shape_pts.get('paper') + game_pts.get('draw')
        case 'scissors':
            return shape_pts.get('scissors') + game_pts.get('draw')

def calc_loss(opp_shape):
    match opp_shape:
        case 'rock':
            return shape_pts.get('scissors')
        case 'paper':
            return shape_pts.get('rock')
        case 'scissors':
            return shape_pts.get('paper')

def points_per_round(throw):
    opp_shape = map_input[throw[0]]
    our_shape = map_input[throw[1]]
    print(f'{opp_shape} ({throw[0]}) vs {our_shape} ({throw[1]})') 

    result = 0
    match our_shape:
        case 'X':
            result = calc_loss(opp_shape)
            return result
        case 'Y':
            result = calc_draw(opp_shape)
            return result
        case 'Z':
            result = calc_win(opp_shape)
            return result

total = 0
count = 0
accrued = []
for throw in rounds:
    total += points_per_round(throw)
    accrued.append(total)
    delta = accrued[count] - accrued[count - 1]
    assert delta <= 9
    print(f'Iteration: {count}')
    print(f'Points: {total} - Delta: {delta} \n')
    count += 1

print(f'Your score: {total}')
print(f'Total rounds: {count}')
print(f'Avg. pts per round: {total / count}')
