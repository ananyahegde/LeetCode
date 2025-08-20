"""
The problem:
    you are given an array in such a fasion:
        - it contains n+1 integers.
        - each element falls in the range [1, n] both inclusive.
        - Exactly one number is repeated (twice or more).
    You gotta return this repeated number.

The solution:
    This does not seem too bad, you could use a hashset to do this.
    But the problem says O(1) space.
    You can sort the array and search for the duplicate, but this takes O(n^2). Can we do better?
    (The problem also says no modifying the original array, so you can't sort it either.)


    ---------- Linked list cycle ----------:
        (This is a linked list problem. Similar to detect cycle one.)

        Let nums = [1, 3, 4, 2, 2].
        they have the corresponding indeces, [0, 1, 2, 3, 4].

        Because of the problem's constraints, the following approach makes sense.

        Think of indices as nodes.
        Think of values in nums as pointers.
        i.e., You think each of the elements, that is array values, as pointers pointing to the index of that exact value.

        i:     0  1  2  3  4
        nums:  1  3  4  2  2

        We're focusing on the subarray from index 1 to 4, which is:
        [3, 4, 2, 2]

        Now treat each value as pointing to another index.
            n[0] = 1 → go to index 1
            n[1] = 3 → go to index 3
            n[3] = 2 → go to index 2
            n[2] = 4 → go to index 4
            n[4] = 2 → go to index 2 again...

        You see? It forms a cycle.
        If you represent this using list, it looks like this. The numbers written here are indices.

        0 -> 1 -> 3 -> 2 <-> 4

        Start at index 0 (0-based indexing)
        0 → 1 (because n[0] = 1)
        1 → 3 (n[1] = 3)
        3 → 2 (n[3] = 2)
        2 → 4 (n[2] = 4)
        4 → 2 (n[4] = 2)

        None of the nodes can ever point to 0th index, because our range is [1, n]. So the node 0 is never included in the cycle.
        Hence, we can always start from there.

        So what do we get from this?
        Notice how both nodes 3 and 4 points to 2. so that is more than one nodes pointing at one.
        So for the duplicate number, multiple nodes are gonna point to that node. You can see how 2 has 2 inward arrows.
        And this duplicate number is the beginning of that cycle.

        So once you know this, all you gotta do is detect the beginning of this cycle.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        ---------- Floyd's algorithm to detect the beginning of the cycle in a list ----------:
        This is the step for floyd's algorithm.
        You have three pointers, slow1, fast, slow2.

        set slow1 and fast to the beginning of the list.

        You move slow1 pointer 1 node at a time.
        You move fast pointer 2 at a time.
        They are both gonna intercept at some point, let's say at node d.

        once they are at d, the node of intersection, you stop the fast pointer.
        set slow2 to the beginning of the list.

        move slow1 one node at a time.
        move slow2 one node at a time.

        The node where these two intersect, is the beginning of the cycle. Our answer.

        But why would it even work?
        Let's think about it in a reverse way.

        So, with slow1 and slow2 we say, they meet each other at the beginning of the cycle.
        That must mean, the distance between beginning of the list and the beginning of the cycle (let's call this `p`),
        &  the distance between the intersection node d (where fast and slow1 met), and the beginning of the cycle (let's call this `x`),
        is same.

        But why this should be true?
        Let's call the length of the cycle `c`.
        So `c-x` is the remaining portion of the cycle.

        2*slow1 = fast ((---> eq 1))

        slow1 covers => p + (c - x)  ((---> eq 2))
        fast covers => p + (c - x) + x + (c - x) [fast HAS to cover the entire cycle once, by the time slow get's to the intersection, it should have already traversed the loop `atleast once`
                                                  (is it exactly once? answered below). that means, it covers (c-x)+x the cycle length, and (c-x) to get to the point of intersection.]
                    => p + c + (c-x) => p + 2c - x ( (---> eq 3))

        From equations 1, 2, and 3

            2(p + c - x) = p + 2c - x
            => 2p + 2c - 2x = p + 2c - x
            => 2p - p + 2c - 2c - 2x + x = 0
            => p - x = 0
            => p = x

        So, p = x. proved.

        But in cases where p > c, the fast pointer traverse the cycle `more than once`.
        So in that case, instead of `2c` in the equation, you'd have `nc`.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow1, fast = 0, 0

        while True:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            if slow1 == fast:
                break

        slow2 = 0
        while True:
            slow1 = nums[slow1]
            slow2 = nums[slow2]

            if slow1 == slow2:
                return slow1