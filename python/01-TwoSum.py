'''
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.
'''

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    visited = {}
    for i, n in enumerate(nums):
        remain = target - n
        if remain in visited:
            return [visited[remain], i]
        visited[n] = i
    return []
