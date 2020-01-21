class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        slow = head
        fast = head
        while slow != None:
            if fast.next == None or fast.next.next == None:
                return None
            else:
                fast = fast.next.next
                slow = slow.next

                if slow == fast:
                    while slow != head:
                        slow = slow.next
                        head = head.next
                    return head
                
                
def detectCycle2(self, head: ListNode) -> ListNode:
        if not head: return None
        fast, slow = head, head
        while True:
            if fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if not fast: return None
                elif slow == fast:
                    break
            else:
                return None
            
        p1, p2 = head, slow
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
    
  def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        slow = fast = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
            if slow == fast:
                slow = head
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            
            
        return None