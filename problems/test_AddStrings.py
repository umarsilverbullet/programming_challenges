from unittest import TestCase
from AddStrings import AddStrings

class TestAddStrings(TestCase):
    def setUp(self) -> None:
        self.add_strings = AddStrings()

    def test_solve_problem(self):
        num1 = "11"
        num2 = "123"
        expected =  "134"

        output = self.add_strings.solveProblem(num1, num2)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')
