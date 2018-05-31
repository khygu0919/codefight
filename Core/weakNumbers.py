'''
the weakness of number x is the number of positive integers smaller than x that have more divisors than x.

It follows that the weaker the number,
the greater overall weakness it has. For the given integer n, you need to answer two questions:

what is the weakness of the weakest numbers in the range [1, n]?
how many numbers in the range [1, n] have this weakness?
Return the answer as an array of two elements,
where the first element is the answer to the first question,
and the second element is the answer to the second question.
'''
import math
def getPower(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return i
def getDivision(n):
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
    return a
def weakNumbers(n):
    x=[]
    y=[]
    for i in range(1,n+1):
        a=1
        for j in getDivision(i).values():
            a*=(j+1)
        x.append(a)
        y.append(sum(k>a for k in x))
    return [max(y),y.count(max(y))]