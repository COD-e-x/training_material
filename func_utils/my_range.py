class MyRange:
    def __init__(self, start=0, stop=0, step=1):
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


if __name__ == '__main__':
    r = MyRange(0, 10)
    # print(next(r))
    # print(r.__next__())
    # print(list(r))

    """
    Запись:
    
    iterator = r.__iter__()

    while True:
        try:
            item = iterator.__next__()
        except StopIteration:
            break
        print(item)
        
    эквивалентно записи ниже.
    """

    for item in r:
        print(item)

    """
    Итерируемый объект — это объект, который поддерживает метод __iter__(). 
        Этот метод должен возвращать объект, который можно будет использовать 
        для получения следующего элемента.
    Итератор — это объект, который поддерживает метод __next__(). 
        Он возвращает элементы один за другим, пока не достигнет конца, 
        после чего выбрасывает исключение StopIteration.
    """
