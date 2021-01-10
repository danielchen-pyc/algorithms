'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''


# My Solution (Runtime: 59.89%)
def isValid(self, s: str) -> bool:
    stack = []
    d = {']': '[', '}': '{', ')': '('}
    for char in s:
        if char in d.values():
            stack.append(char)
        elif char in d.keys():
            if stack == [] or d[char] != stack.pop():
                return False
    return len(stack) == 0



# Runtime 99.11%
def isValid(self, s: str) -> bool:
    stack = []
    d = {'(':')', '{':'}','[':']'}
    for i in s:
        if i in d:  # 1
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:  # 2
            return False
    return len(stack) == 0
