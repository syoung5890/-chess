import Piece

class King(Piece.Piece):
    def __init__(self,row,col,color):
        super().__init__(row,col,color)

    def __str__(self):
        return "K"
    
    def move(self,row,col):
        if (abs(row - self.row) <= 1 ) and (abs(col-self.col) <= 1) :
            return True
        else:
            return False
            
    def capture(self,row,col):
        if (abs(row - self.row) <= 1 ) and (abs(col-self.col) <= 1) :
            return True
        else:
            return False