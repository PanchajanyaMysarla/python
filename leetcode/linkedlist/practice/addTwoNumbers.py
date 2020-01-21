import MyLinkedList

l1 = MyLinkedList.MyLinkedList()
l1.addAtTail(2)
l1.addAtTail(4)
l1.addAtTail(3)

l2 = MyLinkedList.MyLinkedList()
l2.addAtTail(5)
l2.addAtTail(6)
l2.addAtTail(4)

l1.printAll()
l2.printAll()



def addTwoNumbers( l1, l2):
    
    l3 = head = MyLinkedList.ListNode(0)
    
    carry = 0
    
    
    while l1 or l2:
        
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        
        carry = total // 10
        total = total % 10
        
        l3.next = MyLinkedList.ListNode(total)
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        l3 = l3.next
        
    if carry > 0:
        l3.next = MyLinkedList.ListNode(carry)
    return head.next
    
f = addTwoNumbers(l1.head.next,l2.head.next)

while f:
    print(f.val)
    f = f.next
