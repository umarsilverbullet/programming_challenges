from unittest import TestCase
from Traingle import Triangle

class TestTriangle(TestCase):
    def setUp(self) -> None:
        self.ra = Triangle()

    def test_solve_problem(self):
        triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        expected = 11

        triangle = [[-1], [2, 3], [1, -1, -3]]
        expected = -1

        output = self.ra.solveProblem(triangle)
        self.assertEqual(expected,output,f'expected = {expected}   =====    output = {output}')