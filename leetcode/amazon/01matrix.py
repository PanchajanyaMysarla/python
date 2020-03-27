from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        R,C = len(matrix),len(matrix[0])
        
        q = deque()
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    q.append((i,j,0))
                else:
                    matrix[i][j] = -1
                    
        
        while q:
            r,c,depth = q.popleft()
            for nr,nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                if 0 <=nr<R and 0<=nc<C and matrix[nr][nc] == -1:
                    matrix[nr][nc] = depth+1
                    q.append((nr,nc,depth+1))
        return matrix