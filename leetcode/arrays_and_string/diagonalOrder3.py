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
    
    final = []
    
    bottom_left = []
    diagonal = []
    top_right = []
    
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if x == y: diagonal.append(arr[x][y])
            elif x > y: bottom_left.append(arr[x][y])
            else: top_right.append(arr[x][y])
    
    print('bot_left',bottom_left)
    print('diagonal',diagonal)
    print('top_right',top_right)
    
    index = 0
    for i,j,k in zip(diagonal,top_right,bottom_left):
        if index == 0:
            print(index,i,j,k)
            final.extend([i,j,k])
        elif index%2 == 0:
            print(index,j,k,i)
            final.extend([j,k,i])
        else:
            print(index,k,i,j)
            final.extend([k,i,j])
        index+=1
        
    return final

"""

00 01 02
10 11 12
20 21 22

00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33
"""     

        
print(findDiagonalOrder(d6))

