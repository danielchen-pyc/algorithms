'''
Convert integers to Roman
'''

# My Solution (18.07%)
def intToRoman(self, num: int) -> str:
    tens_roman = ['I', 'X', 'C', 'M']
    fives_roman = [' ', 'V', 'L', 'D']
    answer = ''
    while num != 0:
        num_digits = len(str(num))
        digit = num // 10**(num_digits - 1) if num_digits > 1 else num
        if digit < 4:
            toAdd = tens_roman[num_digits-1] * digit
        elif digit == 4:
            toAdd = tens_roman[num_digits-1] + fives_roman[num_digits]
        elif digit < 9:
            toAdd = fives_roman[num_digits] + tens_roman[num_digits-1] * (digit - 5)
        else:
            toAdd = tens_roman[num_digits-1] + tens_roman[num_digits]
        num %= 10**(num_digits - 1) if num_digits > 1 else num
        answer += toAdd
    return answer


# Other ppl's Solution
def intToRoman(self, num: int) -> str:
    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    res = ""

    for i in d:
        res += (num//i) * d[i]
        num %= i

    return res
