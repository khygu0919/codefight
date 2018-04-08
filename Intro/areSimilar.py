'''
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.
'''
def areSimilar(a, b):
    c=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            c-=1
    a.sort()
    b.sort()
    for j in range(len(a)):
        if a[j]!=b[j]:
            return False
            break
    if c<-2:
        return False
    else:return True