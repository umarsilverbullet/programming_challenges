from unittest import TestCase
from ValidPalindrome import ValidPalindrome

class TestValidPalindrome(TestCase):
    def setUp(self) -> None:
        self.rd = ValidPalindrome()
    def test_is_palindrome(self):
        s = "A man, a plan, a canal: Panama"
        expected =True

        output = self.rd.isPalindrome(s)

        self.assertEqual(expected, output,f"your output = {output} \n does not matchs with \n expectedOutput = {expected}")