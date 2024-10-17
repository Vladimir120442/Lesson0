import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    def setUp(self):
        self.Ходьба_бег = Runner("Ходьба_бег")

    def test_walk(self):
        Ходьба = Runner("Спортивная ходьба")
        for _ in range(10):
            Ходьба.walk()
        self.assertEqual(Ходьба.distance, 50)

    def test_run(self):
        Бег = Runner("Бег")
        for _ in range(10):
            Бег.run()
        self.assertEqual(Бег.distance, 100)

    def test_challenge(self):
        Ходьба = Runner("Спортивная ходьба")
        Бег = Runner("Бег")

        for _ in range(10):
            Ходьба.walk()
            Бег.run()

        self.assertNotEqual(Ходьба.distance, Бег.distance)


if __name__ == "__main__":
    unittest.main()
