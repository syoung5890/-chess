import Board

class Game:
    def __init__(self):
        self.board = Board.Board()
        self.turn = "WHITE"
        self.selectedPiece = 0
        
    def selectSquare(self,row,col):
        if self.board.gameboard[row][col] == 0:
            return False
        elif self.board.gameboard[row][col].color == self.turn:
            print(self.board.gameboard[row][col])
            self.selectedPiece = self.board.gameboard[row][col]
            return True
        else:
            return False
        
    def targetSquare(self,row,col):
        print("enter target")
        print(self.selectedPiece)
        if self.board.movePiece(self.selectedPiece,row,col):
            print(self.board.gameboard[row][col])
            if self.turn == "WHITE":
                self.turn = "BLACK"
            else:
                self.turn = "WHITE"
            return True
        elif self.board.capturePiece(self.selectedPiece,row,col):
            print("heya")
            if self.turn == "WHITE":
                self.turn = "BLACK"
            else:
                self.turn = "WHITE"
            return True
        else:
            return False
    
    def kingInCheck(color):
        if color == "WHITE":
            #LOOP THROUGH BLACK PIECES AND CHECK IF ANY PIECES CAN ATTACK WHITE KING
            for x in self.board.blackPieces:
                if x.capture(self.board.whiteKing.row,self.board.whiteKing.col):
                    return True
            return False
        else:
            #LOOP THROUGH WHITE PIECES AND CHECK IF ANY PIECES CAN ATTACK BLACK KING
            for x in self.board.whitePieces:
                if x.capture(self.board.blackKing.row,self.board.blackKing.col):
                    return True
            return False
    
    def kingInCheckMate(color):
        pass
        
        