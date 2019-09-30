str2 ='hello'
str = list(str2)

print(str)

i = 0
j = len(str) -1

while i < j:
    temp = str[i]
    str[i]= str[j]
    str[j] = temp
    i+=1
    j-=1
    
    
print(str)