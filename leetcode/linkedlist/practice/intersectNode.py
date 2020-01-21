def getIntersectionNode(self, headA, headB):
       
    p1 = headA
    p2 = headB
    
    while p1 !=  p2:
        
       
        if not p1:
            p1 = headB
        else:
            p1 = p1.next
        if not p2:
            p2 = headB
        else:
            p2 = p2.next
        
        
    return None    
    
        
        