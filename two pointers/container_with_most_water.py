"""
The problem:
    check on leetcode.

The solution:
    The area calculation is calculated as such: (bar2 position - bar1 position) * min(height of the two bars).
    It's basically area of a rectangle in a euclidian plane.

    Set two pointers at the beginning and the end.
    Calculate area from the formula.
    take the max of the current area and the current maximum area, so that you always have the maximum.
    always update the minimum bar pointer.

Things to remember:
    two pointers, l, r -> beginning, end
    currArea = (r-l) * min(h[l], h[r])
    area = max(currMaxArea, currArea)
    l += 1 if h[l] < h[r] else r-=1
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = -1

        l, r = 0, len(height) - 1

        while l < r:
            area = max(area, ((r-l) * min(height[l], height[r])))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area

obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
res = obj.maxArea(height)
print(res)

# Man. I solved it in 10 minutes. Im happy.