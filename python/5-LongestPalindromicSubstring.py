'''
Given a string s, return the longest palindromic substring in s.
'''


def longestPalindrome(self, s: str) -> str:
    m = ''  # Memory to remember a palindrome
    for i in range(len(s)):  # i = start, O = n
        for j in range(len(s), i, -1):  # j = end, O = n^2
            substring = s[i:j]
            if len(m) >= j-i:  # To reduce time
                break
            elif substring == substring[::-1]:
                m = substring
                break
    return m
