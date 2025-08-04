"""
The solution:
    When we say rotated sorted array (strictly, not fully sorted):
    We have two portions - left and right and usually the elements in the left portion are
    always greater than all the elements in the right sorted portion.
    The elements in this problem are unique, so you dont have to take care of `equal to` cases.

    We gonna consider all the cases basically.

    To determine whether we are in the left sorted portion or right sorted portion,
    check the condition, nums[m] < nums[l] => true -> right sorted portion, false -> left sorted portion.
    (Also notice, the condition nums[m] > nums[l] wouldn't work.)
    (left sorted portion)
    example array = [4, 5, 6, 7, 0]
    mid = 6 (mid is in the left sorted portion)
    left = [4, 5, 6, 7]
    right = [0]

    case 1:
        (If we are in the left sorted portion,)
        and if the target is greater than middle element (say 7),
        you can discard all the element left to it, i.e., 4 and 5. Hence, l = mid + 1

    case 2:
        (If we are in the left sorted portion,)
        and our target is less than middle element,
        you basically get two possibilities again - all the elements to its left (4 and 5) and
        all the elements in the right sorted region (0).

        How do you know which way to go?
        Again, compare target with smallest in the left sorted portion, nums[l],
        If target is greater than that, then you search in the left (nums[l] to nums[mid]). So, r = mid - 1.

        If our target is even smaller than the nums[l], then search in the right sorted portion. So, l = mid + 1.


    (right sorted portion):
    example array = [4, 5, 6, 7, 0, 1, 3]
    mid = 1 (mid is in the right sorted portion)
    left = [4, 5, 6, 7]
    right = [0, 1, 3]

    case 3:
        (If we are in the right sorted portion,)
        If our target was smaller than nums[mid], then we dont have to search right to it.
        So r = mid - 1

    case 4:
        (If we are in the right sorted portion,)
        If our target is greater, again, we have two possibilities:
        It could be to middle element's right; where all elements are greater than itself,
        or in the left sorted portion, where all elements are greater than right portion elements.

        How do you go about it?
        Again, compare target with nums[r], if the is lesser, then we search in the right portion, l = mid + 1
        If not, that means target is even greater nums[r], we search in left portion, where even greater elements
        lie, r = mid - 1.
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] < nums[l]:
                if target < nums[m]:
                    r = m - 1
                else:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
            else:
                if target > nums[m]:
                    l = m + 1
                else:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
        return -1

x = Solution()
res = x.search([5, 6, 7, 8, 1, 2, 3], 6)
print(res)