inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
digit_lst = []
res_lst = []

for line in inputs:
    for char in line:
        if char in digits:
            digit_lst.append(char)
print(digit_lst)

test = [int(char) for char in inputs if char.isdigit()]
print(test)
