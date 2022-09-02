# combination sum
class MergeIntervals:
    def __init__(self):
        print('initialise')

    def solveProblem(self,intervals):
        print(intervals)
#         sort the intervals based on first index
        intervals.sort(key= lambda i: i[0])
        print(intervals)
        mergedInterval = []
        mergedInterval.append(intervals[0])
        j = 0
        for i in range(len(intervals)):
            if intervals[i][0] <= mergedInterval[j][1]:
                mergedInterval[j][1] = max(mergedInterval[j][1],intervals[i][1])
            else:
                mergedInterval.append(intervals[i])
                j += 1

        return (mergedInterval)

