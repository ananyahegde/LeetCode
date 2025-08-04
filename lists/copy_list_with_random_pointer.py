"""
The solution:
    Ok. This one is very simple, but I struggled a little to even understand the problem.
    Basically, they give you a list. Every node has these three things:
        - A value
        - A pointer to the next node
        - A random pointer pointing ANY node in the list randomly. (One node's random pointer only points to ONE another node, or null)

    You gotta create the EXACT CLONE of this list. And nothing in nowhere, the original list should get involved.
    You gotta create a brand new copy of each node,
    And each brand new copy's next and random pointer should point to brand new copy of nodes, exactly as in the original node.

    So doing like, `copy = og_node` wouldn't work. If you do so, it would just create a variable `copy` referencing to the same object as `og_node`.
    You wanna do `copy = Node(og_node.val)` instead.
    Also, you use a hashmap to store these old-new pairs. You need it while linking them.

    Once you've got your brand new copies of all nodes, it's time to link them accordingly.
    Again, if you do `copy.next = og_node.next`, `copy` would point to the node in the original list itself. We don't wanna do that.
    Instead, you wanna fetch the node og_node.next points to, and get the corresponding node from hashmap.
    So, `copy.next = hashmap[og_node.next]`.
    Same goes for random pointer.

    Once done and dusted, return the head of the new list, `hashmap[head]`.
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]': 
        old_to_new = {None: None}

        curr = head 
        while curr: 
            new = Node(curr.val)
            old_to_new[curr] = new
            curr = curr.next 

        curr = head 
        while curr: 
            new = old_to_new[curr] 
            new.next = old_to_new[curr.next]
            new.random = old_to_new[curr.random]
            curr = curr.next 

        return old_to_new[head]