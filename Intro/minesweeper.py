'''
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.
'''
def minesweeper(matrix):
    a=len(matrix)-1
    b=len(matrix[0])-1
    e=[]
    for i in range(a):
        for j in range(b):
            if matrix[i][j]==True: matrix[i][j]=1
            else: matrix[i][j]=0

    for i in range(a+1):
        c=[]
        for j in range(b+1):
            d=0
            if i==0 and j==0: d+=(matrix[i][j+1]+sum(matrix[i+1][j:j+2]))
            elif i==0 and j!=0 and j!=b: d+=(matrix[i][j-1]+matrix[i][j+1]+sum(matrix[i+1][j-1:j+2]))
            elif i==0 and j==b: d+=(matrix[i][j-1]+sum(matrix[i+1][j-1:j+1]))
            elif i!=0 and i!=a and j==0: d+=(sum(matrix[i-1][j:j+2])+matrix[i][j+1]+sum(matrix[i+1][j:j+2]))
            elif i!=0 and i!=a and j==b: d+=(sum(matrix[i-1][j-1:j+1])+matrix[i][j-1]+sum(matrix[i+1][j-1:j+1]))
            elif i!=0 and i!=a and j!=0 and j!=b: d+=(sum(matrix[i-1][j-1:j+2])+matrix[i][j-1]+matrix[i][j+1]+sum(matrix[i+1][j-1:j+2]))
            elif i==a and j==0: d+=(sum(matrix[i-1][j:j+2])+matrix[i][j+1])
            elif i==a and j==b: d+=(sum(matrix[i-1][j-1:j+1])+matrix[i][j-1])
            elif i==a and j!=0 and j!=b: d+=(sum(matrix[i-1][j-1:j+2])+matrix[i][j-1]+matrix[i][j+1])
            c.append(d)
        e.append(c)
    return e