inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
input_lst = [line for line in inputs]
output_lst = []

str_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
str_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

words = ['twoclsk5jd4fzerone23threeight']

for line in words:
    for digit in str_digits:
        output_lst.append(line.find(digit))
    print(output_lst)
