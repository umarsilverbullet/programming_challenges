from unittest import TestCase
from MaximalRectangle import MaximalRectangle

class TestMaximalRectangle(TestCase):
    def setUp(self) -> None:
        self.maxRect = MaximalRectangle()

    def test_solve_problem(self):
        matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        output = self.maxRect.solveProblem(matrix)
        expected = 6
        self.assertEqual(expected,output,f"your output = {output} \n does not matchs with \n expectedOutput = {expected}")
