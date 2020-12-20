import Piece

class Bishop(Piece.Piece):
    def __init__(self,row,col,color):
        super().__init__(row,col,color)
    
    def __str__(self):
        return "B"
    
    def move(self,row,col):
        if (abs(row-self.row) == abs(col-self.col)):
            return True
        else:
            return False
        
    def capture(self,row,col):
        if(abs(row-self.row)==abs(col-self.col)):
            return True
        else:
            return False