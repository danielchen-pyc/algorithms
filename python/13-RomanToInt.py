'''
Convert Roman to integers
'''


# My Solution (80.67%)
def romanToInt(self, s: str) -> int:
    number = 0
    conversion = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    charList = [char for char in s]
    count = 0
    length = len(charList)
    while count < length:
        added = False
        thisNumber = conversion[charList[count]]
        if count + 1 < length:
            nextNumber = conversion[charList[count+1]]
            if nextNumber > thisNumber:
                number += (nextNumber - thisNumber)
                count += 2
                added = True
        if not added:
            number += thisNumber
            count += 1
    return number



def romanToInt(self, s: str) -> int:
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number
