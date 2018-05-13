'''
You are given two numbers a and b where 0<=a<=b.
Imagine you construct an array of all the integers from a to b inclusive.
You need to count the number of 1s in the binary representations of all the numbers in the array.

Example

For a = 2 and b = 7, the output should be
rangeBitCount(a, b) = 11.

Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7].
Converting the numbers to binary, we get [10, 11, 100, 101, 110, 111], which contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.
'''
def rangeBitCount(a, b):
    c=[x for x in range(a,b+1)]
    for x in range(1,len(c)):
        a=a<<len('{0:b}'.format(c[x]))
        a+=c[x]
    b=0
    for x in '{0:b}'.format(a):
        b+=int(x)
    return b