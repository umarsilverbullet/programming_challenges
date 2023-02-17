from unittest import TestCase
from ZigZigConversion import ZigZagConversion

class TestSimplifyPath(TestCase):
    def setUp(self) -> None:
        self.gp = ZigZagConversion()

    def test_solve_problem(self):
        s = "PAYPALISHIRING"
        numRows = 3
        expected = 'PAHNAPLSIIGYIR'
        output = self.gp.solveProblem(s, numRows)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')
