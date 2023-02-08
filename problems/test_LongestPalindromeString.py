from unittest import TestCase
from LongestPalindromeString import LongestPalindromeString

class TestLengthOfLongestSubstring(TestCase):
    def setUp(self) -> None:
        self.lps = LongestPalindromeString()
    def test_solve_problem(self):
        s = "babad"
        expected = "bab"

        s = "cbbd"
        expected= 'bb'

        output = self.lps.solveProblem(s)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')
