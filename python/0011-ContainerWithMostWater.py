'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the
line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis
forms a container, such that the container contains the most water.
'''


def maxArea(self, height: List[int]) -> int:
    maxVol = 0
    i = 0
    j = len(height) - 1
    for _ in range(len(height)):
        width = abs(j - i)
        if height[i] < height[j]:
            volumn = width * height[i]
            i += 1
        else:
            volumn = width * height[j]
            j -= 1

        if volumn > maxVol:
            maxVol = volumn
    return maxVol
