"""
The problem:
    To rotate a sorted array of n elements k times, while k<=n, you take the last k elements
    and move it to the front. For an example [a[0], .... a[n-2], a[n-1]] rotated twice will be
    [a[n-2], a[n-1], a[0], ....].
    You must give O(log n).
    And the values in the array are unique, which might really be significant.

The solution:
    Since atleast we have partially sorted array, we can use binary search.
    we will have three pointers at any point - l, mid, r.
    And we can divide the array into two parts - both sorted.
    Like if you have [3, 4, 5, 1, 2] (original array [1, 2, 3, 4, 5] rotated thrice)
    two sorted parts are [3, 4, 5] and [1, 2].

    Ok. you do mid = (l+r)//2. And we can say that is the minimum, because that value
    is the minimum we have found so far. but how do you proceed? how do you move your pointers?

    You have to find out where the mid lies. i.e., is it in the left portion of the array or right
    portion? and it can be at only one, not both.
    and when we rotate the sorted array, all the values in the left portion are always greater than the right,
    since we take the larger elements from the right and put it in the front (right).

    So, if you are at the left portion, where you have all the large elements, don't you wanna search in the right,
    where the lesser elements are?

    Ok. how do you check if the pointer is in the left portion? if it is at the left portion, it's gonna be greater
    than every element in the right portion - nums[m] >= nums[l].

    (You could also try to find the `pivot`, like [5,1] where the elements are not sorted. We are not doing that here.)
"""
"""
# works for non sorted arrays
class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) -1
        res = nums[0] # if the array is sorted, this is the min

        while l < r:
            mid = (l+r) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                l = mid + 1
        return res

obj = Solution()
res = obj.findMin([4,5])
print(res)
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0] # if the array is sorted, this is the min

        while l <= r:
            if nums[l] < nums[r]:
                res = nums[l]
                break

            mid = (l+r) // 2
            res = min(nums[mid], res)
            print(f"yellooo{res}")
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        print(f"oaeughaoeh{res}")
        return res

obj = Solution()
res = obj.findMin([4, 5, 1, 2, 3])
print(res)