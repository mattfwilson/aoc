inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
input_lst = [line for line in inputs]
output_lst = []

str_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
str_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

words = ['ninel2d4oneight', 'fiveightks2d766kdzero', 'twoclsk5jd4fzerone23threeight']

for word in words:
    temp_lst = []
    for index, digit in enumerate(str_digits):
        if digit in word:
            temp_lst.append(word.replace(digit, str(index)))

    print(temp_lst)

