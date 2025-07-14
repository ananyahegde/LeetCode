"""
The problem:
    Given a string s and integer k.
    You can choose any character and replace it with any other character.
    You can do this k times.

    Return the longest substring containing same letter after performing the above operation.
    For example,
        s = 'ABAB', k = 2.
        You can return either A or B with B or A. resulting string would be AAAA or BBBB.
        So the longest substring with same letter would be 4.

Approach:
    We can solve it in O(26*n) time complexity.
    And O(m) space complexity (m - unique characters).

    Consider, s = ABABBA and k = 2.

    First thing to think of: which character should we replace, so that we maximize our `res`?

    This is a sliding window problem, and each window, you look at the most frequent character.

    For instance, A[BABB]A for this window, if you look at it, B occurs 3 times while A occurs once.
    So we replace A with B.
    To do this we use a hashmap, similar to counter, you count the characters with frequencies in a current
    window.

    But how do we know how many characters we've got to replace?
    windowLength - count[frequentChar] gives you that number.
    And you can only replace if it doesnt exceed k.

    How to do check the most frequent character in the current window?
    Using hashmap. It can contain atmost 26 characters, so O(26).

    The main condition we are checking is:
        windowLength - count[frequentChar] <= k
        if true, then increment r (right pointer).
        if not, increment l pointer until its valid once again.
        And at every valid window, you'd update res to be the windowLength.

Key things:
    Use `hashmap` to lookup most frequent character for the current window.
    check the condition.
    If true -> shift r to the right.
    If false -> shift l to the right.
    update `hashmap`
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        res = 0
        l = 0
        r = 0

        while r < len(s):
            map[s[r]] = 1 + map.get(s[r], 0) # you get key error if you do += 1
            if (r-l+1) - max(map.values()) > k:
                map[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
            r += 1
        return res

obj = Solution()
res = obj.characterReplacement('ABABBA',  2) # ans = 5
print(res)