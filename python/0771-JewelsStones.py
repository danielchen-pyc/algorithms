'''
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type
of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
'''


# My Solution: Runtime 57.11%
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    return sum([stones.count(char) for char in set(jewels)])


# Runtime 95%
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    setJ = set(jewels)
    return sum(s in setJ for s in stones) # Sum the true/false values
