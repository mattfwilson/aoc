inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
input_lst = [line for line in inputs]

str_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
str_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
replace_dict = { 'zerone': '01',
                    'twone': '21',
                    'threeight': '38',
                    'nineight': '98',
                    'eightwo': '82',
                    'eighthree': '83',
                    'sevenine': '79',
                    'fiveight': '58',
                    'oneight': '18'
                    }

test_inputs = ['soweocltwone', '2sktwoclsk5jd4fzerone2s3kthreeight', 'nineightweroizerone', 'blah']

def find_all(replace_dict, str_digits, inputs):
    output_lst = []
    for line in inputs:
        for key, val in combo_dict.items():
            if key in line:
                new_line = line.replace(key, val)
                output_lst.append(new_line)
                print(f'LINE: {new_line}, KEY: {key}, VAL: {val}')

#        for digit in str_digits:
#            if digit in line:
#                index = str(str_digits.index(digit))
#                line = line.replace(digit, index)
#                print(f'input: {line}, key: {key}, val: {val}')

    print(f'Inside outcome: {output_lst}')
    return str(line)

find_all(replace_dict, str_digits, test_inputs)
print(f'Outside outcome: {test_inputs}')
