inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
input_lst = [line for line in inputs]
output_lst = []

#str_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#spelled_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

digits_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

#def replace_digits(input_lst, output_lst, digits_dict):
#    for line in input_lst:
#        for digit in digits_dict.keys():
#            print(digit_dict_keys())
#            if digit in line:
#                output_lst.append(line.replace(digit, digits_dict[digit]))
#            else:
#                continue
#
#replace_digits(input_lst, output_lst, digits_dict)

word = 'zoneight234'

for key, value in digits_dict.items():
    if key in word:
        word = word.replace(key, digits_dict[key])
print(word)
