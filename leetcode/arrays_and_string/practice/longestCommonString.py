

# least  = ''
# length = None
# for i in range(len(s)):
#     if length == None:
#         length = len(s[i])
#         least = s[i]
#     elif len(s[i]) < length:
#         length = len(s[i])
#         least = s[i]
# print(least,length)
#         
# pivot = least
# 
# 
# for i in range(1,len(s)):
#     print(i)
#     while s[i].find(least) < 0:
#         least = least[:len(least)-1]
#     print(least)
        
s= ["flower","flow","flight"]

def isCommonPrefix(strs, index):
    for j in range(1,len(strs)):
        if not strs[j].startswith(strs[0][:index]):
            return False
        return True
        
    
    
    
    

def binarySearchLongestCommonStr(s):
    minLen = min([len(i) for i in s])
    #print(minLen)
    l = 0
    r = minLen -1
    while l < r:
        mid = l + r // 2
        if isCommonPrefix(s,mid):
            l= mid +1
        else:
            r = mid -1
    return s[0][:l+r // 2]  
        
        
print(binarySearchLongestCommonStr(s))
    
