"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution:
    def generateMatrix(self, n: int):

      spiral = [[0]*n for _ in range(n)]
      print(spiral)
      i,j = 0,0
      di,dj = 0,1

      for k in range(n*n):
        spiral[i][j] = k+1
        print((i+di)%n,(j+dj)%n)
        if spiral[(i+di)%n][(j+dj)%n]:
          di,dj = dj,-di
        i+=di
        j+=dj
      return spiral
s = Solution()
print(s.generateMatrix(3))
