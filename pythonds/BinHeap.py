class BinHeap:
    
    def __init__(self):
        self.heapList = [0]
        self.size = 0
        
    def percUp(self,i):
        print(i,i//2)
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i],self.heapList[i//2] = self.heapList[i//2],self.heapList[i]
            i = i//2
            
    def percDown(self,i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc],self.heapList[i]
            i = mc
            
    def minChild(self,i):
        if i *2 +1 > self.size:
            return i*2
        if self.heapList[i*2] < self.heapList[i*2+1]:
            return i*2
        else:
            return i*2+1
                
    def insert(self,item):
        self.heapList.append(item)
        self.size+=1
        
        self.percUp(self.size)
        
    def delMin(self):
        retVal = self.heapList[1]
        self.heapList[1]= self.heapList[self.size]
        self.size-=1
        self.heapList.pop()
        self.percDown(1)
        return retVal
    
    def buildHeap(self,alist):
        i = len(alist)//2
        self.heapList = [0] + alist[:]
        self.size = len(alist)
        
        while i > 0:
            self.percDown(i)
            i-=1
        
binHeap = BinHeap()
binHeap.insert(1)
binHeap.insert(5)
binHeap.insert(2)

#binHeap.buildHeap([2,5,6,1,4])
print(binHeap.heapList)