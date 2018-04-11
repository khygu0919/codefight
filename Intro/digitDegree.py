'''
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.
'''
def digitDegree(n):
	a=str(n)
	b=[]
	c=0
	if len(a)==1:
		return 0
	else:
		for i in a:
			b.append(str(i))
	while len(a)>1:
		d=0
		for j in b:
			d+=int(j)
		a=str(d)
		b=[]
		for k in a:
			b.append(k)
		c+=1
	return c