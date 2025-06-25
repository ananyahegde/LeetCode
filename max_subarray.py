"""
Maximum Subarray - continuous array. There are n^2(?) of these. Starting at 0th index, all the way upto the end,
starting at 1th all the way upto the end, .. and so on.

Since we are trying to find the maximum, if the start index is -ve, you can skip it.
for example, for an array like this - [-2, 1, -3, 4, -1, 2, 1, -5, 4]

when our `i` pointer is at -2 it is not gonna contribute to the max of anything so you can ignore it.
Remember, you can ignore them only if -ves are in the beginning, or `prefix` (or at the end).

And, there is another similar trick here. you've ignored -2, right, and you move on.
The curr_sum is 1 now.
For the next iteration, curr_sum is 1-3 = -2.
So the `4` is prefixed by curr_sum = -2 which negative.
So the 1 and -3 doesn't matter at all.


- Everytime we get a negetive prefix, we remove it (all the previous ones from the subarray).
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0] # don't do zero, remember the array has negative values
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(curSum, maxSub)

        return maxSub