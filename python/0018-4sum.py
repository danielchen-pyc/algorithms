'''
Given an array nums of n integers and an integer target, are there elements a,
b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets
in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.
'''


# My Solution (Runtime 79.78%)
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    def findNsum(l, r, target, N, currSum, results):
        if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:
            return
        if N == 2:
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(currSum + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(l, r+1):
                if i == l or (i > l and nums[i] != nums[i-1]):
                    findNsum(i+1, r, target-nums[i], N-1, currSum + [nums[i]], results)

    nums.sort()
    results = []
    findNsum(0, len(nums)-1, target, 4, [], results)
    return results
