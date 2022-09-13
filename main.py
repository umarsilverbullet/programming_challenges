# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting

# from problems.NqueenProblem import NqueenProblem
# from problems.MaxSubArray import MaxSubArray
# from problems.SpiralMatrix import SpiralMatrix
# from problems.MergeIntervals import MergeIntervals
# from problems.SpiralMatrix2 import SpiralMatrix2
# from problems.InsertInterval import InsertInterval
# from problems.TextJustification import TextJustification
# from problems.SetMatrixZeroes import SetMatrixZeroes
# from problems.Search2dMatrix import Search2dMatrix
# from problems.SortColors import SortColors
from problems.Subsets import Subsets

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def trappingRain1():
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    heights = [4, 2, 0, 3, 2, 5]
    sum = 0
    left, right = (0, 0)

    for i in range(len(heights)):
        left = heights[i]
        right = heights[i]
        print('=================')
        print('search left')
        for j in range(i, -1, -1):
            print(f'heights[{j}] ==> {heights[j]}')
            left = max(left, heights[j])
        print('=================')
        print('search right')
        for j in range(i, len(heights)):
            print(f'heights[{j}] ==> {heights[j]}')
            right = max(right, heights[j])

        print(f'left when i={i} == {left}')
        print(f'right when i={i} == {right}')

        sum = sum + (min(left, right) - heights[i])
        print(f'sum when i={i} == {sum}')
        print(f'=============================================')
        print(f'=============================================')
    print(sum)
def trappingRain2():
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    heights = [4, 2, 0, 3, 2, 5]
    sum = 0
    left, right = (0, 0)
    leftMax = [ 0 for i in range(len(heights))]
    rightMax = [ 0 for i in range(len(heights))]

    n = len(heights)
    for i in range(len(heights)):

        if i == 0:
            leftMax[i] = heights[i]
            rightMax[n-1] = heights[n-1]
        else:
            leftMax[i] = max(leftMax[i-1], heights[i])
            rightMax[n-i-1] = max(rightMax[n-i], heights[n-i-1])

    for i in range(len(heights)):
        sum = sum + (min(leftMax[i],rightMax[i]) - heights[i])

    print(sum)
def permute(nums):

    print('nums = ' + str(nums))
    result= set();
    if len(nums) == 1:
        return [nums.copy()]

    for i in range(len(nums)):
        num = nums.pop(0)
        print(f'popped {num}')
        permutation = permute(nums)
        print(f'permuation returned {permutation}')
        for perm in permutation:
            print(f'append {num} to {perm}')
            perm.append(num)
        result.extend(permutation)
        nums.append(num)

    return result
def permute2(nums,count,perms,result):

    if len(nums) == len(perms):
        result.append(perms.copy())
        return
    for n in count:
        if count[n] > 0:
            perms.append(n)
            count[n] -= 1

            permute2(nums,count,perms,result)

            count[n] += 1
            perms.pop()

    return result

def rotate(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r-l):
            t, b = l, r

            temp = matrix[t][l + i]
            matrix[t][l + i] = matrix[b - i][l]
            matrix[b - i][l] = matrix[b][r - i]
            matrix[b][r - i] = matrix[t + i][r]
            matrix[t + i][r] = temp
        l += 1
        r -= 1

def anagram(words):
    print(words)
    count = {}
    for word in words:
        print(sorted(word))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # trappingRain2()
    # print(permute([1,2,3]))

# permutation 2
    # nums = [1,1,2]
    # count = {n: 0 for n in nums}
    # for n in nums:
    #     count[n] += 1
    # perms = []
    # result = []
    # print(permute2(nums,count,perms,result))
    # print(result)
# permutation 2 ends here
# rotate matrix
#     matrix = [[1,2,3],[4,5,6],[7,8,9]]
#     rotate(matrix)
#     print(matrix)
# rotate matrix  ends here

#  anagram solution starts here
#     words = ["eat","tea","tan","ate","nat","bat"]
#     anagram(words)
#  anagram ends here

# n queen problem
# n=4
# nQueen = NqueenProblem(n)
# nQueen.solveProblem()
#  end here

# max sub array
# arr=[-2,1,-3,4,-1,2,1,-5,4]
# maxsubArray = MaxSubArray(arr)
# print(maxsubArray.solveProblem(arr))

# arr = [[1,2,3],[4,5,6],[7,8,9]]
# arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# arr = [[1,3],[8,10],[15,18],[2,6],[4,6]]
# arr = [[1,4],[2,3]]
# mI = MergeIntervals()
# print(mI.solveProblem(arr))

# inI = InsertInterval()
# intervals = [[1,3],[6,9]]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
# # newInterval = [2,5]
# print(inI.solveProblem(intervals,newInterval))

# spiral matrix 2
# spM2 = SpiralMatrix2()
# spM2.solveProblem(3)

# Unique path 2
# up2 = TextJustification()
#
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
#
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
#
# words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
#
# words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
# maxWidth = 16
#
#
# res = up2.solveProblem(words, maxWidth)
# print(up2.solveProblem(words, maxWidth))

# set matrix zeroes
# smz = SetMatrixZeroes()
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# smz.solveProblem(matrix)
# print(matrix)

# search in 2d matrix
# searchMatrix = Search2dMatrix()
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13
# matrix = [[1,3]]
# target = 3
# print(f'Search => { searchMatrix.solveProblem(matrix, target) }')

# sc = SortColors()
# nums = [2,0,1]
# nums = [1,2,0]
# sc.solveProblem(nums)
# print(nums)

# Subsets
nums = [1,2,3]
ss = Subsets()
print(ss.solveProblem(nums))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
