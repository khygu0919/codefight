'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
'''
def sortByHeight(a):
    b=[]
    c=[]
    for i in range(0,len(a)):
        if a[i]==-1:
            b.append(i)
        else:
            c.append(a[i])
    c.sort()
    for j in b:
        c.insert(j,-1)
    return c