from unittest import TestCase
from IntegerToEnglishWords import IntegerToEnglishWords

class TestIntegerToEnglishWords(TestCase):
    def setUp(self) -> None:
        self.gp = IntegerToEnglishWords()

    def test_solve_problem(self):
        num = 123
        expected = "One Hundred Twenty Three"

        # num = 12345
        # expected="Twelve Thousand Three Hundred Forty Five"
        #
        # # num = 20
        # # expected= "Twenty"
        #
        # num = 100
        # expected = 'One Hundred'

        output = self.gp.solveProblem(num)

        # num = 23
        # expected = "Twenty Three"
        # output = self.gp.solveProblem(num)

        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')

