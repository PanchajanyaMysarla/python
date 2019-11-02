"""
Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

"""

import MyLinkedList

linkedList = MyLinkedList.MyLinkedList()
linkedList.addAtTail(1)
linkedList.addAtTail(2)
linkedList.addAtTail(3)
linkedList.addAtTail(3)
linkedList.addAtTail(2)
linkedList.addAtTail(1)
linkedList.printAll()


def isPalindromeSlowFast(head):
    
    slow =head
    fast = head
    stacks = []
    while fast and fast.next:
        stacks.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
        
    while slow:
        if stacks.pop() != slow.val:
            return False
        slow = slow.next
    return True


def isPalindrome(head):
    li = []
    while head:
        li.append(head.val)
        head = head.next
    print(li)
    l = 0
    r = len(li) -1
    while l < r:
        if li[l] != li[r]:
            return False
        l+=1
        r-=1
    return True

#print(isPalindrome(linkedList.head))
print(isPalindromeSlowFast(linkedList.head))
    