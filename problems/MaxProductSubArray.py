# combination sum
class MaxProductSubArray:

    def __init__(self):
        print('initialising')

    def maxProduct(self, nums: list) -> int:
        r=0
        largest = max(nums)
        curMax,curMin = 1,1

        while (r < len(nums)):

            if nums[r] == 0:
                curMax, curMin = 1, 1
                continue

            tmp = curMax
            curMax = max(curMax * nums[r], curMin * nums[r], nums[r])
            curMin = min(tmp * nums[r], curMin * nums[r], nums[r])

            r += 1
            largest = max(largest,curMax)


        return largest

