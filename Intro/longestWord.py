'''
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.
'''
import re
def longestWord(text):
    p=re.compile('[a-zA-Z]{1,}')
    a=p.findall(text)
    return max(a,key=len)