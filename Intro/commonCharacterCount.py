'''
Given two strings, find the number of common characters between them.
'''
def commonCharacterCount(s1, s2):
    a1={}
    b1={}
    a2=0
    for i in s1:
        if i in a1:
            a1[i]+=1
        else:a1[i]=1
    for j in s2:
        if j in b1:
            b1[j]+=1
        else:b1[j]=1
    for i in a1.keys():
        if i in b1.keys():
            a2+=min(a1[i],b1[i])
    return a2