s = "egg"
t = "add"

s1 = "foo"
t1 = "bar"

s3 = "paper"
t3 = "title"

s4 = "ab"
t4 = "aa"
 
def isIsomorphic(s, t):
    
    d = {}
    
    print(len(set(zip(s,t))))
    for i,j in zip(s,t):
        print(i,j)
        if i not in d:
            if j in d.values():
                return False
            d[i] = j
        elif d[i] != j:
            return False
    return True
            
            
   
    
print(isIsomorphic(s4,t4))    