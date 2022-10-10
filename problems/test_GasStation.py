from unittest import TestCase
from GasStation import GasStation

class TestGasStation(TestCase):
    def setUp(self) -> None:
        self.bss = GasStation()

    def test_solve_problem(self):
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        expected = 3

        output = self.bss.solveProblem(gas,cost)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')
