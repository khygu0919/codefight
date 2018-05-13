'''
A little boy is studying arithmetics.
He has just learned how to add two integers, written one below another, column by column.
But he always forgets about the important part - carrying.

Given two integers, find the result which the little boy will get.

Example
For param1 = 456 and param2 = 1734, the output should be
additionWithoutCarrying(param1, param2) = 1180.
'''
def additionWithoutCarrying(param1, param2):
    a=''
    b=max(len(str(param1)),len(str(param2)))
    param1,param2=str(param1).zfill(b),str(param2).zfill(b)
    for i in range(len(param1),0,-1):
        a+=str(int(param1[-i])+int(param2[-i]))[-1]
    return int(a)