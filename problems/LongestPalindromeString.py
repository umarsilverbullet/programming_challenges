'''
Given a string s, return the longest
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

'''
class LongestPalindromeString:

    def solveProblem(self, s: str) -> str:

        resLen = 0
        res=''

        for i in range( len(s)):
            #odd length palindrome
            l,r = i,i
            while l>=0 and r < len(s) and s[l] == s[r]:

                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = (r-l+1)

                l,r = l-1,r+1
            # even length palindrome
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:

                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = (r - l + 1)

                l, r = l - 1, r + 1

        return res