"""
The problem:
    You gotta add two nunbers, like, 3342 + 465 = 3817.
    The numbers are given in a linked list, like this:
        Each digit of the number is the value in the linked list.
        The linked list is in the reverse order.
        For example, the above two numbers would be -
        2 -> 4 -> 3 -> 3 and 5 -> 6 -> 4.
        And your answer should be - 7 -> 1 -> 8 -> 3.

The solution:
    The approach to this problem is really close to how you'd do it on the paper. I mean, literally.
    If you want to add two numbers, you'd first look at the digits at 0'th place and add them. You sum them
    up, and if it turns out to be 2 digit number, you carry the digit at the 10th place in the sum, to the next place.
    You do this recursively.

    There are two things - more or less edge cases - you wanna remember for this problem.

    First one is, when you add the numbers with uneven number of digits. Just like the example taken from above.
    We are dealing with linked list here. One of the lists is gonna hit the null sooner than the other.
    So we gotta assume that there is a zero in that place, so the number of nodes in both the lists is same.

    The other one is about the `carry`. Say you have 99 and 1. So that would be
    9  -> 9     =  (99)
    1 (-> 0)    =  (01)
    0 -> 0 -> 1 = (100)

    Notice how 1 got carried to the 100th place. So you have to remember to do this.
    Also, you only wanna carry if the carry is not 0, otherwise lc is gonna throw wrong answer at you.
    Because we don't wanna have any leading zero's in our answers (12 + 34 = 46 and 046 is not valid).

"""

# my solution
class Solution:
    def addTwoNumbers(self, l1, l2):
        nodes = {}
        carry = 0
        count = 1

        curr1 = l1
        curr2 = l2

        while curr1 or curr2:
            if not curr1:
                S = carry + curr2.val
                curr2 = curr2.next
            elif not curr2:
                S = carry + curr1.val
                curr1 = curr1.next
            else:
                S = carry + curr1.val + curr2.val
                curr1 = curr1.next
                curr2 = curr2.next

            nodes[count] = ListNode(S%10)
            carry = S//10
            count += 1

        if carry:
            nodes[count] = ListNode(carry)
            nodes[count+1] = None
        else:
            nodes[count] = None

        for key, value in nodes.items():
            if not value:
                break
            value.next = nodes[key+1]

        return nodes[1]


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            sum = val%10
            carry = val//10
            curr.next = ListNode(sum)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr.next = ListNode(carry)

        return dummy.next