'''
Given a sorted array nums, remove the duplicates in-place such that each element
appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the
input array in-place with O(1) extra memory.
'''



# My Solution (Runtime 40.27%)
def removeDuplicates(self, nums: List[int]) -> int:
    d = {}
    i = 0
    while i < len(nums):
        n = nums[i]
        if n not in d:
            d[n] = 1
        else:
            del nums[i]
            i -= 1
        i += 1




# Other Solution (Runtime 80.15%)
def removeDuplicates(self, nums: List[int]) -> int:
    nums[:] = list(Counter(nums).keys())


# Other Solution (Runtime 80.15%)
def removeDuplicates(self, nums: List[int]) -> int:
    if not A:
        return 0

    newTail = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[newTail]:
            newTail += 1
            nums[newTail] = nums[i]

    return newTail + 1
