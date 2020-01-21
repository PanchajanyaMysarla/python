import MyLinkedList

h = MyLinkedList.MyLinkedList()
h.addAtTail(1)
h.addAtTail(2)
h.printAll()


"""
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        pointer = head
        total = 1
        while pointer.next:
            pointer = pointer.next
            total += 1
        
        pointer1 = head
        k = total - k % total
        if k == 0 or k == total:
            return head
        
        while k > 1:
            k -= 1
            pointer1 = pointer1.next    
        tmp = pointer1.next
        pointer1.next = None
        pointer.next = head
        return tmp
            
        
        
"""
def rotateRight(head, k):
    slow = fast = f = curr = head.next
    l = 0
    while curr:
        l+=1
        curr = curr.next
    print('len',l)
    
    k%=l
    print(k)
    
    for i in range(k):
        fast = fast.next
        
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    start = slow.next
    fast = head.next
    slow.next = None
    return start
        


p = rotateRight(h.head,2)

# while p:
#     print(p.val)
#     p =p.next