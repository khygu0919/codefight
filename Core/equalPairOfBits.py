'''
You're given two integers, n and m.
Find position of the rightmost pair of equal bits in their binary representations
(it is guaranteed that such a pair exists), counting from right to left.

Return the value of 2position_of_the_found_pair (0-based).
'''
def equalPairOfBits(n, m):
    return 2**'{0:b}'.format(abs(~(n^m)))[::-1].find('1')