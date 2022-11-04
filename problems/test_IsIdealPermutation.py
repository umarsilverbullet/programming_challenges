from unittest import TestCase
from IsIdealPermutation import IsIdealPermutation

class TestIsIdealPermutation(TestCase):
    def setUp(self) -> None:
        self.iip = IsIdealPermutation()

    def test_solve_problem(self):
        nums = [1, 0, 2]
        expected = True

        nums = [2, 0, 3, 1]
        expected = False

        output = self.iip.solveProblem(nums)

        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')

