# My solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)

        digits = []

        for digit in x:
            digits.append(digit)
        
        n = len(digits)

        for i in range(n):
            if digits[i] != digits[n-i-1]:
                return False
        return True
    
# better one
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x