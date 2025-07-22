"""
The problem:
    self explainatory. return true if there is a cycle.
    The input is given in a list (like an array) and a position is given where the last node points to.
    The description says - `Note that pos is not passed as a parameter.`
    So I don't know how that works and I can't run the program here.
    Just dropping the solution.

The solution:
    We use the `fast and slow pointer` technique.
    Here's how it works - you traverse a linked list with two pointers, one moving one node per iteration and one at two nodes per iteration
    (slow and fast respectively). You can pick other than two of course, but has to be other than 1. 2 is just more efficient(?).

    The idea here is if you do this, the fast pointer WILL reach the slow pointer at some point if the loop exists.
    Why?
    Imagine a clock and two pointers are moving clockwise.
    Let slow be at 9.
    Let fast be at 2.
    (These can be any arbitrary position really, doesn't matter.)

    For fast to reach slow we've got 7 units (nodes) to travel.
    If you move slow 1 at a time and fast 2 at a time,
    At the first iteration you do 9+1 = 10 and 2+2 = 4. Hence you get 6 units to travel.
    At each action/iteration, you are doing current distance to travel + 1 (moving slow pointer by 1 will increase the distance) -
    2 (moving slow pointer by 2 will decrease the distance) = currDist - 1.

    So whatever the original distance was, in that many iterations fast pointer would reach slow pointer.
    Which means it WILL.

Key things:
    Slow and Fast pointers - shift slow by 1 and fast by 2 each time.
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False