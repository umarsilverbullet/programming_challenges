from unittest import TestCase
from .LargestRectangleInHist import LargestRectangleInHist

class TestLargestRectangleInHist(TestCase):
    def setUp(self) -> None:
        self.lrh = LargestRectangleInHist()

    def test_solve_problem(self):
        nums = [2,1,5,6,2,3]
        self.lrh.solveProblem(nums)



    def test_next_smaller(self):
        self.fail()

    def test_prev_smaller(self):
        self.fail()
