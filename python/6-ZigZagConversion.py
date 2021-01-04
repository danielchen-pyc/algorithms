'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
'''


def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    count = 2 * numRows - 2
    n = len(s)
    newstr = []
    for i in range(numRows):
        for j in range(i, n, count):
            newstr.append(s[j])
            if (i != 0 and j + count - 2 * i < n and i != numRows - 1):
                newstr.append(s[j + count - 2 * i])
    return "".join(newstr)
    
