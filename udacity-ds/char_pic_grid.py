grid2 = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

grid = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
    

for i in range(len(grid)):
    for j in range(len(grid[i])):
        
        if i < j:
            temp = grid[i][j]
            grid[i][j] = grid[j][i]
            grid[j][i] = temp
          
print(*grid, sep='\n')