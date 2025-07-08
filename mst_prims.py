"""
We're given set of points. You can represent them in a 2d plane.
In this leetcode problem, the edges are not given, so we have to construct them.
Which is pretty easy, basically all possible edges are gonna be in our (adjecency) list.
After this, it's just applying prim's algorithm to find MST, and then find the cost (that's
what we have to return).

Prim's algorithm:
    We wanna construct an MST (Minimum spanning tree, that's what prims does), while minimizing the
    path cost.

    To make sure every node visited only once, you keep track of visited nodes in a `hash set`.
    And to find optimal path (minimum path cost) you gonna keep a priority queue - a min heap.
    And this heap, roughly, will look like this: (node, cost) (or reverse, based on the implementation)

"""

def minCostConnectPoints(points: list[list[int]]) -> int:
    N = len(points)

    adj = {i:[] for i in range(N)} # just map an empty list indices 0, 1, 2, ..
                                   # i : [cost, node]
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i+1, N):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])
    print(adj)

points = [[3,12],[-2,5],[-4,1]]
minCostConnectPoints(points)