"""
my solution:
    so you will be given an integer which represents the number of digits, and a list of integers.
    You have to find the corresponding palindromes, e.g., if queries = [3, 88] and intLength = 4,
    you have to return a list - [3rd palindrome, 88th palindrome]. If the 88th palindrom does not exist, suppose,
    you return [3rd palindrome, -1].

    The bruteforce approach would be checking the number is palindrome or not, for every number with #digits = intLength.
    The range would be - lower limit is 10 to the power (intLength -1) and higher limit (10 to the power intLength) - 1.

    And append that to a linear data structure.
    Use a hashmap, tracking which palindrome it is, 1st, 2nd, or 3245th.

    return the value for key matching indices in queries.

    As I said, this is a brute force approach, so definately not an optimal one.
    It wouldn't take much to hit the `time exceeded` error.
"""

from collections import defaultdict
class Solution:
    def kthPalindrome(self, queries: list[int], intLength: int) -> list[int]:
        l = 10 ** (intLength - 1)
        h = 10 ** intLength - 1

        map = defaultdict(lambda: -1)
        res = []

        for i in range(l, h+1):
              if self.isPalindrome(i):
                  res.append(i)

        for idx in range(len(res)):
            map[idx] = res[idx]


        return [map[idx-1] for idx in queries]

    def isPalindrome(self, num):
        self.num = num
        temp = num
        rev_num = 0
        while num > 0:
            digit = num % 10
            rev_num = rev_num*10 + digit
            num = num // 10
        return temp == rev_num

x = Solution()
res = x.kthPalindrome([2,201429812,8,520498110,492711727,339882032,462074369,9,7,6], 1)
print(res)