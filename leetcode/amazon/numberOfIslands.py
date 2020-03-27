
"""
200. Number of Islands
Medium

4342

159

Add to List

Share
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
from collections import deque

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
        # def dfs(i,j):
        #     if 0 <= i < R and 0<=j<C and grid[i][j] == '1':
        #         grid[r][c] = '0'
        #         dfs((i-1,j))
        #         dfs((i+1,j))
        #         dfs((i,j-1))
        #         dfs((i,j+1))
        #         return 1
        #     return 0
