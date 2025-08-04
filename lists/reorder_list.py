"""
The problem:
    Check it out on leetcode.

The solution:
    This really is a combination of the last 3 easy leetcode questions -
        linked list cycle - fast and slow pointers
        reverse linked list
        merge two  sorted lists.

    So, what you do is, divide the list into two halfs. Use slow and fast pointer for this.
    Basically fast pointer moves twice as fast as slow pointer. And by the time fast is at the last
    node or at the end (null), slow would be at the `beginning` of the second half.

    Reverse the list from the slow pointer (second half).

    Then merge in such a fasion that, the first node is the first one, first half,
    second node is first one, second half and so on.
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

def print_list(head: Node) -> None:
    curr = head
    while(curr):
        print(curr, end="  ")
        curr = curr. next

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(6)

A.next = B
B.next = C
C.next = D
D.next = E
E.next = F

# print_list(A)

class Solution:
    def reorderList(self, head) -> None:
        slow, fast = head, head

        # get the middle element - slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversing from the middle element
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        """print_list(prev)
        print()
        print_list(head)"""

        # merge them
        p1 = head
        p2 = prev

        dummy = Node(float('inf'))
        dummy.next = p1

        while p1.next and p2.next:
            temp1 = p1.next
            temp2 =  p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2

        print_list(dummy.next)

x = Solution()
x.reorderList(A)
