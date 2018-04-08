'''
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
'''
def arrayMaximalAdjacentDifference(inputArray):
    b=[]
    c=[]
    for i in range(1,len(inputArray)):
        b.append(inputArray[i]-inputArray[i-1])
    for i in range(0,len(inputArray)-1):
        b.append(inputArray[i]-inputArray[i+1])
    for i in b:
        c.append(abs(i))
    return max(c)  