'''Исходный код с обновлениями, который будет тестироваться с использованием
 class RunnerTest(unittest.TestCase)'''


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


Усэйн = Runner('Усэйн', 10)
Андрей = Runner('Андрей', 9)
Ник = Runner('Ник', 3)


'''Тестирование с дополнениями по логированию
(передача отрицательной скорости и неверного имени участника)'''

import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):

    def setUp(self):
        self.Ходьба_бег = Runner('Ходьба_бег')

    def test_walk(self):
        try:
            Ходьба = Runner('Усэйн', -10)
        except:
            logging.warning('Неверная скорость для Runner')
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            Бег = Runner('Усэйн'+1, 5)
        except:
            logging.warning('Неверный тип данных для объекта Runner')
        else:
            logging.info('"test_run" выполнен успешно')

    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')

    def test_challenge(self):
        Ходьба = Runner('Спортивная ходьба')
        Бег = Runner('Бег')
        for _ in range(10):
            Ходьба.walk()
            Бег.run()

        self.assertNotEqual(Ходьба.distance, Бег.distance)


if __name__ == '__main__':
    unittest.main()
