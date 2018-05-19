'''
Determine if the given number is a power of some non-negative integer.

Example

For n = 125, the output should be
isPower(n) = true;
For n = 72, the output should be
isPower(n) = false.
'''
import math
def getPower(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return i
def exactPow(dict):
    if len(a.keys())==1:
        return True
    else:
        for i in len(a.values()):
            
def isPower(n):
    a={}
    while 1:
        b=getPower(n)
        print n,b
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
    return a
print isPower(0)
