# combination sum
from collections import defaultdict
class MaxPointsOfLine:
    def __init__(self):
        print('initialising')
    #  1,2,3,4,3,2,1
    #  1,2,3,4,1,2,1
    def findLine(self,x0, y0, x1, y1):
        if x0 == x1:
            return x0, None
        if y0 == y1:
            return 0, y0

        slope = (y1 - y0) / (x1 - x0)
        intercept = y0 - slope * x0
        return slope, intercept

    def solveProblem(self, points: list) -> int:

        if len(points) == 1:
            return 1

        lines = defaultdict(lambda: set())

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x0, y0 = points[i]
                x1, y1 = points[j]
                line = self.findLine(x0, y0, x1, y1)
                lines[line].add(i)
                lines[line].add(j)

        return max([len(lines[line]) for line in lines])