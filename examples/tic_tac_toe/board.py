from tic_tac_toe.piece_type import PieceType
from typing import Optional

class TicTacToeBoard:

    def __init__(self, size: int, pieces: Optional[list[list[PieceType]]] = None) -> None:
        self.size = size
        if pieces is None:
            self.pieces = self._initialize_empty()
        else:
            self.pieces = pieces

    
    def add_piece(self, row: int, col: int, piece: PieceType) -> bool:
        if(self.pieces[row][col]):
            return False
        else:
            self.pieces[row][col] = piece
            return True

    # Create an empty board
    def _initialize_empty(self) -> list[list[PieceType]]:
        pieces = [[0] * self.size for i in range(self.size)]
        return pieces
    
    def print_board(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                print(f"{self.pieces[i][j]} ", end='')
            print()


    # Check if anyone has n in row / diagonal / column
    def _check_winner(self) -> bool:
        pass
