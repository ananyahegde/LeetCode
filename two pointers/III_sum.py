"""
    The problem:
        Please go read leetcode description.

    The solution:
        First thing you need to do is sort the array.
        Why?
        Because the biggest thing you need to take care of here, is avoiding duplicates.
        Otherwise, it is really is a simple problem.

        When you sort the elements, say [-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2], when you get to the first -1,
        okay, you check the other two such that -1 + _ + _ = 0.
        When you get to the next -1, you already have searched and found all the possible combinations
        of the triplets summing up to 0. so you could just eliminate that.

        So once you have that, all you need to do is find the correct two numbers in those positions: a+_+_ where
        those two equals to -a.
        That reduces to two sum problem.

        You can use hashmap to search for -a, just like you use it in your two sum problem.
        We dont need it though. Since we have already sorted the array, we can you two pointer method,
        just as we did in two sum II.

"""
"""
# works, but duplicates - O(n^2) and O(n)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        map = {}
        res = []

        for l in range(len(nums)):
            for r in range(1, len(nums)):
                currSum = nums[l] + nums[r]
                if -currSum in map.values():
                    
                        res.append([nums[l], nums[r], -currSum])
                else:
                     map[r] = nums[r]
        return res

obj = Solution()
res = obj.threeSum([-1,0,1,2,-1,-4]) # ans = 5
print(res)
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                    break
            if nums[i] == nums[i-1] and i!=0:
                i += 1
                continue

            j = i + 1
            k = len(nums) - 1

            while(j < k and j < len(nums)-1 and k > i+1):
                currSum = nums[j] + nums[k]
                if currSum == -nums[i]:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                if currSum > -nums[i]:
                    k -= 1
                if currSum < -nums[i]:
                    j += 1

        return res

obj = Solution()
res = obj.threeSum([-1,0,1,2,-1,-4])
print(res)

"""
    while nums[j] == nums[j-1] and j < k:
        j += 1
    
    This part right here is important. Say you have [-2, -2, 0, 0, 2, 2].
    You start with -2, and you get the first triplet as -2, 0, 2 - which is right. 
    When you decrement k and increment j, you get the same pair, but it is still valid. 
    But that is a duplicate. 
    So, to prevent that, you also have to check for duplicate numbers for either k or j.
    when you have -2 as a, and 0 as b, you know c has to be 2, you dont need to check for both, only one works fine. 
    
"""