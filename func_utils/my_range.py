class MyRange:

    def __init__(self, start=0, stop=0, step=0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        raise StopIteration


# x = list(MyRange(0, 5, 2))
x = MyRange(0, 5, 2)
# print(x.__next__())
# print(next(x))
print(list(x))