"""
class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: 'int') -> 'int':
        if index < 0 or index >= self.size or \
            self.head is None:
            return -1
        return self.findIndex(index).val
        
    def addAtHead(self, val: 'int') -> 'None':
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: 'int') -> 'None':
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index: 'int', val: 'int') -> 'None':
        if index > self.size:
            return -1
        elif index == 0:
            head = ListNode(val)
            head.next, self.head = self.head, head
        else:
            pre = self.findIndex(index-1)
            cur = ListNode(val)
            cur.next, pre.next = pre.next, cur
        self.size += 1
        
    def deleteAtIndex(self, index: 'int') -> 'None':
        if index < 0 or index >= self.size:
            return -1
        cur = self.findIndex(index-1)
        cur.next = cur.next.next
        self.size -= 1
        
    def findIndex(self, index: 'int') -> 'None':
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur
        """



"""

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        head = self.head
        for i in range(index):
            if head:
                head = head.next
            else:
                break
        return head.val if head else -1

    def addAtHead(self, val):
        if not self.head:
            self.head = ListNode(val=val, next=None)
        else: 
            temp = self.head
            self.head = ListNode(val=val, next=temp)
        
    def addAtTail(self, val):
        if not self.head:
            self.head = ListNode(val=val, next=None)
        else: 
            head = self.head
            while head.next:
                head = head.next
            head.next = ListNode(val=val, next=None)
        

    def addAtIndex(self, index, val):
        if index == 0: return self.addAtHead(val)
        
        head = self.head
        if head:
            for i in range(index-1):
                if head.next:
                    head = head.next
                else:
                    return 
            temp = ListNode(val=val, next=head.next)
            head.next = temp    
        

    def deleteAtIndex(self, index):
        head = self.head
        if head:
            if index == 0:
                self.head = self.head.next
            else:
                for i in range(index-1):
                    if head.next:
                        head = head.next
                    else:
                        return
                if head.next:
                    head.next = head.next.next
                    
                    """



"""

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0)
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
            
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return 
        
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        new_node = ListNode(val)
        new_node.next = pred.next
        pred.next = new_node
        
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return 
        
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        pred.next = pred.next.next
        
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

"""

class Node:
    
    def __init__(self,val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.head = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current = self.head
        
        if index == 0:
            return current.val
        
        for i in range(index):
                current = current.next
        if current:
            return current.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val)
        
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode= Node(val)
        
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
            
            
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        current = self.head
        
        if index == 0:
            self.addAtHead(val)
        else:
            for i in range(index-1):
                current = current.next
            
            newNode= Node(val)
            newNode.next = current.next
            current.next = newNode
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        current = self.head
        previous = None
        
        for i in range(index):
            previous = current
            current = current.next
        
        if previous:
            previous.next = current.next
        else:
            self.head = current.next
        
    def printAll(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.val)
            current = current.next
        print('Nodes',nodes)
        

        
# Your MyLinkedList object will be instantiated and called as such:
# linkedList = MyLinkedList()
# linkedList.addAtHead(1)
# linkedList.printAll()
# linkedList.addAtTail(3)
# linkedList.printAll()
# linkedList.addAtIndex(1, 2)
# linkedList.printAll()
# print(linkedList.get(3))          
# linkedList.deleteAtIndex(1);
# linkedList.printAll()
# print(linkedList.get(0)) 