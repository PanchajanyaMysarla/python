# Input: ["flower","flow","flight"]
# Output: "fl"

strs = ['flower','flow','flight']

strs2 = ['flower','flower','flower']

strs3= ['aa','ab']

strs4 = ["c","acc","ccc"]


def longestCommonPrefix(strs):
    
    prefix = strs[0]
    
    for i in range(1,len(strs)):
        
        while strs[i].find(prefix) != 0:
            prefix =  prefix[:len(prefix)-1]
    return prefix
    
print(longestCommonPrefix(strs4))
