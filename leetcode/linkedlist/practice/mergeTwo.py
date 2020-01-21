import MyLinkedList
import MyLinkedList

l1 = MyLinkedList.MyLinkedList()
l1.addAtTail(1)
l1.addAtTail(2)
l1.addAtTail(4)

l2 = MyLinkedList.MyLinkedList()
l2.addAtTail(1)
l2.addAtTail(3)
l2.addAtTail(4)

l1.printAll()
l2.printAll()



def mergeTwoLists(l1, l2):
    
    final = head = MyLinkedList.ListNode(0)
    
    while l1 and l2:
        if l1.val >= l2.val:
            final.next = l2
            l2 = l2.next
        elif l1.val < l2.val:
            final.next = l1
            l1 =l1.next
            
        final = final.next
        
    final.next = l1 or l2
    return head.next
    
    
f = mergeTwoLists(l1.head.next,l2.head.next)

while f:
    print(f.val)
    f = f.next

