
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        newHead = Node(0,None,None)
        node_hash = {}
        temp = head
        newTemp = newHead = Node(-1,None,None)
        
        while temp:
            node_hash[temp] = Node(temp.val,None,None)
            new_temp.next = node_hash[temp]
            temp = temp.next
            new_temp = new_temp.next
            
            
        
        