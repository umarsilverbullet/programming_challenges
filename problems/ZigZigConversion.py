# combination sum
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

'''
class ZigZagConversion:
    def __init__(self):
        pass

    def solveProblem(self,s: str,  numRows: int)-> str:

        response = '';
        if numRows == 1:
            return s

        for r in range(numRows):
            inc = (numRows -1) * 2
            for i in range(r,len(s), inc):
                response += s[i]
                if (r > 0 and r < (numRows-1) and (i+inc-2*r) < len(s) ):
                    response += s[(i+inc-2*r)]

        return response