from unittest import TestCase
from RomanToInteger import RomanToInteger

class TestRomanToInteger(TestCase):
    def setUp(self) -> None:
        self.rti = RomanToInteger()
    def test_solve_problem(self):
        strs = 'XXVI'
        expected = 26

        strs = 'IX'
        expected = 9

        output = self.rti.solveProblem(strs)

        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')
