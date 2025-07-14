#
# My solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(t) == len(s):
            letters_s = []

            for letter in s: 
                letters_s.append(letter)
            
            for l in t:
                if l not in letters_s: 
                    return False
                    break
                else:
                    letters_s.remove(l)
            return True
        return False
    
# Better one
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
