'''
Construct a square matrix with a size N x N containing integers from 1 to N*N in a spiral order,
starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
'''
def spiralNumbers(n):
    a=[[0 for x in range(n)] for y in range(n)]
    loc=(0,0)
    d=0
    for i in range(1,n**2+1):
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        if a[loc[0]][loc[1]]==0:
            if loc in [(0,n-1),(n-1,n-1),(n-1,0)]:
                d+=1
            a[loc[0]][loc[1]]=i
            loc=tuple(sum(x) for x in zip(loc,direction[d%4]))
            if a[loc[0]][loc[1]]!=0:
                loc=tuple(x-y for x,y in zip(loc,direction[d%4]))
                d+=1
                loc=tuple(sum(x) for x in zip(loc,direction[d%4]))
    return a