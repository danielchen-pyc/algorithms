'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''


# My Solution (Runtime 43.08%)
def strStr(self, haystack: str, needle: str) -> int:
    if haystack == needle or needle == "":
        return 0
    elif haystack == "" or len(needle) > len(haystack):
        return -1
    for i, c in enumerate(haystack):
        if c == needle[0]:
            j = 0
            while j < len(needle):
                if i+j >= len(haystack) or haystack[i+j] != needle[j]:
                    break
                j += 1
            if j == len(needle):
                return i
            if i+len(needle) >= len(haystack):
                return -1
    return -1



# Other Solution (Runtime 71.19% Memory 88.73%)
def strStr(self, haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    elif needle not in haystack:
        return -1
    else:
        return len(haystack.split(needle)[0])
