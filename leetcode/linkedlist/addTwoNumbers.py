"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
class ListNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None

a = [2,4,3]
b = [5,6,4]

c = [5]
d = [5]

e = [1,8]
f = [0]

g = [9,9,9,9]
h = [1]

i = [9,8]
j = [1]


k = [3,7]
l = [9,2]



def linkedList(a):
    l1 = list1 = ListNode(0)
    for i in a:
        l1.next = ListNode(i)
        l1 = l1.next
    return list1.next
        
list1 = linkedList(a)
list2 = linkedList(b)

list3 = linkedList(c)
list4 = linkedList(d)

list5 = linkedList(e)
list6 = linkedList(f)

list7 = linkedList(g)
list8 = linkedList(h)

list9 = linkedList(i)
list10 = linkedList(j)

list11 = linkedList(k)
list12 = linkedList(l)


def addTwoNumbers(l1: ListNode, l2: ListNode):
    dummyHead = ListNode(0)
    p =l1
    q= l2
    curr = dummyHead
    carry = 0
    while p or q:
        x = p.val if p else 0
        y = q.val if q else 0
        total = x + y + carry
        carry = total //10
        curr.next = ListNode(total%10)
        curr = curr.next
        if p:
            p = p.next
        if q:
            q = q.next
            
    if carry > 0:
        curr.next = ListNode(carry)
    
    return dummyHead.next
        
    
lii = addTwoNumbers(list11,list12)

while lii:
    print('f',lii.val)
    lii = lii.next