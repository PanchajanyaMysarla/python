"""
54. Spiral Matrix
Medium

1870

516

Add to List

Share
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R,C = len(matrix),len(matrix[0])
        
        ans= []
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        
        r = c = di = 0
        seen = [[False]* X for _ in range(R)]
        for _ in range(R*C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr,cc =r +dr[di] , c + dc[di]
            if 0<=cr<R and 0<=cc<C and not seen[cr][cc]:
                r,c = cr,cc
            else:
                di = (di +1) % 4
                r,c = r + dr[di],c +dc[di]
        return ans