from unittest import TestCase
from Fibonacci import Fibonacci

class TestFibonacci(TestCase):
    def setUp(self) -> None:
        self.fibonacci = Fibonacci()

    def test_solve_problem(self):
        n = 2
        expected= 1

        n=3
        expected=2

        output = self.fibonacci.fib(n)

        self.assertEqual(expected,output,f"your output = {output} \n does not matchs with \n expectedOutput = {expected}")