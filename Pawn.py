import Piece

class Pawn(Piece.Piece):
    def __init__(self,row,col,color):
        self.numOfMoves = 0
        super().__init__(row,col,color)
        
    def __str__(self):
        return "P"
        
    def move(self,row,col): # MUST CHECK BOARD TO MAKE SURE SPACE IS AVAILLABLE BEFORE CALLING FUNCTION
        if col == self.col: # THIS FUNCTION JUST CHECKS IF MOVE IS LEGAL MOVE FOR THE PIECE
            if abs(row -self.row) == 2:   # IT DOES NOT MAKE THE MOVE OR CHECK IF MOVE IS ILLEGAL BECAUSE OF OTHER PIECES INTERFERING
                if self.numOfMoves == 0:
                    self.numOfMoves+=1
                    return True 
                else:
                    return False
            elif abs(row-self.row) == 1:
                self.numOfMoves+=1
                return True
            else:
                return False
        else:
            return False
            
                   
    def capture(self,row,col):
        if abs(col - self.col) == 1 and abs(row-self.row) == 1:
            self.numOfMoves+=1
            return True
            