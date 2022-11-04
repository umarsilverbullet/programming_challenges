from unittest import TestCase
from MinRotatedArray import MinRotatedArray

class TestMinRotatedArray(TestCase):
    def setUp(self) -> None:
        self.swd = MinRotatedArray()

    def test_find_min(self):
        nums = [3, 4, 5, 1, 2]
        expected =  1

        nums = [2,2,2,0,1]
        expected =  0

        nums = [3,1,3]
        expected =  1

        output = self.swd.findMin(nums)
        self.assertEqual(expected,output,f'output = {output} is not as expected = {expected}')
