class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or len(grid) == 0:
            return 0
        
        count= 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count+=1
                    self.dfs(grid,i,j)
        return count
                    
    def dfs(self,grid,i,j):
        
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)

# soln 2
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        R,C = len(grid),len(grid[0])
        count=0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    count+=1
                    stack = [(i,j)]
                    for r,c in stack:
                        if 0<=r<R and 0<=c<C and grid[r][c] == '1':
                            grid[r][c] = '2'
                            stack.extend([(r+1,c),(r-1,c),(r,c+1),(r,c-1)])
        
        return count
 
        