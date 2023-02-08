from unittest import TestCase
from LongestCommonPrefix import longestCommonPrefix

class TestlongestCommonPrefix(TestCase):
    def setUp(self) -> None:
        self.lcp = longestCommonPrefix()

    def test_solve_problem(self):
        strs = ["flower","flow","flight"]
        expected = "fl"
        output = self.lcp.solveProblem(strs)

        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')


