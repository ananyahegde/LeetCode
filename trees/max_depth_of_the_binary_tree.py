"""
Return the maximum depth (height) of the binary tree.
A binary tree's maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.
There are 3 solutions here.

Solution 1 - recursive dfs:
    A very straightforward one. just do dfs return the max of all paths.
    So, when you do the dfs, remember, it goes left - right traversing all paths from root to every single node.
    Ok, but understanding the recursive part is sure hard.
    I left some pictures in one note at - `DSA_LC_CP_IP/Max depth of a binary tree - recursive dfs figures`.
    Check it out.

Solution 2 - bfs:
    Let's take this tree:
                3
              /    \
            9       20
           /       /   \
          4       15    7

    So in bfs, you have a queue. Initially you add root to the queue.
    You empty the queue entirely, and add every node's left, then right children.

    So, every iteration you are doing -
        - `traverse` the current level entirely and mark `em visited (dequeue those nodes)
        - add the nodes in the next level to queue

    So you can see how this approach is intuitive.
    Our bfs queue is gonna look like this from start to end - [3, 9, 20, 4, 15, 7]
        [3] - in the first pass
        [9, 20] - in the second pass
        [4, 15, 7] - in the third pass
    Hence, 3 levels.

Solution 3 - iterative dfs:

"""

# recursive dfs
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# bfs
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return 0

        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1

        return res
