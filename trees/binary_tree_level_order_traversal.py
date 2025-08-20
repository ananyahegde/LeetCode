"""
This is just implementing the bfs algorithm. With a small change.
You gotta return it in list of lists.
So, for the bfs algorithm itself, you make small nudges.

The bfs works as follows:
    You keep one queue data structure, add nodes from the rear end and pop nodes from the front.
    So, when you pop things out, you add it's children (or neighbours in graph's language, since this
    is a generally a graph traversal algorithm), from the rear end.

    You do this for all nodes, and remember to only add a node's child (left or right), if the node is not null.
    You run this loop until you no longer have nodes in the queue i.e., until queue is empty.

Coming to how to make it a REAL level order traversal (LOL):
    (explaining straight from the code)
    starting from the root, you add it to the queue. and since you can have only one root, only it's children are
    going to be the nodes in the next level. So root is gonna be your first level and it's children are in the next
    level.

    So, when you get to the second iteration of the loop, you would've poped the root. All the elements you have
    is the second level nodes. you can pop all of 'em (just go through as many iterations as length of queue),
    put it into a temperory list and add the popped nodes' children to the queue (which are, in fact, level 3 nodes).
    You can append this temp list to your `res` list at each loop.

Things to remember:
    in the `queue-while` loop make on temp list.
    loop through the current queue status and add everything.
    add nodes' children to the queue (provided node is not null).
    append temp list to res list.
"""

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs = []

        q = deque()
        q.append(root)

        while q:
            q_len = len(q)
            level = []
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                bfs.append(level)
        return bfs