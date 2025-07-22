"""
The problem:
    Check the description.

The solution:
    Brute Force:
        When koko eats a banana from a pile at minimum she can eat 1 (she can't eat 0, because she has to eat atleast 1).
        The maximum she can eat is the number of bananas in the largest pile - max(piles).
        calculate the total time it takes to finish the banana for every k in [1......max(piles)] and return whatever k that
        yeilds total time <= h.
        The complexity of this would be (max(p)*p).
        Because for every single integer from 1 to max(p) you are doing, you are iterating.
        And for every integer in this range, you are trying it as k, calculating the total time it takes. For that, you traverse the piles.

    The improved solution - Binary Search:
        You do the binary search for the array of integers - [1.....max(p)], to search for the target k.
        In the input given below, you have piles = [3, 6, 7, 11].

        So you binary search the array [1, 2, ..... 5, 6, ...., 11].
        So for some values in the beginning of the array you are going to get total_time > h.
        And after some point you get total_time <= h.

        If you get total_time > h, that means all the integers before that also yeild the same thing. So you ignore that portion - m = i + 1.

        If you get total_time <= h, that means all the integers after that also yeild the same thing. But the question asks for the minimum of k,
        which is i currently. Hence you don't search that right portion either. n = i - 1.
        For this one, you find another integer such that it is less than the current k AND it passes the condition total_time <= h,
        you need to update k there. k = min(k, i).

Things to remember:
    - Binary Search on [1.....max(piles)]
    - calculate total_time = ceil(p/i) where p in piles
    - if total_time > h then m = i + 1
    - if total_time <= h then n = i - 1 and k = min(k, i)

"""

import math

"""
# brute force
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        m, n = 1, max(piles)

        for i in range(m, n+1):
            total_time = 0
            for p in piles:
                total_time += math.ceil(p/i)
            if total_time <= h:
                k = i
                break
        return k
obj = Solution()
res = obj.minEatingSpeed([3,6,7,11], 8)
print(res)
"""

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        m, n = 1, max(piles)
        k = max(piles)

        while m <= n:
            i = (m+n)//2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p/i)
            print(f"i={i} total_time={total_time}")
            if total_time > h:
                m = i + 1
            if total_time <= h:
                n = i - 1
                k = min(k, i)
        return k
obj = Solution()
res = obj.minEatingSpeed([3,6,7,11], 8)
print(res)
