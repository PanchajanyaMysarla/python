from collections import deque
class Solution:
    def orangesRotting(self, grid) :
        R,C = len(grid),len(grid[0])
        
        q = deque()
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] ==2:
                    q.append((i,j,0))
        
        d = 0
        
        while q:
            r,c,d = q.popleft()
            
            for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] =2
                        q.append((nr,nc,d+1))
            
        if any(1 in row for row in grid):
            return -1
        return d
s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))