
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def detectCycle(self, head: ListNode) -> ListNode:
        temp = head
        a = []
        while(temp):
            if temp not in a:
                a.append(temp)
            else:
                return temp
            temp = temp.next
        return None
    
    def hasCycle(self, head: ListNode) -> bool:
        node_set =  set()
        
        while head != None:
            if head in node_set:
                return True
            node_set.add(head)
            head =  head.next
            
        return False
    
    
    def hasCycleTwoPointer(self, head:ListNode):
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        
        while slow != head:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast =  fast.next.next
        return True
        
    