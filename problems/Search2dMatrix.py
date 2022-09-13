# combination sum
class Search2dMatrix:
    def __init__(self):
        print('initialised')

    def solveProblem(self,matrix, target):
        ROWS, COLS = len(matrix),len(matrix[0])
        top, bot = 0, ROWS-1
        searchRow = -1
        while top <= bot:
            midRow = (bot + top) // 2
            if target > matrix[midRow][COLS-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow -1
            else:
                searchRow = midRow
                break

        if searchRow == -1:
            return False


        l,r = 0,COLS-1
        while l <= r:
            mid = (l + r) // 2

            if matrix[searchRow][mid] == target:
                return True
            elif matrix[searchRow][mid] > target:
                r = mid -1
            else:
                l = mid + 1

        return False

