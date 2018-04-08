'''
Given a string, find out if its characters can be rearranged to form a palindrome.
'''
def palindromeRearranging(inputString):
    b=[]
    c=[]
    d=[]
    for i in inputString:
        b.append(i)
    c=list(set(b))
    for i in c:
        d.append(b.count(i))
    b[0]=0
    if len(inputString) %2 !=0:
        for i in d:
            if i %2!=0:
                b[0]+=1
                if b[0]>1:
                    return False
                    break
        return True
    else:
        for i in d:
            if i %2 !=0:
                return False
                break
        return True