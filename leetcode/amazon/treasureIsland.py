class Solution:
    def treasureIsland(self,island):
        
        R,C = len(island),len(island[0])
        
        
        q = collections.deque((0,0),0)
        
        
        while q:
            r,c,step = q.popleft()
            
            for nr,nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                if 0 <=nr< R and 0 <=nc < C :
                    if island[nr][nc] == 'X':
                        return step+=1
                    if island[nr][nc] == 'O':
                        island[nr][nc] = 'D'
                        q.append(((nr,nc),step+1))
            