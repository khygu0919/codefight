'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
'''
def addBorder(picture):
    b=len(picture[0])
    c='*'*(b+2)
    for i in range(len(picture)):
        picture[i]='*'+picture[i]+'*'
    picture.append(c)
    picture.insert(0,c)
    return picture