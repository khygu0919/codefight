'''
Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that after the rearrangement the strings at consecutive positions would differ by exactly one character.
'''
import itertools
def stringsRearrangement(inputArray):
    a=len(inputArray[0])
    b=len(inputArray)
    c=[]
    d=[]
    permutate = itertools.permutations(inputArray)
    for p in permutate:
        for i in range(1,b):
            e=0
            for j in range(a):
                if p[i][j]!=p[i-1][j]:
                    e+=1
            c.append(e)
        if c.count(1)==b-1:
            return True
            break
        c=[]
    return False