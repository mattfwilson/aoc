with open('inputs.txt', 'r') as file:
    directions = [int(item) for item in file.read().strip().split('\n')]
