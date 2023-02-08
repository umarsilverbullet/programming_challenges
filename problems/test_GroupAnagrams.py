from unittest import TestCase
from GroupAnagrams import GroupAnagrams

class TestGroupAnagrams(TestCase):
    def setUp(self) -> None:
        self.ga = GroupAnagrams()
    def test_solve_problem(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]

        output = self.ga.solveProblem(strs)
        print(f'output={output}')
        self.assertListEqual(expected,output,f'expected = {expected}   =====    output = {output}')
