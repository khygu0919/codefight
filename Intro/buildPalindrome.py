'''
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.
'''
def buildPalindrome(st):
	a=len(st)
	for i in range(a):
		b=st[i:a]
		if isPalindrome(b):
			c=st[0:i]
			return st+c[::-1]
def isPalindrome(st):
	return st == st[::-1]