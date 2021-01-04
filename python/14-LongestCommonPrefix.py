'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

# My Solution (Runtime: 77.11%, Memory: 91.61%)
def longestCommonPrefix(self, strs: List[str]) -> str:
    current = ""
    if len(strs) == 0 or len(strs[0]) == 0:
        return current
    for i in range(1, len(strs[0])+1):
        new_strs = list(map(lambda word: word[:i], strs))
        if len(list(dict.fromkeys(new_strs))) == 1:
            current = new_strs[0]
        else:
            return current
    return current
