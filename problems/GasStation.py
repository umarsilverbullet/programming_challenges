# combination sum
class GasStation:
    def __init__(self):
        print('initialising')

    def solveProblem(self, gas: list, cost: list) -> int:

        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            total  += gas[i] - cost[i]

            if total < 0:
                start = i+1
                total = 0

        return start
