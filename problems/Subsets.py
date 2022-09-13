# combination sum
class Subsets:
    def __init__(self):
        print('initialised')

    def solveProblem(self,nums):
        print(nums)
        res = []
        sub_set = []
        self.subset(nums,res,sub_set,0)
        return res

    def subset(self,nums, res, sub_set, i):

        if i >= len(nums):
            res.append(sub_set.copy())
            return
        # adding to the set
        sub_set.append(nums[i])
        self.subset(nums, res, sub_set,i+1)

        # not including in the set
        sub_set.pop()
        self.subset(nums, res, sub_set,i+1)
