'''
number feels comfortable with number b if a!=b and b lies in the segment
[a - s(a), a + s(a)], where s(x) is the sum of x's digits.

How many pairs (a, b) are there, such that a < b,
both a and b lie on the segment [l, r],
and each number feels comfortable with the other?
'''
def comfortableNumbers(l, r):
    x=[i for i in range(l,r+1)]
    a=0
    for i in x:
        y=[j for j in range(i+1,i+sum(int(k) for k in str(i))+1)]
        for j in y:
            if j>r:
                pass
            elif i in [k for k in range(j-sum(int(l) for l in str(j)),j)]:
                a+=1
    return a