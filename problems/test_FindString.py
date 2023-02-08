from unittest import TestCase
from FindString import FindStringInString


class TestFindStringInString(TestCase):
    def setUp(self) -> None:
        self.strStr = FindStringInString()
    def test_solve_problem(self):

        haystack = "leetcode"
        needle = "leeto"
        expected = -1

        # haystack = "sadbutsad"
        # needle = "sad"
        # expected = 0

        haystack ="mississippi"
        needle = "issip"
        expected = 4

        # haystack = "aaa"
        # needle = "aaaa"
        # expected = 0

        output = self.strStr.solveProblem(haystack,needle)


        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')
