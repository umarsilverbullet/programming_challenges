# combination sum
from collections import Counter
class RecoverArray:
    def __init__(self):
        print('initialised')

    def findGivenSubsetSum(self, nums:list, n:int):
        res = []
        subset = []
        nums.sort()
        self.backtrack(nums, res, 0, [],n)
        print(subset)
        return res

    def backtrack2(self,nums,res,i,subset,n):

        if i == len( nums):
            if len(subset) == n and sum(subset) == 0:
                print(f'subset with {n} size {subset}')
                res.append( subset.copy())
                return subset
            return []

        subset.append(nums[i])
        include = self.backtrack(nums, res, i+1, subset, n)

        if(len(include) == n):
            return include


        subset.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i+=1

        exclude = self.backtrack(nums,res,i+1,subset, n)
        if (len(exclude) == n):
            return exclude

        return []

    # ======================================================================================

    def solveProblem(self, sums, n):
        print(f'sums={sums}    n= {n}')
        # subset = []
        # res = []
        # sums.remove(0)
        # print(f'now sums is {sums}')
        # subset.append(self.minBesideZero(sums))
        # self.backtrack(sums,n,res,0,subset)
        sums.sort()
        # return self.dfs(sums,n)
        return self.dfs2(n,sums)

    def backtrack(self,nums,n,res,i,subset):



        if (len(subset) == n) and (sum(subset) in nums):
            res.append(subset.copy())
            return

        if i == len(subset):
            return

        subset.append(nums[i])
        if nums[i] != subset[0]  and sum(subset) in nums:
            self.backtrack(nums,n,res,i+1,subset)
        else:
            subset.pop()
            self.backtrack(nums,n,res,i+1,subset)

    def minBesideZero(self,nums):

        minN = nums[0]

        for i in range(len(nums)):

            if nums[i] == 0:
                continue

            if minN == 0 or minN > nums[i]:
                minN = nums[i]

        return minN

    def dfs(self,sums,n):

        if 0 not in sums:
            return []

        if n == 2:
            sums.remove(0)
            return [sums[0]]

        x = sums[-1] - sums[-2]

        # for positive x's
        newSum1 = []
        count1 = Counter(sums)
        for a in sums[::-1]:
            b = a - x
            if count1[a] and count1[b]:
                newSum1.append(b)
                count1[a] -= 1
                count1[b] -= 1
            else:
                break
        ans1 = []
        if len(newSum1) == n //2:
            ans1 = [x] + self.dfs(newSum1[::-1],n)

        #  for negative x's
        newSum2 = []
        count2 = Counter(sums)
        for a in sums[::-1]:
            b = a + x
            if count2[a] and count2[b]:
                newSum1.append(b)
                count2[a] -= 1
                count2[b] -= 1
            else:
                break
        ans1 = []
        if len(newSum2) == n // 2:
            ans1 = [-x] + self.dfs(newSum2, n)


        return newSum1 if len(newSum1) >= len(newSum2) else newSum2

    def dfs2(self,n,sums):
        if n == 1 and 0 in sums: return [max(sums, key=abs)]
        cands = []

        d = sums[1] - sums[0]

        for dr in [1, -1]:
            cnt, new = Counter(sums), []
            if cnt[0] == 0: return []
            for num in sums[::-dr]:
                if cnt[num] == 0: continue
                if cnt[num - d * dr] == 0: break
                cnt[num] -= 1
                new += [num]
                cnt[num - d * dr] -= 1

            if len(new) == 1 << (n - 1):
                cands += [[-d * dr] + self.dfs2(n - 1, new[::-dr])]

        return max(cands, key=len)