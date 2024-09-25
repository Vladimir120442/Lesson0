from threading import Thread
import time
import requests

RED = "\033[31m"
RESET = "\033[0m"
GREEN = "\033[32m"
RESET = "\033[0m"

foe_begin = 100


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.foe = foe_begin
        self.days = 0

    def run(self):
        print(f'{self.name}, {RED}на нас напали!{RESET}')
        while self.foe > 0:
            if self.foe <= 0:
                self.foe = 0
            time.sleep(1)
            self.days += 1
            self.foe -= self.power
            print(f'{self.name} сражается {self.days} дней, осталось {self.foe} врагов')
            if self.foe <= 0:
                print(f'{GREEN}{self.name} одержал победу спустя {self.days} дней(дня)!{RESET}')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'{GREEN}Все битвы закончились!{RESET}')
