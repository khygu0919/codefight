'''
Sudoku is a number-placement puzzle.

The objective is to fill a 9x9 grid with digits
so that each column, each row, and each of the nine 3x3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.
'''
def sudoku(grid):
    a=[]
    for k in range(3):
        a=[]
        for j in range(3):
            a=grid[k*3][j*3:j*3+3]+grid[k*3+1][j*3:j*3+3]+grid[k*3+2][j*3:j*3+3]
            for x in range(1,10):
                if a.count(x)>1:
                    return False
    for m in range(9):
        a=[]
        for x in range(1,10):
            if grid[m].count(x)>1:
                return False
        for n in range(9):
            a.append(grid[n][m])
        print a
        for x in range(1,10):
            if a.count(x)>1:
                return False
    return True