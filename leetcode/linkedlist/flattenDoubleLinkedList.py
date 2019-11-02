"""


Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
"""

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: Node):
        stack, curr, root = [], head, head
        
        while stack or curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                new = curr.child
                new.prev = curr
                curr.child = None
                curr.next = curr = new
            elif not curr.next and stack:
                curr.next = stack.pop()
                curr.next.prev = curr
                curr = curr.next
            else:
                curr = curr.next
        return root
    
    
    def flattenUsingStack(self,head):
        stack,curr,root = [], head,head
        
        while stack or curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                new = curr.child
                new.previous = curr
                curr.child = None
                curr.next = curr = new
            elif not curr.next and stack:
                curr.next = stack.pop()
                curr.next.prev = curr
                curr = curr.next
            else:
                curr = curr.next
        return root
    