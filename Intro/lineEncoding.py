'''
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
'''
def lineEncoding(s):
    a=[]
    b=[]
    c=0
    for i in range(len(s)):
        if i==0:
            a.append(s[i])
            c+=1
        elif s[i]!=s[i-1]:
            a.append(s[i])
            b.append(c)
            c=1
            if i==len(s)-1:
                b.append(c)
        else:
            c+=1
            if i==len(s)-1:
                b.append(c)
    c=''
    for i in range(len(a)):
        if b[i]!=1:
            c+=str(b[i])
            c+=a[i]
        else:
            c+=a[i]
    return c