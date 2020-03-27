class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        def bfs(forest,ti,ty,sx,sy):
            q= collections.deque([(sx,sy,0)])
            seen = {(sx,sy)}
            
            while q:
                r,c,d = q.popleft()
                if r == ti and c == ty:
                    return d
                for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if 0<=nr<len(forest) and 0<= nc< len(forest[0]) and (nr,nc) not in seen and forest[nr][nc]:
                        seen.add((nr,nc))
                        q.append((nr,nc,d+1))
            return -1
        
        trees= []
        
        R,C = len(forest),len(forest[0])
        
        for r in range(R):
            for c in range(C):
                if forest[r][c] > 1:
                    trees.append((forest[r][c],r,c))
        
        trees = sorted(trees)
        x,y,count = 0,0,0
        for h,i,j in trees:
            step = bfs(forest,x,y,i,j)
            if step < 0:
                return -1
            count+=step
            x,y = i,j
        
        return count
