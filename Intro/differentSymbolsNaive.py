'''
Given a string, find the number of different characters in it
'''
def differentSymbolsNaive(s):
    s.replace('&quot;','')
    a=[]
    for i in s:
        a.append(i)
    a=list(set(a))
    return len(a)