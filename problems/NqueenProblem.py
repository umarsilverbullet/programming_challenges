# combination sum
class NqueenProblem:
    def __init__(self,n):
        self.n = n
        self.board = []
        self.rowSet = set()
        self.colSet = set()
        self.diagnolNegativeSet = set()
        self.diagnolPositiveSet = set()
        print('initialise')

    def solveProblem(self):
        board = [['.' for i in range(self.n)] for j in range(self.n)]
        result = []
        rowSet, colSet, diagnolNegativeSet, diagnolPositiveSet = set(),set(),set(),set()
        self.solve(board,self.n,rowSet,colSet,diagnolNegativeSet,diagnolPositiveSet,0,result)
        print(result)
    def solve(self,board,n,rowSet,colSet,diagnolNegativeSet,diagnolPositiveSet,row,result):
        print(f'row => {row}')
        print(f'board => {board}')
        print(f'diagnolPositive = {diagnolPositiveSet}')
        print(f'diagnolNegativeSet = {diagnolNegativeSet}')

        if row == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return

        for col in range(n):
            if col in colSet  or (row + col) in diagnolPositiveSet or (row - col) in diagnolNegativeSet:
                continue

            board[row][col] = 'Q'
            colSet.add(col)
            rowSet.add(row)
            diagnolPositiveSet.add(row + col)
            diagnolNegativeSet.add(row - col)

            print(f'diagnolPositive w= {diagnolPositiveSet}')
            print(f'diagnolNegativeSet w= {diagnolNegativeSet}')
            self.solve(board,self.n,rowSet,colSet,diagnolNegativeSet,diagnolPositiveSet,row + 1,result)

            board[row][col] = '.'
            colSet.remove(col)
            rowSet.remove(row)
            diagnolPositiveSet.remove(row + col)
            diagnolNegativeSet.remove(row - col)


