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

        i=0
        n1,n2 = num1,num2
        while n1 and n2:
            p1 = int(num1[-(i+1)])
            p2 = int(num2[-(i+1)])
            res = p1 + p2 + carry

            if res > 10:
                carry = 1
            else:
                carry = 0

            result = str(res) + result
            n2 = num2[0:-(i+1)]
            n1 = num1[0:-(i+1)]
            i+=1

        if num1:

        return result

