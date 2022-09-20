# combination sum
class BuyAndSellStock:
    def __init__(self):
        print('initialise')

    def solveProblem(self,prices):
        print(f'prices = {prices}')
        maxProfit = 0
        l=0
        r=1

        for r in range(1,len(prices)):
            profit = prices[r] - prices[l]
            if prices[r] <= prices[l]:
                l = r

            maxProfit = max(maxProfit,profit)

        return maxProfit

    def solveProblem2(self,prices):
        print(f'prices = {prices}')
        maxProfit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i,len(prices)):
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit,profit)

        return maxProfit
