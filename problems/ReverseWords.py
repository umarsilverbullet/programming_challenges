'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words.
Do not include any extra spaces.

Example:-
Input: s = "the sky is blue"
Output: "blue is sky the"

'''
class ReverseWords:

    def solveProblem(self, st: str) -> str:
        r = ''
        rStr = ''

        i=0
        while i < len( st):

            while i < len(st) and st[i] == ' ':
                i+=1
                continue

            while i < len(st) and st[i] != ' ':
                r += st[i]
                i+=1

            if rStr == '':
                rStr = r
            elif r != '':
                rStr = r + ' ' + rStr

            r = ''

        if r != '':
            rStr = r + ' ' + rStr
        return rStr

