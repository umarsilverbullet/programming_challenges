# combination sum
class MyPower:
    def __init__(self):
        print('initialising')
    #  1,2,3,4,3,2,1
    #  1,2,3,4,1,2,1
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if x == 0:
            return 0

        if n == 1:
            return x

        if n < 0:
            return self.myPow(1 / x, (n * -1))

        ans = self.myPow(x, n >> 1)

        return (x * ans * ans) if n % 2 == 1 else (ans * ans)


    def myPowBruteForce(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if n < 0:
            return 1/x * self.myPow(x,n+1)

        return x * self.myPow(x,n-1)