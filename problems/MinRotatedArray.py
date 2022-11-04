# combination sum
class MinRotatedArray:

    def __init__(self):
        print('initialising')
        a = 132600 + 2000 + 1000 + 2000 + 4500 + 6000 + 900 + 80 + 10000 + 2300 + 250 + 1000 + 40 + 200 + 13000
        b = 1600 + 1200 + 2000 + 1000 + 10000 + 2000 + 10000 + 3000 + 2000 + 18000 + 1300 + 11000 + 3250 + 2200
        c = 1500 + 5000 + 960 + 1850
        total = 275000 - (a + b + c)

        print(f'total => {a + b + c} total={total}')

    def findMin(self, nums: list) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if l == r:
                return min(res,nums[l])

            if nums[l] == nums[l + 1]:
                l = l + 1
                continue

            if nums[r] == nums[r - 1]:
                r = r - 1
                continue
            if nums[l] == nums[r]:
                l+=1
                r-=1
                continue
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (r + l) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid

        return res
    def findMinI(self, nums: list) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res,nums[l])
                break

            mid = (r+l) // 2
            res = min(res,nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res


