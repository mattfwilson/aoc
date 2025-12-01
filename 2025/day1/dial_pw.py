nums = list(range(100))

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
print(dial.current())
dial.move(5)
print(dial.current())
dial.move(-65)
print(dial.current())
dial.move(14)
print(dial.current())
