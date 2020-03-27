class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000 
        }
        
        
        num = hash.get(s[-1])
        for i in reversed(range(len(s)-1)):
            print(i)
  
            if hash[s[i+1]] > hash[s[i]]:
                num-=hash[s[i]]
            else:
                num+=hash[s[i]]
        return num
                
                
        