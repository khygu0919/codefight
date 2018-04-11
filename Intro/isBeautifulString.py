'''
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.
'''
def isBeautifulString(inputString):
	a=sorted(list(set(sorted(inputString))))
	inputString=''.join(sorted(inputString))
	b=[]
	c=ord(a[-1])-96
	if len(a)!=c:
		return False
	for i in a:
		b.append(inputString.count(i))
	if b==sorted(b,reverse=True):
		return True
	else: return False