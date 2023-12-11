games = []
inputs = [games.append(line) for line in open('inputs.txt').read().strip().split('\n')]


game_index = 0
red = 0
green = 0
blue = 0

temp_lst = [line.split(': ') for line in games]
temp_lst2 = []

for line in temp_lst:
    for section in line:
        temp_lst2.append(section.split('; '))
    print(section)

for i in temp_lst2:
    print(i)

print(temp_lst2)



