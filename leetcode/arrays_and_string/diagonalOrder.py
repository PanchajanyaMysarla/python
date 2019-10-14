d2 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

d1 =[
    [6,9,7]
    ]

d3= [
    [3],
    [2]
    ]

d4= [
    [7],
    [9],
    [6]
    ]

d5 = [
    [2,5],
    [8,4],
    [0,-1]
    ]

d6 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
"""

00 01 02
10 11 12
20 21 22


"""
  
def findDiagonalOrder(arr):
    if len(arr) == 0: return []
    i = 0
    j = 0
    final = []    
    m= len(arr)
    n = len(arr[0])
    print(m,n)
        
    for k in range(m*n):
        
        print(k,i,j)
        final.append(arr[i][j])
        
        if i == j:
            
            if i-1 >= 0 and j+1 < n:
                i-=1
                j+=1
            elif j+1 < n:
                j+=1
            else:
                i+=1
                
        elif i < j:
            
            if i+1 < m and j-1>=0 and i+1 != j-1:
                i+=1
                j-=1
            elif j+1 < n:
                j+=1
                
            elif i == 0 and i+1 < m:
                i+=1
          
        elif i > j:
            
            if m > i+1 >= 0 and j-1 >=0:
               i-=1
               j-=1
               
            elif i+1 < m and j >= 0:
                i+=1
                
            elif i-1 == j+1:
                i-=1
                j+=1
            
            else:
               
                j+=1
    return final

"""

00 01 02
10 11 12
20 21 22


"""     

        
print(findDiagonalOrder(d6))