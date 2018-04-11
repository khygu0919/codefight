'''
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. 
'''
def bishopAndPawn(bishop, pawn):
	b=[ord(bishop[0]),int(bishop[1])]
	p=[ord(pawn[0]),int(panw[1])]
	return b[1]-b[0]==p[1]-p[0] or sum(b)==sum(p)
print bishopAndPawn('e3','h3')
'''
a b c d e f g h
1 2 3 4 5 6 7 8

4,4
1,1 2,2 3,3 5,5 6,6 7,7 8,8
1,7 2,6 3,5 5,3 6,2 7,1
5,3 6,4
3,1 4,2 6,4 7,5 8,6
1,7 2,6 3,5 4,4 6,2 7,1
'''