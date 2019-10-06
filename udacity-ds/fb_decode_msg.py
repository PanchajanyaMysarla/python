#alpabets = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    
str ='1234'
    
    
def helper(data):
    if len(data) == 0:
        return 1
    elif data[0] == '0':
        return 0
    res = helper(data[:len(data)-1])
    if len(data) >=2 and int(data[:3]) <=26:
        res += helper(data[:len(data)-2])
        return res
    else:
        res += helper(data[:len(data)-2]) + helper(data[:len(data)-3])
        return res
    
    
def num_ways(data):
    return helper(data)


print(num_ways(str))