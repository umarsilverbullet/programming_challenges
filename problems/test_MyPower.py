from unittest import TestCase
from MyPower import MyPower

class TestMyPower(TestCase):
    def setUp(self) -> None:
        self.rd = MyPower()

    def test_my_pow(self):
        x = 2.00000
        n = 10
        expected = 1024.00000

        # x = 2.00000
        # n = 5
        # expected = 32.00000
        #
        # x = 2.00000
        # n = -2
        # expected = 0.25000


        output = self.rd.myPow(x,n)
        print(output)
        self.assertEqual(expected, output,f"your output = {output} \n does not matchs with \n expectedOutput = {expected}")