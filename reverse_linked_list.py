"""
Two approaches: Recursion and Iterative.

Iterative Approach:
    - keep two pointers: curr and prev
    - curr points at the current node where you wanna take out its curr.next and point it to the previous node.
    - prev points at the previous node of curr.

    Given this list: A -> B -> C
    At B, we want to remove the link B -> C and make it A <- C.
    So point curr to B, and prev to A.
    curr.next = prev

    But when you wanna move to the next node, you would have already lost that info since curr.next now points to prev.
    So you gotta store that somewhere before you do the manipulation.

    After you've store the curr.next to temp initially and you've done curr.next = prev, you move prev and curr to the next node,
    prev = curr
    curr = temp (which points to the original next node link)

    `Remember two things, two pointers and store curr.next somewhere.`

Recursive approach:
    The logic is where simple. it's even similar to recursive dfs. if current node is null you just return,
    and if not you just iteratively call the same function. Depending on where you put the print statement,
    it'll either print the list in the correct order (put print before recursive function call) or in the
    reverse order (put print statement after the recursive call)
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

A = Node(10)
B = Node(20)
C = Node(30)
D = Node(-40)
E = Node(50)
F = Node(-60)

A.next = B
B.next = C
C.next = D
D.next = E
E.next = F

def print_list(head: Node) -> None:
    curr = head
    while(curr):
        print(curr, end="  ")
        curr = curr. next

print("Original List: ", end="")
print_list(A)
print("")

# recursion

def reverse_print_recursion(node):
    if not node:
        return

    # print(node, end=" ") # this prints it in the og way
    reverse_print_recursion(node.next)
    print(node, end=" ")

print("Reverse list recursion: ", end="")
reverse_print_recursion(A)
print("")

# Iterative

def reverse_list(head):
    curr = head
    prev = None

    while(curr):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


new_head = reverse_list(A)

print("Reversed List: ", end="")
print_list(new_head)
print("")



