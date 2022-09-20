# combination sum
class SubsetsWithDup:
    def __init__(self):
        print('initialised')

    def solveProblem(self, nums:list):
        res = []
        subset = []
        nums.sort()
        self.backtrack(nums, res, 0, [])
        print(subset)

    def backtrack(self,nums,res,i,subset):

        if i == len( nums):
            res.append( subset.copy())
            return

        subset.append(nums[i])
        self.backtrack(nums,res,i+1,subset)

        subset.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i+=1

        self.backtrack(nums,res,i+1,subset)