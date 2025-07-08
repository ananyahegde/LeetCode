"""
    Create a dummy node of the node class to make sure that we return a `list`.
    maintain a pointer to merge list.
    compare values of two lists, and based on which is smaller, make merge list pointer point `point to that node`.
    If one of them gets over, copy all the elements in the other list (if there are any).
    return merged_head - dummy.next.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

# List, A
A = Node(10)
B = Node(20)
C = Node(30)
D = Node(40)
E = Node(50)
F = Node(60)

A.next = B
B.next = C
C.next = D
D.next = E
E.next = F

# List, B
M = Node(10)
N = Node(10)
O = Node(40)
P = Node(50)
Q = Node(60)
R = Node(90)

M.next = N
N.next = O
O.next = P
P.next = Q
Q.next = R

def print_list(head: Node) -> None:
    curr = head
    while(curr):
        print(curr, end="  ")
        curr = curr. next

# merging A and M
def merge(A: Node, M: Node) -> Node:
    dummy = Node(float('inf')) # just to make sure that we are merging into a `list`
    ptr = dummy

    while A and M:
        if A.val < M.val:
            ptr.next = A
            A = A.next
        else:
            ptr.next = M
            M = M.next
        ptr = ptr.next

    # If there is a remaining portion in one of them, we copy entire thing that point on
    if A:
        ptr.next = A

    if M:
        ptr.next = M

    return dummy.next

merged_head = merge(A, M)
print_list(merged_head)