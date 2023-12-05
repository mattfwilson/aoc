inputs = [line for line in open('inputs.txt').read().strip().split('\n')]
input_lst = [line for line in inputs]
output_lst = []

str_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

words = ['ninel2d4oneight', 'fiveightks2d766kdzero', 'twoclsk5jd4fzerone23threeight']

for word in words:
    temp_lst = []
    for index, digit in enumerate(str_digits):
        if digit in word:
            word = word.replace(digit, str(index))
            temp_lst.append(word)
    print(temp_lst)

