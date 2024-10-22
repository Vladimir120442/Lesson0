import unittest
from runner_2 import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.Усэйн = Runner('Усэйн', 10)
        self.Андрей = Runner('Андрей', 9)
        self.Ник = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for elem in cls.all_results:
            console = '{' + ', '.join(f'{key}: {value}' for key, value in elem.items()) + '}'
            print(console)

    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.Усэйн, self.Ник)
        results = tournament.start()
        self.all_results.append(results)
        self.assertTrue(results[max(results.keys())] == self.Ник)

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.Андрей, self.Ник)
        results = tournament.start()
        self.all_results.append(results)
        self.assertTrue(results[max(results.keys())] == self.Ник)

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.Усэйн, self.Андрей, self.Ник)
        results = tournament.start()
        self.all_results.append(results)
        self.assertTrue(results[max(results.keys())] == self.Ник)


if __name__ == '__main__':
    unittest.main()
