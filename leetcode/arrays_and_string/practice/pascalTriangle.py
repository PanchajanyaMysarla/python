

def pascals(n):
    triangle = []
    
    for i in range(n):
        #print('i',i)
        row = [None for _ in range(i+1)]
        row[0],row[-1] = 1,1
        
        for j in range(1,len(row)-1):
            print('j',j)
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
        print(i,row)
    print(triangle)

print(pascals(5))