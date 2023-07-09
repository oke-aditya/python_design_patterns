# Generate snake / ladders based on given no

import random


# We can generate it a bit smarter as well so that there are no looped snakes and ladders
def generate_snake_ladders(
    num_snakes: int, num_ladders: int
) -> tuple[dict[int, int], dict[int, int]]:
    # Start of ladder: End of ladder
    ladders = {}

    # start of snake: End of snake
    snakes = {}

    generated_correct = 0

    while generated_correct < (num_ladders + num_snakes):
        # Start of point
        n1 = random.randint(1, 99)

        # end of point
        n2 = random.randrange(1, 99)

        # start > end
        if n1 > n2:
            snakes[n1] = n2
            generated_correct += 1

        # end > start
        if n2 > n1:
            ladders[n1] = n2
            generated_correct += 1

    return snakes, ladders
