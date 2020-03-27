def addTwo(a,b):
    res= []
    carry = 0
    while a or b:
        
        x = a.pop() if a else 0
        y = b.pop() if b else 0
            
        total = x + y + carry
        res.append(total%10)
        carry = total//10
    if carry != 0:
        res.append(carry)
    return res[::-1]
    
    
a =   [9,9,9]
b = [9,9,9,9]
    
print(addTwo(a,b))
    