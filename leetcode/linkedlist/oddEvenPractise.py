
"""

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

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


def oddEvenList(head):
    odd = head
    even = evenHead = head.next
    
    while even and even.next:
        odd.next = even.next
        odd= odd.next
        even.next = odd.next
        even = even.next
    odd.next = evenHead
    
    return head

oddEven = oddEvenList(linkedList.head)


while oddEven:
    print(oddEven.val)
    oddEven = oddEven.next
    