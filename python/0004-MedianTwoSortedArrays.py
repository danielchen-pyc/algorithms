'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).
'''


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums1.extend(nums2)
    nums = sorted(nums1)
    print(nums)
    if len(nums) % 2 == 0:
        median = (nums[len(nums)//2-1] + nums[len(nums)//2]) / 2
    else:
        median = nums[len(nums)//2]
    return median
