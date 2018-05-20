'''
Determine if the given number is a power of some non-negative integer.

Example

For n = 125, the output should be
isPower(n) = true;
For n = 72, the output should be
isPower(n) = false.
'''
import math
def gcd(n,m):
    for x in range(min(n,m),0,-1):
        if m%x==0 and n%x==0:
            return x
def getPower(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return i
def exactPow(a):
    x=list(a.values())
    if len(x)==1 and x[0]>1:
        return True
    elif len(x)>1:
        for i in range(1,len(a.values())):
            x[0]=gcd(x[0],x[i])
        return True if x[0]!=1 else False
    else:
        return False
def isPower(n):
    if n==1:
        return True
    a={}
    while 1:
        b=getPower(n)
        if b:
            n=n//b
            if b in a.keys():
                a[b]+=1
            else:
                a[b]=1
        else:
            if n in a.keys():
                a[n]+=1
                break
            else:
                a[n]=1
                break
    return exactPow(a)