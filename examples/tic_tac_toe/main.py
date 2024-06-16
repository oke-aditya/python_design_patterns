# Here we play the game
from tic_tac_toe.board import TicTacToeBoard
from tic_tac_toe.player import Player
from tic_tac_toe.piece_type import PieceType
from collections import deque


def play_game(size: int) -> None:
    # board = TicTacToeBoard.initialize_empty(size=3)
    board = TicTacToeBoard(size=size)
    board.print_board()

    p1 = Player(name="P1", piece_type=PieceType.X)
    p2 = Player(name="p2", piece_type=PieceType.O)

    players: deque[Player] = deque()
    players.append(p1, p2)

    winner = False

    while not winner:
        current_player = players.popleft()
        print(
            f"Current turn {current_player.name}: Piece to Play: {current_player.piece_type}"
        )

        row = int(input("Enter the row no to insert: "))
        col = int(input("Enter the col no to insert: "))

        if board.add_piece(row, col, piece=current_player.piece_type):
            print("Piece placed")
            board.print_board()

            if board._check_winner():
                print(f"Winner Winner Chicken Dinner!!! {current_player.name}")
                winner = True

            players.append(current_player)

        else:
            print("Failed to add the piece already occupied")
            board.print_board()


if __name__ == "__main__":
    play_game(size=3)
