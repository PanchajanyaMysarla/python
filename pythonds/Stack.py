class Stack:
    
    def __init__(self):
        self.store = []
    
    def push(self,item):
        self.store.append(item)
    
    def pop(self):
        self.store.pop()
    
    def peek(self):
        return self.store[len(self.store) -1]
    
    def isEmpty(self):
        return len(self.store) == 0
    
    def size():
        return len(self.store)
        
        

def revStr(s):
    x = []
    z= []
    for i in s:
        x.append(i)
        
    while len(x) > 0:
        z.append(x.pop())
        
    return z
#print(revStr('hello'))


def parCheck(s):
    stack = []
    for i in range(len(s)):
        
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    
    return len(stack) == 0
print(parCheck('(()))'))
                
                
        
    