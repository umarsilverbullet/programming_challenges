'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
'''

class longestCommonPrefix:
    def solveProblem(self, strs: list) -> str:
        print(strs)
        result = ''
        for i in range( len(strs[0])):
            for s in strs:
                if i >= len(s) or strs[0][i] != s[i]:
                    return result
            result = result + s[i]



