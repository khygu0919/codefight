'''
Given two cells on the standard chess board, determine whether they have the same color or not.
'''
def chessBoardCellColor(cell1, cell2):
    a=[]
    b=[]
    a.extend((cell1[0],cell2[0]))
    b.extend((int(cell1[1]),int(cell2[1])))
    for i in range(len(a)):
        a[i]=ord(a[i])-64
    for i in range(len(a)):
        if a[i]%2==1:
            if b[i]%2==1:
                a[i]=1
            else:
                a[i]=0
        else:
            if b[i]%2==0:
                a[i]=1
            else:
                a[i]=0
    if a[0]!=a[1]:
        return False
    else:
        return True