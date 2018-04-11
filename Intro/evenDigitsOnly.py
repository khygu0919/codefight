'''
Check if all digits of the given integer are even.
'''
def evenDigitsOnly(n):
    for i in str(n):
        if int(i)%2==0:
            pass
        else:
            return False
            break
    return True