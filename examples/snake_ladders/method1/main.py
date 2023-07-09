from snake_ladders.method1.dice import roll_dice
from snake_ladders.method1.snake_ladder_gen import generate_snake_ladders

from collections import deque


def play_game(num_players: int, num_snakes: int, num_ladders: int):
    players = deque()

    # Players starts from 0.
    for i in range(num_players):
        players.append(0)

    snakes, ladders = generate_snake_ladders(num_snakes, num_ladders)

    print(f"Location of snakes are: {snakes}")
    print(f"Location of ladders are: {ladders}")

    win_condition = False

    player_no = 0

    while not win_condition:
        print(f"Player: {player_no} starts the turn")

        player_playing = players.popleft()
        steps = roll_dice()
        player_playing += steps

        # Check if he landed on snake / ladders
        possible_snake_subtraction = snakes.get(player_playing)

        if possible_snake_subtraction:
            print(f"Got bit by snake at: {player_playing}")
            player_playing = possible_snake_subtraction

        # Check if there is ladder
        possible_ladder_addition = ladders.get(player_playing)

        if possible_ladder_addition:
            print(f"Got a Ladder at: {player_playing}")
            player_playing = possible_ladder_addition

        print(f"Final position after turn: {player_playing}")

        player_no = player_no % num_players
        player_no += 1

        players.append(player_playing)
        if player_playing >= 100:
            win_condition = True
            print(f"Player {player_no} won with final position: {player_playing}")
            break


if __name__ == "__main__":
    play_game(num_players=2, num_snakes=3, num_ladders=3)
