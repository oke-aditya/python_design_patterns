from tic_tac_toe.piece_type import PieceType


class Player:
    def __init__(self, name: str, piece_type: PieceType) -> None:
        self.name = name
        self.piece_type = piece_type

    def __str__(self) -> str:
        print(f"Player name {self.name} and Piece Type {self.piece_type}")
