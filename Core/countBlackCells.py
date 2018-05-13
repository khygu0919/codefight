'''
Imagine a white rectangular grid of n rows and m columns divided into two parts
by a diagonal line running from the upper left to the lower right corner.
Now let's paint the grid in two colors according to the following rules:

A cell is painted black if it has at least one point in common with the diagonal;
Otherwise, a cell is painted white.
Count the number of cells painted black.
'''
import math
def countBlackCells(n, m):
    a=[-n/float(m)*x+n for x in range(m+1)]
    matrix=[[0]*m for i in range(n)]
    print matrix, a
    for i in range(m):
        print i
print countBlackCells(3,4)
'''
y=-n/m*x+n
3 2.25 > 3
2.25 1.5 > 3,2
1.5 0.75 > 2,1
0.75 0 > 1
3 2 1 0
3 2 > 3,2
2 1 > 3,2,1
1 0 > 2,1
'''