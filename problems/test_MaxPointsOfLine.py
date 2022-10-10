from unittest import TestCase
from MaxPointsOfLine import MaxPointsOfLine

class TestCandy(TestCase):
    def setUp(self) -> None:
        self.bss = MaxPointsOfLine()

    def test_solve_problem(self):
        points = [[1,1],[2,2],[3,3]]
        expected = 3

        points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
        expected = 4

        output = self.bss.solveProblem(points)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')
