'''
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.
'''
import re
def variableName(name):
    name=name.replace("&quot;","")
    p=re.compile('[a-zA-Z\_]')
    if p.match(name):
        name=name[1:]
        a=re.sub('[0-9a-zA-Z\_]','',name)
        if a:return False
    else:return False
    return True