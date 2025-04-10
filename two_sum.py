# Definately a solution. Mine
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
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