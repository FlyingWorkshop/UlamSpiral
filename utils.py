from enum import Enum
from tqdm import tqdm
from sympy import isprime
import numpy as np


class Moving(Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3


INCREMENTS = {
    Moving.RIGHT: (1, 0),
    Moving.UP: (0, 1),
    Moving.LEFT: (-1, 0),
    Moving.DOWN: (0, -1)
}

COUNTERCLOCKWISE_TURN = {
    Moving.RIGHT: Moving.UP,
    Moving.UP: Moving.LEFT,
    Moving.LEFT: Moving.DOWN,
    Moving.DOWN: Moving.RIGHT
}

def get_ulam_spiral_coords(n: int):
    gen = square_spiral_range(n)
    xv = []
    yv = []
    for i in tqdm(np.arange(n)):
        x, y = next(gen)
        if isprime(i):
            xv.append(x)
            yv.append(y)
    return np.array(xv, dtype=int), np.array(yv, dtype=int)

def is_even(n: int) -> bool:
    return n % 2 == 0

def square_spiral_range(n: int):
    x, y = 0, 0
    direction = Moving.RIGHT
    num_turns = 0
    side_len = 1
    side_pos = 0
    for i in range(n):
        # decide whether to turn (i.e. change directions)
        if side_pos == side_len:
            # do turn
            direction = COUNTERCLOCKWISE_TURN[direction]
            side_pos = 0
            num_turns += 1

            # increase side_len every other turn
            if is_even(num_turns):
                side_len += 1

        # increment side_pos and coords
        x_step, y_step = INCREMENTS[direction]
        x += x_step
        y += y_step
        side_pos += 1
        yield x, y
