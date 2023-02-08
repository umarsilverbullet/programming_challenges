from unittest import TestCase
from MinimumRemoveParenthesis import MinimumRemoveParenthesis

class TestMinimumRemoveParenthesis(TestCase):
    def setUp(self) -> None:
        self.mrp = MinimumRemoveParenthesis()
    def test_solve_problem(self):
        s = "lee(t(c)o)de)"
        expected = "lee(t(c)o)de"

        s = "a)b(c)d"
        expected = "ab(c)d"

        output = self.mrp.solveProblem(s)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')
