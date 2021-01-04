'''
Given a string s, find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(self, s: str) -> int:
    dict = {}
    max_length = start = 0
    for i, char in enumerate(s):
        if char in dict:
            sum = dict[char] + 1
            if sum > start:
                start = sum
        num = i - start + 1
        if num > max_length:
            max_length = num
        dict[char] = i
    return max_length
