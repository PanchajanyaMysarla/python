s= ["flower","flow","flight"]

least  = ''
length = None
for i in range(len(s)):
    if length == None:
        length = len(s[i])
        least = s[i]
    elif len(s[i]) < length:
        length = len(s[i])
        least = s[i]
print(least,length)
        
pivot = least


for i in range(1,len(s)):
    print(i)
    while s[i].find(least) < 0:
        least = least[:len(least)-1]
    print(least)
        
        

    
