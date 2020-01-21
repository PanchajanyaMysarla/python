def toBinary(n,base):
    
    if n < base:
        return str(n)
    return toBinary(n//base,base) + str(n%base)

print(toBinary(10,2))


def toBase(n,base):
    s= '0123456789ABCDEF'
    if n < base:
        return s[n]
    return toBase(n//base,base) + s[n%base]
    
print(toBase(1453,16))   
def toBin(n):
    s = ''
    while n > 0:
        s+=str(n%2)
        n = n//2
    return s[::-1]
print(toBin(10))
        