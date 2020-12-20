import Board

#USE LOGIC AS PRINT BOARD FUNCTION LATER
def printBoard():  
    for i in range(8):
        for j in range(8):
            print(board.gameboard[i][j], end = " ")
        print()
    print()

board = Board.Board()
printBoard()
board.movePiece(board.gameboard[1][3],3,3)
printBoard()
board.movePiece(board.gameboard[0][4],1,3)
printBoard()
board.movePiece(board.gameboard[1][3],2,4)
printBoard()
board.movePiece(board.gameboard[0][3],2,3)
printBoard()
board.movePiece(board.gameboard[2][3],4,5)
printBoard()
board.movePiece(board.gameboard[2][4],3,4)
printBoard()
board.movePiece(board.gameboard[0][2],3,5)
printBoard()
board.movePiece(board.gameboard[3][5],2,5)
printBoard()
board.movePiece(board.gameboard[3][5],0,2)
printBoard()
