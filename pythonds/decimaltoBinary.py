def decimalToBinary(n):
    
    remstack = []
    while n > 0:
        rem = n%2
        remstack.append(rem)
        n = n//2
    
    binStr = ''
    while len(remstack) != 0:
        binStr+=str(remstack.pop())
    return binStr
        
print(decimalToBinary(42))

def baseConvertor(n,base):
    
    remStack = []
    digits = '0123456789ABCDEF'
    
    while n > 0:
        rem = n%base
        remStack.append(rem)
        n = n // base
    
    s = ''
    
    while len(remStack) != 0:
        s+=digits[remStack.pop()]
        
    return s
print(baseConvertor(10,16))
        