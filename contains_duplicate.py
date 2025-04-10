# The below two are my dirty solutions

# This is not good for large n
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = False
        i = 0
        while(i < len(nums)):
            j = i + 1
            while(j < len(nums)):
                if nums[i] == nums[j]:
                    result = True
                j+=1
            i+=1
        return result

# Orrrr this!. works all the time. got 4ms on leetcode. hehehehehehhe. hehe :)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if (len(nums) == len(nums_set)):
            return False
        else:
            return True
