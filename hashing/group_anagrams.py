"""
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. So the return type is list of lists.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    hashes = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        hashes[tuple(count)].append(s)

    return list(hashes.values())

strs = ["eat","tea", "tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))