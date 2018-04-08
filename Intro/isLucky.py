'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.
'''
def isLucky(n):
    a=str(n)
    b=[]
    c=0
    n=0
    for i in a:
        b.append(i)
    for j in range(0,len(b)//2):
        c+=int(b[j])
    for k in range(len(b)//2,len(b)):
        n+=int(b[k])
    if c==n:
        return True
    else:return False