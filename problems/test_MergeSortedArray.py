from unittest import TestCase
from MergeSortedArray import MergeSortedArray

class TestSpiralMatrix(TestCase):
    def setUp(self) -> None:
        self.msa = MergeSortedArray()

    def test_solve_problem(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        expected = [1,2,2,3,5,6]

        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        expected = [1]

        nums1 = [4, 5, 6, 0, 0, 0]
        m=3
        nums2 = [1, 2, 3]
        n=3
        expected = [1, 2, 3, 4, 5, 6]
        self.msa.solveProblem(nums1, m, nums2, n)
        output = nums1
        print(f'output = {output},\n expected={expected}')
        self.assertListEqual(expected, output,
                         f"your output = {output} \n does not matchs with \n expectedOutput = {expected}")
