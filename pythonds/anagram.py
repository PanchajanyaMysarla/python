def anagram(s1,s2):
    
    if len(s1) != len(s2): return False
    str1 = {}
    str2 = {}
    for i in s1:
       str1.setdefault(i,0)
       str1[i]+=1
    
    for j in s2:
        str2.setdefault(j,0)
        str2[j]+=1
    print(str1,str2)

    return str1 == str2
        
print(anagram('hello','elloa'))
    
    # word with same length and same char count
    
    
