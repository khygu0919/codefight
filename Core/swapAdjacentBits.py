'''
You're given an arbitrary 32-bit integer n.
Take its binary representation, split bits into it in pairs and swap bits in each pair.
Then return the result as a decimal number.
Example

For n = 13, the output should be
swapAdjacentBits(n) = 14.

13 = 11012 ~> {11}{01} ~> 1110 = 1410.

For n = 74, the output should be
swapAdjacentBits(n) = 133.

74 = 010010102 ~> {01}{00}{10}{10} ~> 10000101 = 13310.
'''
def swapAdjacentBits(n):
    return int(''.join(['{0:b}'.format(n).zfill(32)[2*x:2*x+2][::-1] for x in range(16)]),2)