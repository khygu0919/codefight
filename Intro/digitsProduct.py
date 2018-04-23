'''
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.
'''
def getDivisor(product):
    for i in range(9,1,-1):
        if product%i==0:
            return product//i,i
def digitsProduct(product):
    c=[]
    a=0
    while 1:
        if product==1:
            break
        a=getDivisor(product)[1]
        product=getDivisor(product)[0]
        c.append(a)
    return ''.join(str(x) for x in sorted(c))