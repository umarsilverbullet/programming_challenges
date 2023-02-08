from unittest import TestCase
from ReverseWords import ReverseWords

class TestReverseWords(TestCase):

    def setUp(self) -> None:
        self.gp = ReverseWords()

    def test_solve_problem(self):
        str = "the sky is blue"
        expected = "blue is sky the"

        str = "  hello world  "
        expected = "world hello"

        output = self.gp.solveProblem(str)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')
