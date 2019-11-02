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