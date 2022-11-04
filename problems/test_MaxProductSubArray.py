from unittest import TestCase
from MaxProductSubArray import MaxProductSubArray

class TestMaxProductSubArray(TestCase):
    def setUp(self) -> None:
        self.swd = MaxProductSubArray()

    def test_max_product(self):
        nums = [2, 3, -2, 4]
        expected =  6

        nums = [3,-1,4]
        expected =  4

        nums = [2,-5,-2,-4,3]
        expected =  24

        # nums = [-2, 3, -4]
        # expected =  24
        #
        # nums = [0,2]
        # expected =  2

        output = self.swd.maxProduct(nums)

        self.assertEqual(expected,output,f'output = {output} is not as expected = {expected}')
