"""
Longest Substring without Repeating Characters:
    You're given a String. You have to find a length of the longest substring (substrings are consecutive (contiguous) characters in the string)
    without repeating any character.

    Brute force approach would be just looking at every single substring and see if it has any duplicate characters.
    (Go through this once if you need to: https://stackoverflow.com/questions/8269916/what-is-sliding-window-algorithm-examples)

    But with a sliding window technique, here's what you would do:
        You add characters until you find the duplicate.
        You discard all characters till the duplicate element (Not the second occurance of c, but the first)
        Record your highest length, and update it if the current length is greater.

        So for example: abcabcbb
        1: a
        2: ab
        3: abc
        4: abca -> duplicate, discard the first a
        5: bcab -> duplicate, discard the first b
        6: cabc -> duplicate, discard the first c
        7: abcb -> duplicate, discard a and b both, now it's only length 2
        8: cbb -> duplicate, discard c and b both, now it's only length 1

        If you visualize it, you can imagine it as container moving along the elements, hence `sliding window`.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet: # found duplicate, also why while? see below.
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r]) # not a duplicate
            res = max(res, len(charSet)) # len(charSet) or l-r+1
        return res

sol = Solution()
res = sol.lengthOfLongestSubstring('abcabcbb')
print(res)

"""
Why while? 
    You could be tempted to use if, but if only removes the s[l] once. But with while we are removing `till` the duplicate character (the first one). 
    You cant go and check entire string otherwise. and res always holds the max, so we still have the correct answer. 
"""