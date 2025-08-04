"""
The solution:

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
    def removeNthFromEnd(self, head, n):
        dummy = Node(float('inf'), head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

x = Solution()
x.removeNthFromEnd(A, 2)