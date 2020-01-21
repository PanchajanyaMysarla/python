class SpecialStack:
    
    def __init__(self):
        self.store = []
        self.min = []
        self.max = []
    
    def getMin(self):
        return self.min[len(self.min)-1]
    
    def getMax(self):
        return self.max[len(self.max)-1]
    
    def isEmpty(self):
        return len(self.store) == 0
        
    def push(self,item):
        
        if self.isEmpty():
            self.store.append(item)
            self.min.append(item)
            self.max.append(item)
        else:
            self.store.append(item)
        
            mini = self.min.pop()
            self.min.append(mini)
            
            maxi = self.max.pop()
            self.max.append(maxi)
        
            if item <= mini:
                self.min.append(item)
            
            if item >= maxi:
                self.max.append(item)
        print('min',self.getMin())
        print('max',self.getMax())
            
    def pop(self):
        if self.isEmpty():
            return
        else:
            p = self.store.pop()
        
            mini = self.min.pop()
            maxi = self.max.pop()
        
            if mini != p:
                self.min.append(mini)
                
            if maxi != p:
                self.max.append(maxi)
            print('min',self.getMin())
            print('max',self.getMax())
            return p
        
    def printAll(self):
       print([i for i in self.store] , [j for j in self.min], [k for k in self.max])
        
        
ss = SpecialStack()
ss.pop()
ss.push(2)
ss.printAll()
ss.push(3)
ss.printAll()
ss.push(1)
ss.printAll()
ss.pop()
ss.printAll()