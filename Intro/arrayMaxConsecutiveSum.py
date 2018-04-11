'''
Given array of integers, find the maximal possible sum of some of its k consecutive elements.
'''
def arrayMaxConsecutiveSum(inputArray, k):
    a=len(inputArray)
    s = sum(inputArray[0:k])
    m=s
    for i in range(k,a):
        s=s+inputArray[i]-inputArray[i-k]
        if s>m:
            m=s
    return m