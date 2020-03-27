from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        R,C = len(rooms),len(rooms[0])
        q = collections.deque()
        for i in range(R):
            for j in range(C):
                if rooms[i][j] == 0:
                    q.append((i,j,0))

        def neighbours(r,c,rooms):
            for nr,nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                if 0<=nr<len(rooms) and 0<=nc<len(rooms[0]) and rooms[nr][nc] == 2147483647:
                    yield nr,nc

        while q:
            r,c,d = q.popleft()

            for nr,nc in neighbours(r,c,rooms):
                rooms[nr][nc] = d+1
                q.append((nr,nc,d+1))
        return rooms
