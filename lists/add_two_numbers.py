# my solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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