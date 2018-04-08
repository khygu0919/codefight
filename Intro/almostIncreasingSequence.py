'''
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
'''
def almostIncreasingSequence(sequence):
    b=0
    c=0
    for i in range(0,len(sequence)-1):
        if c>0:
            c-=1
            pass
        #print 'int',i, b
        if sequence[i+1]>sequence[i]:
            pass
        else:
            b+=1
            if i+2>len(sequence)-1:
                break
            elif i==0:
                c+=1
                pass
            elif sequence[i+1]<=sequence[i-1] and sequence[i+2]<=sequence[i]:
                return False
                break
    return b<=1