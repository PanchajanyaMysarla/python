class Solution:
    def maxArea(self, height):
        area = 0
        
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                area = max(area, min(height[i],height[j]) * (j-i))
        return area
        
        
        
        
    def twoPointer(self,height):
        l = 0
        r = len(height) - 1
        area = 0
        
        while l < r:
            curr_area = min(height[l],height[r]) * (r -l )
            area = max(area,curr_area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return area
            
        
a = [1,8,6,2,5,4,8,3,7]       
s = Solution()
print(s.maxArea(a))
print(s.twoPointer(a))
