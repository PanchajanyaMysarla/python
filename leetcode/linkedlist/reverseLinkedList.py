"""
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""
import MyLinkedList

def reverseList(head):
    previous = None
    current = head
    
    while current:
        nextTemp = current.next
        current.next = previous
        previous = current
        current = nextTemp

    return previous   
        
    pass 
   

linkedList = MyLinkedList.MyLinkedList()
linkedList.addAtHead(1)
linkedList.printAll()
linkedList.addAtTail(3)
#linkedList.printAll()
linkedList.addAtIndex(1, 2)
linkedList.addAtTail(4)
linkedList.addAtTail(5)
linkedList.printAll()

li = reverseList(linkedList.head)
while li:
    print(li.val)
    li = li.next


