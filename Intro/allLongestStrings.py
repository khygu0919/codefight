'''
Given an array of strings, return another array containing all of its longest strings.
'''
def allLongestStrings(inputArray):
    b=[]
    c=0
    for i in inputArray:
        b.append(len(i))
    c=max(b)
    b=[]
    for j in inputArray:
        if len(j)==c:
            b.append(j)
    return b
    