import Bishop
import King
import Knight
import Pawn
import Queen
import Rook


class Board:
    def __init__(self):
        self.gameboard =  [[0] * 8 for i in range(8)]
        self.blackKing = 0
        self.whiteKing = 0
        self.whitePiecesList = []
        self.blackPiecesList = []
        self.capturedByWhite = []
        self.capturedByBlack = []
        setPawns(self.whitePiecesList,self.gameboard,1,"WHITE")
        setMajorPieces(self.whitePiecesList,self.gameboard,0,"WHITE",self.whiteKing)
        setPawns(self.blackPiecesList,self.gameboard,6,"BLACK")
        setMajorPieces(self.blackPiecesList,self.gameboard,7,"BLACK",self.blackKing)
    
    def getPiece(self,row,col):
        return self.gameboard[row][col]
    
    def isPieceInWay(self,piece,row,col):
        if row == piece.row:
            x = 0
        elif row>piece.row:
            x = -1
        else:
            x = 1
        if col == piece.col:
            y = 0
        elif col>piece.col:
            y = -1
        else:
            y = 1
        
        if x != 0:
            c = col
            for r in range(row,piece.row,x):
                if self.gameboard[r][c] != 0:
                    return True
                c += y
            return False
        
        elif y!=0:
            r = row
            for c in range(col,piece.col,y):
                if self.gameboard[r][c] != 0:
                    return True
                r += x
            return False
        else:
            return False
                
    
    def movePiece(self,piece,row,col):
        if piece == 0:
            return False
        
        if not self.isPieceInWay(piece,row,col) or piece.__str__() == "k":
            if piece.move(row,col):
                self.gameboard[row][col] = piece
                self.gameboard[piece.row][piece.col] = 0
                piece.row = row
                piece.col = col
                return True
            else:
                return False
        else:
            print("Piece in way!")
            return False
        
    def capturePiece(self,piece,row,col):
        print("enter capture piece")
        if row-piece.row >0:
            deltaX=-1
        elif row-piece.row <0:
            deltaX = 1
        else:
            deltaX = 0
        if col - piece.col >0:
            deltaY=-1
        elif col-piece.col <0:
            deltaY = 1
        else:
            deltaY = 0
            
        if self.gameboard[row][col] != 0 and (not self.isPieceInWay(piece,row + deltaX,col + deltaY) or piece.__str__() == "k"):
            if piece.color == "WHITE":
                if self.gameboard[row][col].color == "BLACK":
                    print("seems good")
                    if piece.capture(row,col):
                        self.capturedByWhite.append(self.gameboard[row][col])
                        self.blackPiecesList.remove(self.gameboard[row][col])
                        self.gameboard[row][col] = 0
                        self.gameboard[row][col] = piece
                        self.gameboard[piece.row][piece.col] = 0
                        piece.row = row
                        piece.col = col
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                if self.gameboard[row][col].color == "WHITE":
                    if piece.capture(row,col):
                        self.capturedByBlack.append(self.gameboard[row][col])
                        self.whitePiecesList.remove(self.gameboard[row][col])
                        self.gameboard[row][col] = 0
                        self.gameboard[row][col] = piece
                        self.gameboard[piece.row][piece.col] = 0
                        piece.row = row
                        piece.col = col
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False
    


def setPawns(lst,gameboard, row,color):
    for col in range(8):
        pawn = Pawn.Pawn(row,col,color)
        lst.append(pawn)
        gameboard[row][col] = pawn
        
def setMajorPieces(lst,gameboard,row,color,kng):
    rook = Rook.Rook(row,0,color)
    lst.append(rook)
    gameboard[row][0] = rook
    
    knight = Knight.Knight(row,1,color)
    lst.append(knight)
    gameboard[row][1] = knight
    
    bishop = Bishop.Bishop(row,2,color)
    lst.append(bishop)
    gameboard[row][2] = bishop
    
    queen = Queen.Queen(row,3,color)
    lst.append(queen)
    gameboard[row][3] = queen
    
    king = King.King(row,4,color)
    lst.append(king)
    kng = king
    gameboard[row][4] = king
    
    bishop = Bishop.Bishop(row,5,color)
    lst.append(bishop)
    gameboard[row][5] = bishop
    
    knight = Knight.Knight(row,6,color)
    lst.append(knight)
    gameboard[row][6] = knight
    
    rook = Rook.Rook(row,7,color)
    lst.append(rook)
    gameboard[row][7] = rook
