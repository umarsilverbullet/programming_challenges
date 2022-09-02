# combination sum
class MaxSubArray:
    def __init__(self,n):
        print('initialising')

    def solveProblem(self,nums):
        subSum = nums[0]
        curSum = 0
        # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            subSum = max(subSum, curSum)
            print(f'cur sum = {curSum}')
            print(f'sub sum = {subSum}')
        return subSum