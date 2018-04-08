'''
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.
'''
def avoidObstacles(inputArray):
    for i in range(2,max(inputArray)+2):
        a=0
        for j in inputArray:
            if j%i !=0:
                a+=1
        if a==len(inputArray):
            return i
            break