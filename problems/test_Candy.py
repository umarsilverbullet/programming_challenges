from unittest import TestCase
from Candy import Candy

class TestCandy(TestCase):
    def setUp(self) -> None:
        self.bss = Candy()

    def test_solve_problem(self):
        ratings = [1, 0, 2]
        expected = 5

        output = self.bss.solveProblem(ratings)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')
