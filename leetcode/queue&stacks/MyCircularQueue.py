class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q= [None] * k
        self.size = k
        self.front = self.rear = -1
        self.length = 0
        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front = (self.front+1)%self.size
        self.q[self.front] = value
        self.length += 1
        return True
      
        
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear+1)%self.size
        self.q[self.rear]= None
        self.length -=1
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        
        if self.isEmpty():
            return -1
        idx = (self.rear +1 )%self.size
        return self.q[idx]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.length == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.length == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
param_1 = obj.enQueue(1)
param_5 = obj.enQueue(2)
param_6 = obj.enQueue(3)
#param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()