'''
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. 
'''
def bishopAndPawn(bishop, pawn):
	b=[ord(bishop[0]),int(bishop[1])]
	p=[ord(pawn[0]),int(panw[1])]
	return b[1]-b[0]==p[1]-p[0] or sum(b)==sum(p)