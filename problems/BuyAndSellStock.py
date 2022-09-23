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
        dp = [[-1 for j in range(2)] for k in  range( len(prices))]
        maxProfit = self.solveStockII(prices,0,1,dp);
        return maxProfit


        maxProfit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i,len(prices)):
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit,profit)

        return maxProfit

    def buyAndSellStockII(self,prices):
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] >= prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit

    def buyAndSellStockIII(self,prices):
        limit = 2
        dp = [[ [-1 for k in range(3)] for j in range(2) ]  for i in range(len(prices))]
        maxProfit = self.solveStockIII(prices, 0, 1, 2, dp)
        return maxProfit

        #  other non-working method which did not work.
        totalProfit = 0
        transactions = 2
        l = 0
        r = 1
        for i in range(transactions):
            r = l+1
            profit = 0
            while r < len(prices):

                if prices[r] < prices[l]:
                    totalProfit += profit
                    l = r
                    break
                else:
                    profit = max(profit,prices[r] - prices[l])

                r+=1

            if r >= len(prices):
                totalProfit += profit
                break

        return totalProfit

    def solveStockIII(self,prices,index,buy,limit,dp):

        if index == len(prices):
            return 0

        if limit == 0:
            return 0

        if dp[index][buy][limit] != -1:
            return dp[index][buy][limit]

        profit =0

        if (buy):
            buyProfit = -prices[index] + self.solveStockIII(prices, index+1, 0, limit, dp)
            skipBuyProfit = 0 + self.solveStockIII(prices, index+1, 1, limit, dp)
            profit = max(buyProfit,skipBuyProfit)
        else:
            sellProfit = prices[index] + self.solveStockIII(prices, index+1, 1, limit-1, dp)
            skipSellProfit = 0 + self.solveStockIII(prices, index+1, 0, limit, dp)
            profit = max(sellProfit, skipSellProfit)

        dp[index][buy][limit] = profit
        return profit

    # Does not work till now
    def solveStockII(self,prices, index, buy, dp):
        print(f'dp === {dp}')
        if index == len(prices):
            return 0

        if dp[index][buy] != -1:
            return dp[index][buy]

        profit = 0
        if buy:
            buyAtIndex = -prices[index] + self.solveStockII(prices,index+1,0,dp)
            skipBuyAtIndex = 0 + self.solveStockII(prices,index+1,0,dp)
            profit = max(buyAtIndex,skipBuyAtIndex)
        else:
            sellAtIndex = prices[index] + self.solveStockII(prices, index+1, 1,dp)
            skipSellAtIndex = 0 + self.solveStockII(prices, index+1, 0,dp)
            profit = max(sellAtIndex, skipSellAtIndex)

        print(f" dp [{index}][{buy}] = {dp[index][buy]}");
        dp[index][buy] = profit
        return profit