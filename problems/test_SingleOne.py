from unittest import TestCase
from SingleOne import SingleOne

class TestCandy(TestCase):
    def setUp(self) -> None:
        self.bss = SingleOne()

    def test_solve_problem(self):
        nums = [2, 2, 1]
        expected =  1

        nums = [4, 1, 2, 1, 2]
        expected = 4
        output = self.bss.solveProblem(nums)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')

    def test_solve_problem_2(self):
        nums = [2, 2, 3, 2]
        expected = 3

        nums = [0,1,0,1,0,1,99]
        expected = 99

        output = self.bss.solveProblem2(nums)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')