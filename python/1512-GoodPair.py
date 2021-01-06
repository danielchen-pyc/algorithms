'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
'''


# My Solution (Runtime: 90.51%)
def numIdenticalPairs(self, nums: List[int]) -> int:
    count = 0
    prev = 0
    rep = {}
    # nums.sort()
    for num in nums:
        if num in rep:
            count += rep[num]
            rep[num] += 1
        else:
            rep[num] = 1
    return count
