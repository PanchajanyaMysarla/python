"""
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

"""
import MyLinkedList


def removeNthFromEnd( head, n):
    size = 0
    traverse = head
    while traverse:
        size+=1
        traverse= traverse.next
    print(size)
    
    previous = None
    for i in range(size - n ):
        print(i)
        previous =  head
        head =  head.next

    print(previous.val,head.val)
    previous.next =  head.next
    
    
    pass
    
def removeNthFromEndTwpPointer(head,n):
    first =  head
    second = head
    
    for i in range(n+1):
        if first:
            first = first.next
    print(first)

    while first != None:
        first = first.next
        second = second.next
    print(first,second.val)
    if second.next and second.next.next:    
        second.next = second.next.next
    else:
        second.next = None
        
    
        
linkedList = MyLinkedList.MyLinkedList()
linkedList.addAtHead(1)
#linkedList.printAll()
# linkedList.addAtTail(3)
# #linkedList.printAll()
# linkedList.addAtIndex(1, 2)
# linkedList.addAtTail(4)
# linkedList.addAtTail(5)
linkedList.printAll()
#linkedList.printAll()
# print(linkedList.get(3))          
# #linkedList.deleteAtIndex(1);
# linkedList.printAll()
# print(linkedList.get(0)) 

removeNthFromEndTwpPointer(linkedList.head, 1)
linkedList.printAll()