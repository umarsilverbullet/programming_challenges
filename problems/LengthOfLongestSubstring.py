'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The a

'''
class LengthOfLongestSubstring:

    def solveProblem(self, s: str) -> int:

        l=0
        res=0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res,(r - l+1 ))

        return res