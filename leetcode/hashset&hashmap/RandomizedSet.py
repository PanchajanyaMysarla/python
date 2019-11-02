import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.id = -1
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dic:
            self.id+=1
            self.dic[val] = self.id
            return True
        return False
        
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dic:
            del self.dic[val]
            self.id-=1
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        values = list(self.dic.keys())
        if values:
            r = random.randint(0,len(values)-1)
            return values[r]
        return False
        
        
# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(1)
param_3 = obj.getRandom()
print('ttt',param_1,param_2,param_3)