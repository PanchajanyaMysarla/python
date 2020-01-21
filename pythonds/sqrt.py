def sqrt(n):
    x = n/2
    for i in range(20):
        x= (1/2) * (x + n/x)
        print(x)
    
    return x
    
#print(sqrt(121))


def gcd(x,y):
    
    while x%y !=0:
        oldx = x
        oldy = y
        y = oldx
        x = oldx%oldy
    return y
print(gcd(30,15))