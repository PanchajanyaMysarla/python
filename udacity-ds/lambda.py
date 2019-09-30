a = [1,2,3]
b = [4,5,6]
c = [7,8,9]


grid = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']
        ]

i,j,k = zip(*grid)

#print(i,j,k)



#print('\n'.join(list(map(''.join,zip(*grid)))))

for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j])
     

mapped = map(lambda x1,x2 : x1 * x2, a,b)

#print(list(mapped))