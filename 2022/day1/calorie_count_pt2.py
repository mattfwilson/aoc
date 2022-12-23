highest = 0
total = 0
cal_lst = []

with open('inputs.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if line == '':
        print(f'EMPTY LINE - {type(line)}')
        cal_lst.append(total)
        total = 0
    if line != '':
        line = int(line)
        print(f'{line} - {type(line)}')
        total += line
            
cal_lst.sort(reverse=True)
print(cal_lst)
top_three = 0

for i in cal_lst[:3]:
    top_three += i
print(top_three)

