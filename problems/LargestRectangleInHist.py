# combination sum
class LargestRectangleInHist:
    def __init__(self):
        print('initialised')

    def solveProblem(self,nums):
        ps = self.prevSmaller(nums)
        ns = self.nextSmaller(nums)
        maxArea = 0
        for i in range(len(nums)):
            area = (ns[i]-ps[i]-1) * nums[i]
            maxArea = max(maxArea,area)

        return maxArea

    def nextSmaller(self, a):
        stack = []
        ns = [-1] * len(a)
        for i in range(len(a)-1,-1,-1):
            while len(stack) > 0 and a[stack[len(stack) - 1]] >= a[i]:
                stack.pop()

            if (len(stack) <= 0):
                ns[i]= len(a)
            else:
                ns[i]= stack[len(stack) - 1]

            stack.append(i)

        return ns
    def prevSmaller(self, a):
        stack = []
        ps = []
        for i in range(len(a)):
            while len(stack) > 0 and a[ stack[len(stack)-1]] >= a[i]:
                stack.pop()

            if(len(stack) <= 0):
                ps.insert(i,-1)
            else:
                ps.insert(i,stack[len(stack)-1])

            stack.append(i)

        return ps
