'''
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.
'''
def deleteDigit(n):
    n=str(n)
    a=[]
    b=[]
    for i in n:
        a.append(i)
    for j in range(len(n)):
        b.append(int(''.join(a[:j]+a[j+1:])))
    return max(b)