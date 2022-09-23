from unittest import TestCase
from BuyAndSellStock import BuyAndSellStock


class TestBuyAndSellStock(TestCase):
    def setUp(self) -> None:
        self.bss = BuyAndSellStock()

    def test_solve_problem(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5

        prices = [7, 6, 4, 3, 1]
        expected = 0

        prices = [2, 1, 2, 1, 0, 1, 2]
        expected = 2

        prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
        expected = 9

        output = self.bss.solveProblem(prices)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')

    def test_solve_problem2(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7

        output = self.bss.solveProblem2(prices)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')

    def test_buy_and_sell_stock_ii(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7

        output = self.bss.buyAndSellStockII(prices)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')

    def test_buy_and_sell_stock_iii(self):
        prices = [3, 3, 5, 0, 0, 3, 1, 4]
        expected = 6

        prices = [1, 2, 3, 4, 5]
        expected = 4

        # prices = [7,6,4,3,1]
        # expected = 0

        prices = [1, 4, 2]
        expected = 3

        prices = [2, 1, 2, 0, 1]
        expected = 2

        output = self.bss.buyAndSellStockIII(prices)
        print(f'output={output}')
        self.assertEqual(expected, output, f'expected = {expected}   =====    output = {output}')


