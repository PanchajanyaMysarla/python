
"""

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""
import MyLinkedList

linkedList = MyLinkedList.MyLinkedList()
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2)
linkedList.addAtTail(4)
linkedList.addAtTail(5)
linkedList.addAtTail(3)
linkedList.printAll()




def removeElements(head, val):
    
    while head and head.next:
        if head.next.val == val:
            head.next = head.next.next
        head = head.next
        
removeElements(linkedList.head,3)
linkedList.printAll()


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
                
        p = head
        
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        
        if head.val == val:
            head = head.next
            
        return head
    
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return sentinel.next