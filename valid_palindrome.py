class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [myS.lower() for myS in s if myS.isalnum()]
        s  = ''.join(s)

        # or
        """
        for c in s:
            if c.alnum():
                newS += c.lower()
        """

        n = len(s)
        for i in range(n):
            if s[i] != s[n-i-1]:
                return False
        return True

        # or return newS == newS[::-1]

# or
# Two pointer metthod

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l+=1

            while r > l and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True