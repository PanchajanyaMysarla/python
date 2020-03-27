class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1 = version1.split('.')
        n2 = version2.split('.')
  
        for i in range(max(len(n1),len(n2))):
            a = int(n1[i]) if i < len(n1) else 0
            b = int(n2[i]) if i < len(n2) else 0
            
            if a!=b:
                return 1 if a > b else -1
        return 0 
        
    from itertools import zip_longest

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        versions1 = list(map(int, version1.split(".")))
        versions2 = list(map(int, version2.split(".")))
        
        for v1, v2 in zip_longest(versions1, versions2, fillvalue=0):            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            
        return 0
class Solution3:
    def nextNum(self,version,p,n):
            if p > n-1:
                return 0,p
            p_end = p
            while p_end < n-1 and version[p_end] != '.':
                p_end+=1
            
            i = int(version[p:p_end]) if p_end != n-1 else int(version[p:n])
            
            p =p_end+1
            
            return i,p
        
    def compareVersion(self,version1,version2):
        
        
        p1,p2 = 0,0
        n1 = len(version1)
        n2 = len(version2)
        
        while p1 < n1 or p2< n2:
            i,p1 = self.nextNum(version1,p1,n1)
            j,p2 = self.nextNum(version2,p2,n2)
            
            if i != j:
                return 1 if i > j else -1
        return 0
s = Solution3()
print(s.compareVersion('1.2.0.0','1.2'))
        