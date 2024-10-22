import unittest
from tests_12_3 import RunnerTest, TournamentTest

Загрузка = unittest.TestLoader()
Набор_тестов = unittest.TestSuite()
Набор_тестов.addTests(Загрузка.loadTestsFromTestCase(RunnerTest))
Набор_тестов.addTests(Загрузка.loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(Набор_тестов)
