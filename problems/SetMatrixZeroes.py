# combination sum
class SetMatrixZeroes:
    def __init__(self):
        print('initialised')

    def solveProblem(self,matrix):
        print(matrix)
        setZero = False
        ROWS,COLS = len(matrix),len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):

                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0 :
                        matrix[r][0] = 0
                    else:
                        setZero = True

        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for c in range(COLS):
                matrix[0][c] = 0
        if setZero:
            for r in range(ROWS):
                matrix[r][0] = 0


