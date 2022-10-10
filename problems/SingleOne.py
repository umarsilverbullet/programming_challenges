# combination sum
class SingleOne:
    def __init__(self):
        print('initialising')
    #  1,2,3,4,3,2,1
    #  1,2,3,4,1,2,1
    def solveProblem(self, nums: list) -> int:

       hasMap = set()

       for i in range(len(nums)):

           if nums[i] not in  hasMap:
               hasMap.add(nums[i])
           else:
               hasMap.remove(nums[i])

       return hasMap.pop()

    def solveProblem2(self, nums):
        hasMap = {nums[i]:0 for i in range(len(nums))}

        for i in range(len(nums)):

            if hasMap[nums[i]] == 0:
                hasMap[ nums[i] ] = 1
            else:

                if hasMap[nums[i]] == 2:
                    del hasMap[nums[i]]
                else:
                    hasMap[nums[i]] = 2

        return list(hasMap).pop()