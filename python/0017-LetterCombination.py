'''
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
'''

# My Solution: Runtime 82.43%
def letterCombinations(self, digits: str) -> List[str]:
    d = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    if len(digits) == 0:
        return []
    elif len(digits) == 1:
        return d[digits]
    else:
        answer = []
        rest = self.letterCombinations(digits[:-1])
        return [s+c for c in d[digits[-1]] for s in rest]
