"""
The problem:
    Please read it on leetcode.
The Solution:
    Same as anagram. You've got a tuple with 26 characters, and number in each index indicates corresponding character's frequency.
    And for s2, you check the characters with same number characters in s1, like a fixed sliding window.
    If the tuple of char_frequency for that window matches with the char_frequency of s1, you've got a permutation -> return True.
    else, return False.
"""

"""
# Was trying it out myself. 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for c in s1:
            count[c] = count.get(c, 0) + 1
        og_count = count

        l = 0
        for r in range(len(s2)):
            print(s2[l:r+1])

            if s2[r] not in count.keys():
                l += 1
            elif s2[r] in count.keys() and count[s2[r]] != 0:
                count[s2[r]] -= 1
            elif count[s2[r]] == 0:
                count[s2[r]] = og_count[s2[r]]
                l = l + (og_count[s2[r]] - 1)
            elif r-l+1 == len(s1) and not all(count.values()):
                print(s2[l:r+1])
                return True
        return False

obj = Solution()
res = obj.checkInclusion('caab', 'eidcaaabaac')
print(res)
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_s1 = [0] * 26
        for c in s1:
            char_s1[ord(c) - ord('a')] += 1

        l = 0
        for r in range(len(s1), len(s2)+1, 1):
            char_s2 = [0] * 26
            for c in s2[l:r]:
                char_s2[ord(c) - ord('a')] += 1
            if char_s1 == char_s2:
                return True
            l += 1
        return False

obj = Solution()
res = obj.checkInclusion('caab', 'eidcaaabaac')
print(res)
