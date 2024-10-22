import unittest
from runner_2 import Runner, Tournament

'''
is_frozen = True: заморозить тесты
is_frozen = False: - выполнить тесты
'''


def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest(f'{method.__name__}: ''Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUp(self):
        self.Ходьба_бег = Runner("Ходьба_бег")

    @skip_if_frozen
    def test_walk(self):
        Ходьба = Runner("Спортивная ходьба")
        for _ in range(10):
            Ходьба.walk()
        self.assertEqual(Ходьба.distance, 50)

    @skip_if_frozen
    def test_run(self):
        Бег = Runner("Бег")
        for _ in range(10):
            Бег.run()
        self.assertEqual(Бег.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        Ходьба = Runner('Спортивная ходьба')
        Бег = Runner('Бег')

        for _ in range(10):
            Ходьба.walk()
            Бег.run()

        self.assertNotEqual(Ходьба.distance, Бег.distance)


if __name__ == '__main__':
    unittest.main()


class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @skip_if_frozen
    def setUp(self):
        self.Усэйн = Runner('Усэйн', 10)
        self.Андрей = Runner('Андрей', 9)
        self.Ник = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            formatted_result = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(formatted_result)

    @skip_if_frozen
    def test_usain_nick(self):
        tournament = Tournament(90, self.Усэйн, self.Ник)
        results = tournament.start()
        self.all_results.append(results)
        self.assertTrue(results[max(results.keys())] == self.Ник)

    @skip_if_frozen
    def test_andrey_nick(self):
        tournament = Tournament(90, self.Андрей, self.Ник)
        results = tournament.start()
        self.all_results.append(results)
        self.assertTrue(results[max(results.keys())] == self.Ник)

    @skip_if_frozen
    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.Усэйн, self.Андрей, self.Ник)
        results = tournament.start()
        self.all_results.append(results)
        self.assertTrue(results[max(results.keys())] == self.Ник)


if __name__ == '__main__':
    unittest.main()
