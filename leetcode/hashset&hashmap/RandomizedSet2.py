import random

class RandomizedSet2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.pos = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False
        
        self.values.append(val)
        self.pos[val] = len(self.values) - 1
        return True
        
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos:
            return False
        
        idx, last = self.pos[val], self.values[-1]
        self.values[idx] = last
        self.pos[last] = idx
        print(self.values,self.pos)
        self.values.pop()
        self.pos.pop(val,0)
        return True
            
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.pos:
            return self.values[random.randint(0,len(self.values)-1)]
        return False
        
        
# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet2()
param_1 = obj.insert(1)
param_2 = obj.remove(1)
param_3 = obj.getRandom()
print('ttt',param_1,param_2,param_3)
