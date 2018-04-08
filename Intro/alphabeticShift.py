'''
Given a string, replace each its character by the next one in the English alphabet (z would be replaced by a).
'''
def alphabeticShift(inputString):
    a=[]
    for i in inputString:
        a.append(i)
    for j in range(len(a)):
        if a[j]=='z':
            a[j]='a'
            a[j]=chr(ord(a[j]))
        else:a[j]=chr(ord(a[j])+1)
    return ''.join(a)