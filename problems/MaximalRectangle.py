# combination sum
from LargestRectangleInHist import LargestRectangleInHist
class MaximalRectangle:
    def __init__(self):
        print('initialised')

    def solveProblem(self,matrix):

        curRow = [0]* len(matrix[0])
        maxArea = 0

        for i in range( len(matrix)):
            for j in range( len(matrix[0])):

                if matrix[i][j] == "1":
                    curRow[j] += 1
                else:
                    curRow[j] = 0

            curMax = LargestRectangleInHist().solveProblem(curRow)
            maxArea = max(maxArea,curMax)

        return maxArea

