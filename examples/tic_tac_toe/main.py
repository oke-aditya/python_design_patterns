# Here we play the game
from tic_tac_toe.board import TicTacToeBoard

if __name__ == "__main__":
    board = TicTacToeBoard.initialize_empty(3, 3)
    board = TicTacToeBoard(3, pieces=board)
    print(board)
