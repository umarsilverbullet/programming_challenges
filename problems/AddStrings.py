'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
'''

class AddStrings:
    def __init__(self):
        print('initialised')

    def solveProblem(self, num1: str, num2: str) -> str:
        result = ''
        carry = 0

        lenNum1, lenNum2 = len(num1), len(num2)
        p1,p2 = lenNum1-1,lenNum2-1

        while p1 >= 0 or p2 >= 0:
            o1,o2 = 0,0

            if p1 >= 0:
                o1 = ord(num1[p1])-48
                p1 -= 1

            if p2 >= 0:
                o2 = ord(num2[p2])-48
                p2 -= 1


            tmp = o1 + o2 + carry

            if tmp > 9:
                carry = 1
            else:
                carry = 0

            result = str(tmp)[-1] + result

        if carry:
            result = str(carry) + result

        return result




