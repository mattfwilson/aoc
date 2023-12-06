inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
input_lst = [line for line in inputs]
output_lst = []

str_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
str_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

words = ['2twoclsk5jd4fzerone23threeight']
temp_lst = []
result = []

for word in words:
    for index, digit in enumerate(str_digits):
        if digit in word:
            temp_lst.append(word.replace(digit, str(index)))

for i in temp_lst:
    print(i)

for string in temp_lst:
    index = 0
    while len(result) < 1:
        if string[index].isdigit():
            print(f'{string[index]} is a digit')
            result.append(int(string[index]))
        else:
            print('not a digit')
        index += 1

for string in temp_lst:
    neg_index = -1
    while len(result) < 2:
        if string[neg_index].isdigit():
            print(f'{string[neg_index]} is a digit')
            result.append(int(string[neg_index]))
        else:
            print('not a digit')
        neg_index += -1

print(result)
