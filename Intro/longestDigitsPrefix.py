'''
Given a string, output its longest prefix which contains only digits.
'''
def longestDigitsPrefix(inputString):
    a=''
    b=[]
    for i in inputString:
    	try:
    		if int(i)==0 or int(i):
    			b.append(i)
    	except:
    		break
    a= ''.join(b)
    return a