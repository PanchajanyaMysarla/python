a = [1,2,3,2,1,5,6,5,5,5,9]
b = [1,2,2,3,3,3,4,5,6,7,7,8]

union = a + b
print(union,set(union))

uniq=set()
dups=set()
for i in union:
    if i not in uniq:
        uniq.add(i)
    else:
        dups.add(i)
print(uniq,dups, uniq-dups)
        


        
        
        

