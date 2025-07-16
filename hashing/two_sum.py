
"""
https://leetcode.com/problems/two-sum/description/

The problem:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution.
    You have to return indices, in any order.

The solution:
    have one hashmap. store lis_ values:their indices
    iterate over the list and check if target - curr_value is in the map.
    If yes -> return [curr_value_idx, key(target - curr_value)]
    If not -> store the value:idx in the map.
"""

# Solution using arrays - brute force
"""def twoSum(nums: list[int], target: int) -> list[int]:
    indeces = []

    i = 0
    while(i < len(nums)):
        j = i + 1
        while(j < len(nums)):
            if(nums[i] + nums[j] == target):
                indeces.append(i)
                indeces.append(j)
                return indeces
            j+=1
        i+=1
    return []

nums = [1, 3, 11, 15, 7, 3, 5, 2, 7]
target = 9

twoSum(nums, target)"""

#
def twoSum(nums: list[int], target: int) -> list[int]:
    map = {}

    l = 0
    for i in range(len(nums)):
        if target - nums[i] in map.keys():
            return [i, map.get(target - nums[i])]
        else:
            map[nums[i]] = i
    return []

nums = [1, 3, 11, 15, 7, 3, 5, 2, 7]
target = 9

res = twoSum(nums, target)
print(res)