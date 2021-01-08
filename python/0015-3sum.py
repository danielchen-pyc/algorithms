'''
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
'''


# My Solution (Time-limit exceeded :( )
def threeSum(self, nums: List[int]) -> List[List[int]]:
    pos = sorted(filter(lambda x: x > 0, nums))
    neg = sorted(filter(lambda x: x < 0, nums))
    answer = []
    zeros = list(filter(lambda x: x == 0, nums))
    if len(zeros) >= 3:
        answer.append([0, 0, 0])

    if len(zeros) != 0:
        for num1 in pos:
            if -num1 in neg and [-num1, 0, num1] not in answer:
                answer.append([-num1, 0, num1])

    for num1 in pos:
        for num2 in neg:
            num3 = -num1-num2
            toAppend = sorted([num1, num2, num3])
            if (((num3 in pos and not (num3 == num1 and pos.count(num3) < 2))
                or (num3 in neg and not (num3 == num2 and neg.count(num3) < 2)))
                and toAppend not in answer):
                answer.append(toAppend)

    return answer



# Runtime: 85.57%
def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        if i >= 1 and v == nums[i-1]:
            continue
        d = {}
        for x in nums[i+1:]:
            if x not in d:
                d[-v-x] = 1
            else:
                res.add((v, -v-x, x))
    return map(list, res)



# Runtime: 68.12%, Memory: 97.55%
def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res



# Practice: 4sum
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    if len(nums) < 4:
        return []
    res = set()
    nums.sort()
    print(nums)
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i+1:]):
            if i >= 1 and (num1 == nums[i-1]):
                continue
            d = {}
            for num3 in nums[i+2:]:
                if num2 == num3 and nums[j+i+1] != nums[j+i]:
                    continue
                if num3 not in d:
                    d[-num1-num2-num3] = 1
                else:
                    res.add(tuple(sorted((num1, num2, num3, -num1-num2-num3))))
    return list(res)
