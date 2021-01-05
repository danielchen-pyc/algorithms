'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

# Runtime 62.58%
def runningSum(self, nums: List[int]) -> List[int]:
    current = 0
    answer = []
    for num in nums:
        current += num
        answer.append(current)
    return answer


def runningSum(self, nums: List[int]) -> List[int]:
    return accumulate(nums)
