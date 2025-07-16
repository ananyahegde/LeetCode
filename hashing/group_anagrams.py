"""
https://leetcode.com/problems/group-anagrams/description/

The problem:
    Given an array of strings strs, group the anagrams together. So the return type is list of lists.

    Example:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

The solution:
    use hashmap.
    your key in this map is a tuple of 26 elements - the characters.
    Anagrams will have the same characters in them, so the `key` is same for anagrams.
    store these anagrams in values, as a list.
    get the values of this map and return it as list of lists.

Key things:
    Use map.
    key: a boolean tuple, 1 means character present.
    value: words, in a list
    return [map.values()]
"""

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    hashes = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        hashes[tuple(count)].append(word)

    return list(hashes.values())

strs = ["eat","tea", "tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))