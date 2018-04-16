'''
Determine if the given character is a digit or not.
'''
def isDigit(symbol):
    try:
        if int(symbol)==0 or int(symbol):
            return True
    except:
        return False