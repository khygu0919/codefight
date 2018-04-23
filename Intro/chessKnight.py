'''
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it.
The complete move therefore looks like the letter L.
Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.
'''
def chessKnight(cell):
    a=(ord(cell[0])-96,int(cell[1]))
    b=[]
    b.append((a[0]+2,a[1]+1))
    b.append((a[0]+1,a[1]+2))
    b.append((a[0]+2,a[1]-1))
    b.append((a[0]+1,a[1]-2))
    b.append((a[0]-2,a[1]+1))
    b.append((a[0]-1,a[1]+2))
    b.append((a[0]-2,a[1]-1))
    b.append((a[0]-1,a[1]-2))
    c=0
    for i in b:
        if 9>i[0]>0 and 9>i[1]>0:
            c+=1
    print b
    return c