'''
Given a rectangular matrix containing only digits, calculate the number of different 2x2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2x2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1
'''
def differentSquares(matrix):
    a=len(matrix[0])
    b=len(matrix)
    c=[]
    for i in range(b-1):
        for j in range(a-1):
            if not [matrix[i][j],matrix[i][j+1],matrix[i+1][j],matrix[i+1][j+1]] in c:
                c.append([matrix[i][j],matrix[i][j+1],matrix[i+1][j],matrix[i+1][j+1]])
    return len(c)