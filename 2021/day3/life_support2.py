from collections import Counter

index = 0

inputs = [line for line in open('inputs.txt').read().strip().split('\n')]

while index < len(inputs[0]):
    print(Counter(binary[index] for binary in inputs).most_common()[0])
    index += 1
