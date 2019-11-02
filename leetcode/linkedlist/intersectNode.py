"""
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
"""
listA = [4,1,8,4,5]
listB = [5,0,1,8,4,5]
 
 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
def getIntersectionNode(self, headA, headB):
    if headA == None or headB ==None:
        return None
    
    a = set()
    while headA:
        a.add(headA)
        headA = headA.next
    while headB:
        if headB in a:
            return headB
        headB = headB.next
        
    return None

def getIntersectionNodeTwoPointer(self, headA, headB):
    if headA == None or headB ==None:
        return None
    tempA = headA
    tempB = headB
    
    while headA != headB:
        headA = headA.next if headA else tempB
        headB = headB.next if headB else tempA
    
    return headA



print(getIntersectionNode(listA,listB))