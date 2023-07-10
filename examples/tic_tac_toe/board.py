from tic_tac_toe.piece_type import PieceType

class TicTacToeBoard:

    def __init__(self, size: int, pieces: list[list[PieceType]]) -> None:
        self.size = size
        self.pieces = pieces

    
    def add_piece(self, row: int, col: int, piece: PieceType) -> bool:
        if(self.pieces[row][col] is not None):
            return False
        else:
            self.pieces[row][col] = piece
            return True

    # Create an empty board
    @staticmethod
    def initialize_empty(n_rows: int, n_cols: int) -> list[list[PieceType]]:
        board = [[None] * n_rows] * n_cols
        return board
    
    def print_board(self,) -> None:
        for i in range(self.size):
            for j in range(self.size):
                print(self.pieces[i][j], sep='\t', end='')
            print()

