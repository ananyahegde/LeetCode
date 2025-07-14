"""
Problem explaination:
     You have given `numCourses` and our nodes will be labelled from 0 to numCourses-1.
     Some course have pre-requisites.
     Ex: you have to take course 1 before you can take course 0 - represented as a pair [0, 1].
     (The prereq comes second, [course, prereq]).

     Given number of courses and prereq pairs (only two) you have to check if it's possible to finish
     all the courses or not (return True or False).

Explaination:
    So the courses are gonna be our nodes.
    You've given a pair like this [1, 0] means 0 <- 1 (or 1 -> 0) - a directed graph.
    These pairs are given in a list - so it's a list of lists like, [[1, 0], [1,  2]].

    An expample where it's impossible is - [[1, 0], [0, 1]] - 0 ⇄ 1.
    This is cycle. So you end up in a loop.

    So if there is a cycle we return False.

Solution:
    Can be solved with DFS (BFS also).

    Example: n=5
             prereq = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]

    The graph looks like this:

    2    4 <-
    ^    ^   \
    |    |    \
    0 -> 1 -> 3

    (Hope you can make it).

    you have #prereqs pair edges (The inner dim or prereqs).

    We are gonna construct an adjecency list using a hashmap like this.

    course      prereqs
    0           [1, 2]
    1           [3, 4]
    2           []
    3           [4]
    4           []

    so the [] tells us that, that course can be completed. We do DFS until we reach that node
    and mark it as `can be completed`.

    If you start at 0 and take path 0 -> 1 -> 3 -> 4, you can mark 4 as completed.
    You come back to it's parent 3, and since 4 is completed, its prereqs are []. so mark 3 as completed.
    Come back to 1 and both 3, 4 are completed so 1's prereqs are now []. mark 1 completed.

    Come back to 0.
    Go to 2.
    2 has [], so mark it completed.
    Come back to 0. it has [] now. so mark completed.

    We completed all course now.
    Return True.

    This is topological sorting.
    order in which we finished - [4, 3, 1, 2, 0]

    Time complexity:
        we have to process n nodes (and you dont visit any node twice).
        and we have to go through p edges to check if the adjecent nodes are processed or not.
        Hence O(n+p).

    We still haven't talked how to detect a loop.
    To do that we are gonna use a hash set - visitSet where we store all the nodes we are visiting while doing DFS
    (not thevisited nodes).

    so you have 0, 1, 2 in a loop, and say you start from 0.
    you add 0 to visitSet.
    go to 1, add 1 to visitSet.
    go to 2, add 2 to visitSet.
    and 2 goes to 0 again, which is already in the visitSet.
    That is how we detect a loop.

Key points: Make an adjecency list
            Detect cycle in graph (make a set to keep track of visited node along the way of dfs)
            use dfs on every nodes
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # adjecency list
        preMap = {i:[] for i in range(numCourses)}

        for course, prereqs in prerequisites:
            preMap[course].append(prereqs)

        # visitSet - all courses along the current DFS
        visitSet = set()

        def dfs(course):
            if course in visitSet:
                return False # detected a loop

            if preMap[course] == []:
                return True # that course can be completed

            visitSet.add(course) # course is not visited in dfs and have adjecents
            for pre in preMap[course]: # do bfs on each adjecent nodes
                if not dfs(pre):
                    return False # loop case

            visitSet.remove(course) # dfs on course is done and no loop detected, we can process the node
            preMap[course] = [] # all the adjecent nodes are processed
            return True

        # loop through each course and perform dfs (doing so to make sure it works with isolated nodes/subgraphs)
        for course in range(numCourses):
            if not dfs(course): return False

        return True


x = Solution()
res = x.canFinish(5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]])
print(res)