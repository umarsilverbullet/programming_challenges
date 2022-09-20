# combination sum
class Triangle:
    def __init__(self):
        print('initialised')
    def solveProblem(self, triangle: list):
        dp = [0] * (len(triangle)+1)

        for row in triangle[::-1]:
            for i in range( len(row)):
                dp[i] = row[i] + min( dp[i],dp[i+1])

        return dp[0]

    def solveProblem2(self, triangle:list):
        print(triangle)

        p = 0
        for i in range( len(triangle)):

            if i ==0:
                sum = triangle[i][p]
                continue

            sum = sum + min(triangle[i][p],triangle[i][p+1])
            p = p+1 if triangle[i][p] > triangle[i][p+1] else p

        #
        return sum

