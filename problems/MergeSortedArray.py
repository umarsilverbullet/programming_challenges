"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
 and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
 but instead be stored inside the array nums1.
 To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
 and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
class MergeSortedArray:
    def __init__(self):
        print('initialising')

    def solveProblem(self, nums1, m: int, nums2, n: int):
        print(f'nums1 = {nums1} m={m} \n nums2 = {nums2} n={n}')

        p1,p2 =m-1,n-1
        for i in range(m + n -1,-1,-1):

            if p1 < 0:
                nums1[i] = nums2[p2]
                p2-=1
                continue

            elif p2 < 0:
                p1 -= 1
                continue

            if nums1[p1] <= nums2[p2]:
                nums1[i] = nums2[p2]
                p2-=1
            else:
                nums1[i] = nums1[p1]
                p1-=1

