# combination sum
class RemoveDuplicates:
    def __init__(self):
        print('initialising')

    def removeDuplicates(self, nums: list) -> int:

        r,l = 1,1

        while (r < len(nums)):

            if nums[r] == nums[r-1]:
                r+=1
            else:
                nums[l] = nums[r]
                l+=1
                r+=1


        return l

