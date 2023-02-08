from unittest import TestCase
from LengthOfLongestSubstring import LengthOfLongestSubstring

class TestLengthOfLongestSubstring(TestCase):
    def setUp(self) -> None:
        self.ls = LengthOfLongestSubstring()
    def test_solve_problem(self):
        s = "abcabcbb"
        expected = 3

        output = self.ls.solveProblem(s)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')
