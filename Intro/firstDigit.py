'''
Find the leftmost digit that occurs in a given string.
'''
def firstDigit(inputString):
    for i in inputString:
        if i=='0':
            return '0'
            break
        try:
            if int(i):
                return i
                break
        except:
            pass