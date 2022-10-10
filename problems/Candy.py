# combination sum
class Candy:
    def __init__(self):
        print('initialising')
    #  1,2,3,4,3,2,1
    #  1,2,3,4,1,2,1
    def solveProblem(self, ratings: list) -> int:

        minCandy = 0

        candy = [1 for i in range(len(ratings))]

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i],candy[i+1]+1)


        return sum(candy)