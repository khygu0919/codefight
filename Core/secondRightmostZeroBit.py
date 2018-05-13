'''
Presented with the integer n, find the 0-based position of the second rightmost zero bit in its binary representation
(it is guaranteed that such a bit exists), counting from right to left.

Return the value of 2(position_of_the_found_bit).
'''

def secondRightmostZeroBit(n):
    return 2**('{0:b}'.format(n)[::-1].find('0','{0:b}'.format(n)[::-1].find('0')+1))