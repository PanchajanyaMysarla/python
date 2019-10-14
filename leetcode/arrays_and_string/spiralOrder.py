"""

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

"""

d2 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

def spiralOrder(matrix):
    final =[]
    r = len(matrix)
    c = len(matrix[0])
    seen = [[False] * c for i in matrix]
    i = 0
    j = 0
    print(r,c,seen)
    for _ in range(r * c):
        print(i,j)
        
        final.append(matrix[i][j])
        seen[i][j] =True
        
        if j < c-1 and not seen[i][j+1]:
            if j >= i:
                j+=1
            else:
                j-=1
        elif i < r -1 and not seen[i+1][j]:
            if i >= j:
                i+=1
            else:
                i-=1
       
#         elif j-1 < 0 and not seen[i][j-1]:
#             i-=1
            
            
        
        
        
    print(final,seen)

print(spiralOrder(d2))