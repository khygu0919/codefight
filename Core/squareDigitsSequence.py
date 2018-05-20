'''
Consider a sequence of numbers a0, a1, ..., an,
in which an element is equal to the sum of squared digits of the previous element.
The sequence ends once an element that has already been in the sequence appears again.

Given the first element a0, find the length of the sequence.
'''
def squareDigitsSequence(a0):
    a=[a0]
    while 1:
    	print a
        a0=sum(int(i)**2 for i in str(a0))
        if a0 in a:
            a.append(a0)
            return len(a)
        a.append(a0)