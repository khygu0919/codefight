'''
After they became famous, the CodeBots all decided to move to a new building and live together. The building is represented by a rectangular matrix of rooms. Each cell in the matrix contains an integer that represents the price of the room. Some rooms are free (their cost is 0), but that's probably because they are haunted, so all the bots are afraid of them. That is why any room that is free or is located anywhere below a free room in the same column is not considered suitable for the bots to live in.

Help the bots calculate the total price of all the rooms that are suitable for them.
'''
def matrixElementsSum(matrix):
    a=len(matrix)
    b=[]
    c=0
    for i in range(0,a):
        for k in b:
            matrix[i][k]=0
            b=[]
        for j in range(0,len(matrix[i])):
            if matrix[i][j]==0:
                b.append(j)
            else:c+=matrix[i][j]
    return c