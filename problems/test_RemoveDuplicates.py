from unittest import TestCase
from RemoveDuplicates import RemoveDuplicates

class TestRemoveDuplicates(TestCase):
    def setUp(self) -> None:
        self.rd = RemoveDuplicates()

    def test_remove_duplicates(self):
        nums= [1, 1, 2]
        expected= 2

        nums= [0,0,1,1,1,2,2,3,3,4]
        expected= 5

        output = self.rd.removeDuplicates(nums)
        print(f'output = {nums}')

        self.assertEqual(expected, output,f"your output = {output} \n does not matchs with \n expectedOutput = {expected}")

