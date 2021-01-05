'''
Given the array nums consisting of 2n elements in the form
[x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
'''

# My solution (Runtime: 95.99%)
def shuffle(self, nums: List[int], n: int) -> List[int]:
    first = nums[:int(len(nums)/2)]
    second = nums[int(len(nums)/2):]
    answer = []
    for i in range(len(first)):
        answer.append(first[i])
        answer.append(second[i])
    return answer



# Runtime 95.99%
def shuffle(self, nums: List[int], n: int) -> List[int]:
    res = []
    for i, j in zip(nums[:n],nums[n:]):
        res += [i,j]
    return res
