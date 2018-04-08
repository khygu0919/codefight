'''
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
'''
def arrayChange(inputArray):
    b=0
    c=0
    for i in range(1,len(inputArray)):
        if inputArray[i]> inputArray[i-1]:
            pass
        else:
            b=inputArray[i-1]-inputArray[i]+1
            c+=b
            inputArray[i]+=b
    return c