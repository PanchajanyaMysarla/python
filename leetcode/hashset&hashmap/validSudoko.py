"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
"""


"""
lass Solution:
    def isValidRow(self, row: List[str]) -> bool:
        zero_to_nine = set()
        for x in row:
            if x in zero_to_nine:
                return False
            elif x != ".":
                zero_to_nine.add(x)
        return True
        
    def hasValidSubmatrixes(self, board: List[List[str]]) -> bool:
        for row in range (0, 3):
            for column in range (0,3):
                submatrix = set()
                for i in range (row * 3, row * 3 + 3):
                    for j in range (column * 3, column * 3 + 3):
                        if board[i][j] in submatrix:
                            return False
                        elif board[i][j] != ".":
                            submatrix.add(board[i][j])
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValidRow(row):
                return False
        for column in [list(i) for i in zip(*board)]:
            if not self.isValidRow(column):
                return False
        if not self.hasValidSubmatrixes(board):
            return False
        return True
        
Copyright © 2019 LeetCodeHelp Center  |  Jobs  |  Bug Bounty  |  Terms  |  Privacy Policy      United States

"""

"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            nums = [num for num in row if num != "."]
            if len(nums) != len(set(nums)): return False
        # check columns
        for col in range(len(board[1])):
            nums = [row[col] for row in board if row[col] != "."]
            if len(nums) != len(set(nums)): return False
        # check blocks
        for row in range(0,9,3):
            for col in range(0,9,3):
                block = board[row][col:col+3] + board[row+1][col:col+3] + board[row+2][col:col+3]
                block = [num for num in block if num != "."]
                print(block)
                if len(block) != len(set(block)): return False
        return True
"""
board =  [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

def isValidSudoku(board):
    rowCount, colCount, subCount = {}, {}, {}
    
    for i in range(9):
        for j in range(9):
            if board[i][j].isdigit():
            
                #check the row for the digit
                if board[i][j] in rowCount and i in rowCount[board[i][j]]:
                    return False
                else:
                    rowCount[board[i][j]] = rowCount.get(board[i][j], []) + [i]

                #check the column for the digit
                if board[i][j] in colCount and j in colCount[board[i][j]]:
                    return False
                else:
                    colCount[board[i][j]] = colCount.get(board[i][j], []) + [j]
               
                #check the sub-grid for the digit
                if board[i][j] in subCount and 3*(i//3)+j//3 in subCount[board[i][j]]:
                    return False
                else:
                    subCount[board[i][j]] = subCount.get(board[i][j], []) + [3*(i//3)+j//3]
                print(i,j,board[i][j],rowCount,colCount,subCount)
    
    return True
def isValidSudoku2(board):
    row = {}
    col = {}
    sub = {}
    
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            
            if val.isdigit():
                if val in row and i in row[val]:
                    return False
                else:
                    row[val] = row.get(val,[]) + [i]
                
                if val in col and j in col[val]:
                    return False
                else:
                    col[val] = col.get(val,[]) + [j]
                    
                print('sub',3*(i//3)+j//3)
                
                if val in sub and 3*(i//3)+j//3 in sub[val]:
                    return False
                else:
                    sub[val] = sub.get(val,[]) + [3*(i//3)+j//3]
                print(i,j,val,row,col,sub)
    return True
       
print(isValidSudoku(board))