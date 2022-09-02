# combination sum
class InsertInterval:
    def __init__(self):
        print('initialise')

    def solveProblem(self,intervals,newInterval):
        # return self.solveProblemWithSort(intervals,newInterval)
        return self.solveProblemWithoutSort(intervals,newInterval)

    def solveProblemWithSort(self,intervals,newInterval):

        print(f'intervals = {intervals} newinteval = {newInterval}')
        res = []
        for interval in intervals:
            if newInterval[0] >= interval[0] and newInterval[0] <= interval[1]:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
            elif newInterval[0] < interval[0] and newInterval[1] >= interval[0]:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
            else:
                res.append(interval)

        res.append(newInterval)
        res.sort(key= lambda i: i[0])
        return res

    def solveProblemWithoutSort(self, intervals, newInterval):

        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res