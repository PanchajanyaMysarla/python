"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import MyLinkedList

l1 = MyLinkedList.MyLinkedList()
l1.addAtTail(1)
l1.addAtTail(2)
l1.addAtTail(4)
l1.addAtTail(5)

l2 = MyLinkedList.MyLinkedList()
l2.addAtTail(1)
l2.addAtTail(3)
l2.addAtTail(4)

l1.printAll()
l2.printAll()

def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    
    l3 = MyLinkedList.MyLinkedList()
    while l1 and l2:
        l3.addAtTail(l1.val)
        l3.addAtTail(l2.val)
        l1 = l1.next
        l2 = l2.next
        
    while l1:
        l3.addAtTail(l1.val)
        l1 = l1.next
        
    while l2:
        l3.addAtTail(l2.val)
        l2 =l2.next
        
    return l3

def mergeTwo2(l1,l2):
    
    if not l1:
        return l2
    elif not l2:
        return l1

    left = l1
    right = l2
    
    head = sortedList = ListNode(0)
 
    while left and right:
        
        if left.val < right.val:
            head.next = left
            left = left.next
            head = head.next
        else:
            head.next = right
            head = head.next
            right = right.next
    
    head.next = left or right
    
    return sortedList.next
        
list3 = mergeTwo2(l1.head,l2.head)

while list3:
    print(list3.val)
    list3= list3.next








