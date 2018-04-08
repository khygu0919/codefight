'''
You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets. It is guaranteed that the parentheses in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair. The results string should not contain any parentheses.
'''
def reverseParentheses(s):
    a1=[]
    a2=[]
    for i in range(len(s)):
        if s[i]=='(':
            a1.append(i)
        elif s[i]==')':
            a2.append((a1[-1],i))
            del a1[-1]
    for b in a2:
        l, r = b
        tmp = s[l:r]
        tmp = tmp[::-1]
        s = s[:l]+tmp+s[r:]
    s=s.replace(')','')
    s=s.replace('(','')
    return s