"""
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
"""

from collections import Counter

def topKFrequent(nums: list[int], k: int) -> list[int]:
    counter = Counter(nums)
    sorted_counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    items = list(sorted_counter.keys())
    return items[:k]

nums = [3,0,1,0]
k = 1
print(topKFrequent(nums, k))