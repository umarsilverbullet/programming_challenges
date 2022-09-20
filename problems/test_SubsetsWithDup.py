from unittest import TestCase
from SubsetsWithDup import SubsetsWithDup

class TestSubsetsWithDup(TestCase):
    def setUp(self) -> None:
        self.swd = SubsetsWithDup()

    def test_solve_problem(self):
        nums = [1, 2, 2]
        output = self.swd.solveProblem(nums)
        expected = [[],[1],[1,2],[1,2,2],[2],[2,2]]

        print(f'output = {output},\n expected={expected}')
