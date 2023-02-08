'''
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

'''
class MinimumRemoveParenthesis:

    def solveProblem(self, s: str) -> str:
        res = ''
        strStack = []
        invalidPositions = []
        for i in range(len(s)):
            if s[i] == '(':
                strStack.append(i)
            elif s[i] == ')' and len(strStack) > 0:
                strStack.pop()
            elif s[i] == ')':
                invalidPositions.append(i)

        invalidPositions.extend(strStack)

        for i in range(len(s)):
            if i in invalidPositions:
                continue
            res += s[i]

        return res