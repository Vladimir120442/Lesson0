class StepValueError(ValueError):
    pass

class ValuecycleError(Exception):
    def __init__(self, message):
        self.message = message

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равным 0')

        if (start >= stop and step > 0) or (start <= stop and step < 0):
            raise ValuecycleError('Финиш, старт и направление бега перепутаны :)')

        pointer = 0
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = pointer

    def __iter__(self):
        self.pointer = self.start
        return(self)

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration()
        result = self.pointer
        self.pointer += self.step
        return result


RED = '\033[42m'
UNDERLINE = '\033[93m'  # '\033[4m'
RESET = '\033[0m'
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as e:
    print(f'{e}')

try:
    iter2 = Iterator(-5, 1)
    for i in iter2:
        print(i, end=' ')
except ValuecycleError as e:
    print(e.message)
else:
    print()
    print(f'{RED}Успешная итерация{RESET}')

try:
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')
except ValuecycleError as e:
    print(e.message)
else:
    print()
    print(f'{RED}Успешная итерация{RESET}')

try:
    iter4 = Iterator(5, 1, -1)
    for i in iter4:
        print(i, end=' ')
except ValuecycleError as e:
    print(e.message)
else:
    print()
    print(f'{RED}Успешная итерация{RESET}')

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
except ValuecycleError as e:
    print(e.message)
else:
    print(f'Успешная итерация{iter5}')
