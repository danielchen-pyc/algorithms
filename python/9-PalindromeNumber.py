'''
Determine whether an integer is a palindrome. An integer is a palindrome when it
reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?
'''


def isPalindrome(self, x: int) -> bool:
    arr = []
    nextNum = x
    if x < 0:
        return False
    left = nextNum % 10
    nextNum = nextNum // 10
    arr.append(left)
    while nextNum != 0:
        left = nextNum % 10
        nextNum = nextNum // 10
        arr.append(left)
    l = len(arr) - 1
    print(arr)
    result = 0
    for i in arr:
        result += i*(10**l)
        l -= 1
    print(result)
    return result == x
