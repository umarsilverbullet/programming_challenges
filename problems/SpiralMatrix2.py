# combination sum
class SpiralMatrix2:
    def __init__(self):
        print('initialising')

    def solveProblem(self,n):
        print(n)
        res = [[0]*n for i in range(n)]

        print(res)
        left,right = 0,len(res[0])
        top,bottom = 0,len(res)

        curNumber = 1
        while left < right and top < bottom:

            # left to right
            for i in range(left,right):
                res[left][i] = curNumber
                curNumber += 1
            top += 1

            # top to bottom
            for i in range(top,bottom):
                res[i][right-1] = curNumber
                curNumber += 1
            right -= 1

            if not(left < right and top < bottom):
                break
            # right to left
            for i in range(right-1,left-1, -1):
                res[bottom-1][i] = curNumber
                curNumber += 1
            bottom -=1

            # bottom to top
            for i in  range(bottom -1, top-1, -1):
                res[i][left] = curNumber
                curNumber += 1
            left += 1

        print(res)