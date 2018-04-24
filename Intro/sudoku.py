'''
Sudoku is a number-placement puzzle.

The objective is to fill a 9x9 grid with digits
so that each column, each row, and each of the nine 3x3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.
'''
def sudoku(grid):
    a=[]
    for i in range(3):
        for j in range(3):
            a+=grid[3*j+i][3*j:3*j+3]
    return a
grid=[[1,3,4,2,5,6,9,8,7], 
 [4,6,8,5,7,9,3,2,1], 
 [7,9,2,8,1,3,6,5,4], 
 [9,2,3,1,4,5,8,7,6], 
 [3,5,7,4,6,8,2,1,9], 
 [6,8,1,7,9,2,5,4,3], 
 [5,7,6,9,8,1,4,3,2], 
 [2,4,5,6,3,7,1,9,8], 
 [8,1,9,3,2,4,7,6,5]]
print sudoku(grid)
'''
 [3*n][3*m]~[3*n][3*m+2] [3*n+1][3*m]~[3*n+1][3*m+2] [3*n+2][3*m]~[3*n+2][3*m+2]
 [0][0]~[0][2],[1][0]~[1][2],[2][0]~[2][2]
 [0][3]~[0][5],~,~
 [0][6]~[0][8],~,~
 [3][0]~[3][2],~,~
 ~
 ~
 [6][0]
 [7]
 [8]
 '''