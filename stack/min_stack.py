"""
Designing a stack class that supports stack operations -
    push, pop, top and `retrieve minimum element in constant time`.

The Input and Output:
    The input is going to be array of operation like ["MinStack", "push" ..] and
    the stack is given as list of lists - [[], [-2], [0], ...] and these two are of same length.
    Consider the second as an arguments passed to the operations in the first one.
    you have to return an array of same length, each time returning something - return null if its anything but getMin operation.

The first three are default operations of stack.
The last one - getting minimum in constant time is the problem.
You can get the minimum sure, but takes O(n) in brute force or naive solution.

Solution:
    One stack is our original stack.
    Maintain another stack, where you keep track of minumum at everypoint, like everytime you push, you keep track of the minimum.
    And when you pop, you pop off from this stack too (if the elements match, that would mean we popped our minimum, otherwise it
    just makes sure the number of elements in each stack is same, hard to explain but makes sense).
    The top of this stack always gonna hold minimum element, so we return top of this stack.
    So this is going to be O(1).

Example:
    Consider this stack - [-2, 0, -3]
    And our stack for keeping the minumum would be  - [-2, -2, -3].

Things to remember:
    Just keep another stack to track minimum at every push. and for pop, you pop from both.
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# please run it in leetcode, the input is quite different, and I won't do it here