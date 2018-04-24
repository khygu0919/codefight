'''
You are given an array of desired filenames in the order of their creation.

Since two files cannot have equal names,
the one which comes later will have an addition to its name in a form of (k),
where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].
'''
def fileNaming(names):
    a=[names[0]]
    for i in range(1,len(names)):
        if names[i] in names[0:i] or names[i] in a[0:i]:
            b=names[0:i].count(names[i])
            c=a[0:i].count(names[i])
            d=max(b,c)
            buf=names[i]+"("+str(d)+")"
            while buf in a[0:i]:
                d+=1
                buf=names[i]+"("+str(d)+")"
            a.append(buf)
        else:
        	a.append(names[i])
    return a