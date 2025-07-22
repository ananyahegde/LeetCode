"""
The problem:
    Leetcode

The solution:
    Do binary search twice.
    First binary search is to find the right row.
    What you are doing is, finding a correct row the target might fall in.
    That row has - first element <= target <= last element.

    So, in your binary search, if the last element in the row you are at is strictly lesser than the target, then that row + all the rows before it
    do not have the target. Hence, if matrix[row][-1] < target then top = row + 1.
    Similarly, the other case. If the target is strictly smaller than the first element of current row, then that row + all the rows after it
    do not have the target. Hence, if matrix[row][0] > target then bot = row - 1.
    If none of these are true, then your are at the right row. break out of the loop.

    Once you have the current row, it is just the classic binary search.

"""
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # search for the right row
        n_row, n_col = len(matrix), len(matrix[0])
        top, bot = 0, n_row - 1

        while top <= bot:
            row = (top + bot)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        # search for the right element in the row
        l, r = 0, n_col - 1
        while l <= r:
            mid = (l+r)//2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
        return False


obj = Solution()
res = obj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11)
print(res)