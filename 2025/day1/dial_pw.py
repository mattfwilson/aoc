nums = list(range(100))
zeroes = 0
inputs = []

with open('inputs.txt', 'r') as file:
    for line in file:
        clean = line.strip()
        inputs.append(clean)

class CycleList:
    def __init__(self, lst):
        self.lst = lst
        self.idx = 50

    def move(self, steps):
        self.idx = (self.idx + steps) % len(self.lst)
        return self.lst[self.idx]

    def current(self):
        return self.lst[self.idx]
 
dial = CycleList(nums)
nums_lst = [(val[0], int(val[1:])) for val in inputs]

for direction, amount in nums_lst:
    print(direction, amount)
    step = -amount if direction == 'L' else amount
    dial.move(step)

    if dial.current() == 0:
        zeroes += 1

print(zeroes)
