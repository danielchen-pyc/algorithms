'''
Given the array candies and the integer extraCandies, where candies[i] represents
the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids
such that he or she can have the greatest number of candies among them. Notice
that multiple kids can have the greatest number of candies.
'''


# My Solution (77.41%)
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    return map(lambda x: (x + extraCandies) >= max(candies), candies)


# My Solution (92.70%)
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    maxCandies = max(candies)
    return [x + extraCandies >= maxCandies for x in candies]
