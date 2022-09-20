from unittest import TestCase
from RecoverArray import RecoverArray

class TestRecoverArray(TestCase):
    def setUp(self) -> None:
        self.ra = RecoverArray()

    def test_solve_problem(self):
        n = 3
        sums = [-3,-2,-1,0,0,1,2,3]

        n = 2
        sums = [0,0,0,0]

        output = self.ra.solveProblem(sums,n)
        print('outp')
        expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

        print(f'output = {output},\n expected={expected}')
