
import MyLinkedList



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
        
    
def reverseList( head):
    
    prev= None
    curr = head
    
    while curr:
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp
        
    return prev
    
def reverseList(ListNode head) {
    if (head == null || head.next == null) return head;
    ListNode p = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return p;
}
    
    
a = MyLinkedList.MyLinkedList()
a.addAtTail(1)
a.addAtTail(2)
a.addAtTail(3)
a.addAtTail(4)
a.addAtTail(5)
a.head = a.head.next
a.printAll()

a.head =reverseList(a.head)
a.printAll()
