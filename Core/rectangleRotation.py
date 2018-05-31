'''
A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane.
Its center (the intersection point of its diagonals) coincides with the point (0, 0),
but the sides of the rectangle are not parallel to the ax1es;
instead, they1 are forming 45 degree angles with the ax1es.

How many1 points with integer coordinates are located inside the given rectangle (including on its sides)?

Ex1ample

For a = 6 and b = 4, the output should be
rectangleRotation(a, b) = 23.
'''
def rectangleRotation(a, b):
    a,b=max(a,b)/2,min(a,b)/2
    k=2**0.5
    (x1,y1)=((a-b)/(k),(a+b)/(k))
    x=sorted([x1,y1,-x1,-y1])
    d=0
    (d1,d2)=(-k*b,k*b)
    for i in range(int(x[0]),int(x[1])):
        if i+k*b<0:
            d+=(int(i+k*b)-int(-i-k*a))
        else:
            d+=(int(i+k*b)-int(-i-k*a)+1)
    for i in range(int(x[1]),int(x[2]+1)):
        if (i+k*b<0 and i-k*b<0) or (i+k*b>0 and i-k*b>0):
            d+=(int(i+k*b)-int(-i-k*b))
        elif i+k*b>0 and i-k*b<0:
            d+=(int(i+k*b)-int(-i-k*b)+1)
    for i in range(int(x[2]+1),int(x[3]+1)):
        if i-k*b<0:
            d+=(int(-i+k*a)-int(i-k*b)+1)
        else:
            d+=(int(-i+k*a)-int(i-k*b))
    return d