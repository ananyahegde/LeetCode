
"""
https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution.
You have to return indices, in any order.
"""

# Solution using arrays
def twoSum(nums: list[int], target: int) -> list[int]:
    indeces = []

    i = 0
    while(i < len(nums)):
        j = i + 1
        while(j < len(nums)):
            print(f"iteration: {i, j}  ----->  num1 = {nums[i]}, num2 = {nums[j]}, sum = {nums[i]+nums[j]}, target = {target}")
            if(nums[i] + nums[j] == target):
                indeces.append(i)
                indeces.append(j)
                return indeces
            j+=1
        i+=1
    return []



nums = [1, 3, 11, 15, 7, 3, 5, 2, 7]
target = 9

twoSum(nums, target)
