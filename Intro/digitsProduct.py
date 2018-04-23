'''
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.
'''
import math
def getDivisor(product):
    for i in range(9,1,-1):
        if product%i==0:
            return product//i,i

def digitsProduct(product):
    c=[]
    a=0
    if product==1:
        return 1
    if product==0:
        return 10
    if product==5 or product==7:
        return product
    for i in range(int(math.sqrt(product)),1,-1):
        if product%i==0:
            break
        if product%i!=0 and i==2:
            return -1
    while 1:
        if product==1:
            break
        try:
            a=getDivisor(product)[1]
            product=getDivisor(product)[0]
            c.append(a)
        except:
        	return -1
    return int(''.join(str(x) for x in sorted(c)))