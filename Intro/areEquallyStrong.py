'''
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
'''
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    a=[yourLeft, yourRight, friendsLeft, friendsRight]
    if max(a[0],a[1]) == max(a[2],a[3]):
        if min(a[0],a[1]) == min(a[2],a[3]):
            return True
        else: return False
    else: return False