'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

'''
import json
class FindStringInString:
    def testingJsonLoad(self):
        '''
                testing the json.load
                '''
        with open('dirJson/products.json', encoding='utf8') as file:
            jsonLoad = json.load(file)

    def solveProblemIncorrect1(self, haystack: str, needle: str) -> int:

        s1,s2=0,0
        while s1 < len(haystack) and s2 < len(needle):
            if haystack[s1] == needle[s2]:
                s2+=1
            else:
                s2 = 0
            s1+=1

        if s2 == len(needle):
            return s1 - s2

        return -1

    def solveProblem(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range( len(haystack) + 1 - len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

    def solveProblemBruteForce(self, haystack: str, needle: str) -> int:

        c = 0
        while c < len(haystack):
            s1 = c
            s2 = 0
            while s1 < len(haystack) and s2 < len(needle):
                if haystack[s1] == needle[s2]:
                    s2 += 1
                else:
                    c += 1
                    break
                s1 += 1
            if s2 == len(needle):
                return c

        return -1