'''
Given an array nums of n integers and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.
'''


#Solution: Runtime 66.51%
def threeSumClosest(self, nums: List[int], target: int) -> int:
    diff = float('inf')
    nums.sort()
    for i, num in enumerate(nums):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            total = num + nums[lo] + nums[hi]
            if abs(total - target) < abs(diff):
                diff = target - total
            if total < target:
                lo += 1
            else:
                hi -= 1
        if diff == 0:
            break

    return target - diff
