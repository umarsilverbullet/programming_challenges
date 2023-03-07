'''
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


'''
class IntegerToEnglishWords:
    englishNumbers = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand',
        1000000: 'million',
        1000000000: 'billion'
    }
    def __init__(self):
        pass

    def solveProblem(self, num: int)-> str:
        if num == 0:
            return 'Zero'
        englishWord = ''
        englishWord = self.convertToEnglish(num)
        return englishWord.title()


    def convertToEnglish(self, num):

        if num == 0:
            return ''

        placeNum = num
        placeValue = 1

        for n in [10, 100, 1000, 1000000, 1000000000]:
            placeValueCheckNumber = num
            if placeValueCheckNumber // n == 0:
                break
            placeValue = n

        if placeValue == 1:
            englishWord = self.englishNumbers[num]

        elif placeValue == 10:
            placeValueNumber = num // placeValue
            restValueNumber = num % placeValue
            englishWord = self.englishNumbers[num] if (num in self.englishNumbers) else (
                        self.englishNumbers[placeValueNumber * placeValue] + ' ' + self.convertToEnglish(
                    restValueNumber))
        else:
            placeValueNumber = num // placeValue
            restValueNumber = num % placeValue
            englishWord = self.convertToEnglish(placeValueNumber) + ' '+ self.englishNumbers[placeValue]
            englishWord+= '' if restValueNumber==0 else ' ' + self.convertToEnglish(restValueNumber)

        return englishWord