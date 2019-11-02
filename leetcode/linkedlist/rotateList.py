"""
Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

import MyLinkedList
linkedList = MyLinkedList.MyLinkedList()
linkedList.addAtHead(1)
linkedList.printAll()
linkedList.addAtTail(3)
#linkedList.printAll()
# linkedList.addAtIndex(1, 2)
# linkedList.addAtTail(4)

linkedList.printAll()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def rotateRightLinked(self, head: ListNode, k: int) -> ListNode:
        # 首先计算链表的长度
    cursor = head
    list_length = 0
    while cursor is not None:
        cursor = cursor.next
        list_length += 1
    if list_length == 0 or k == 0:
        return head
    # 计算长度
    remain_length = list_length - (k % list_length)
    if remain_length == list_length:
        return head
    cursor = head
    while remain_length > 1:
        remain_length -= 1
        cursor = cursor.next
        
    new_head = cursor.next
    cursor.next = None
    cursor = new_head
    while cursor.next is not None:
        cursor = cursor.next
        
    cursor.next = head
    return new_head
    
def rotateRightSlicing(head: ListNode, k: int):
    arr =[]
    while head:
        arr.append(head.val)
        head = head.next
    k =  k%len(arr)
    while k > 0:
        arr = [arr[-1]] + arr[:-1]
        k-=1
    
    print(arr)
        
    head = ll = ListNode(0)
    for i in arr:
        ll.next = ListNode(i)
        ll = ll.next
    
    return head.next


def rotateRight(head: ListNode, k: int):
    arr =[]
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)
    for _ in range(k):
        arr.insert(0,arr.pop())
        
    head = ll = ListNode(0)
    for i in arr:
        print(i)
        ll.next = ListNode(i)
        ll = ll.next
    
    return head.next 
        
ll = rotateRightSlicing(linkedList.head,2000000000)

while ll:
    print('ll',ll.val)
    ll = ll.next
    
    
    
    
    