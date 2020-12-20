import Piece

class Queen(Piece.Piece):
    def __init__(self,row,col,color):
        super().__init__(row,col,color)
        
    def __str__(self):
        return "Q"
    
    def move(self,row,col):
        if (abs(row-self.row) == abs(col-self.col)) or (row == self.row)  or (col == self.col):
            return True
        else:
            return False
        
    def capture(self,row,col):
        if (abs(row-self.row) == abs(col-self.col)) or (row == self.row)  or (col == self.col):
            return True
        else:
            return False