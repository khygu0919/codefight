'''
Given array of integers, remove each kth element from it.
'''
def extractEachKth(inputArray, k):
    a=len(inputArray)//k
    b=[]
    for i in range(1,a+1):
        b.append(k*i-1)
    inputArray=[v for i, v in enumerate(inputArray) if i not in b]
    return inputArray