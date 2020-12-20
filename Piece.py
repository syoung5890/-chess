class Piece:
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        
    def setPos(self,row, col):
        self.row = row
        self.col = col