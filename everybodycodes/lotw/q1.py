from math import sqrt, ceil

from input_data import q1_p1, q1_p2, q1_p3
from myutils import apply_then_combine

def parse_outputsts(input) -> list[int]:
    return [int(o) for o in input.split(",")]

def next_square(i: int) -> int:
    """Returns the lowest square number greater than or equal to i."""
    return ceil(sqrt(i)) ** 2

def next_hollow_fort(i:int) -> int:
    """Returns the lowest number of pinecones needed to produce an
    empty square fort perimeter as described in part 2, which has
    at least i pinecones in it."""
    if i < 8: # 3x3 with hollow center
        return 8
    # closed form for hollow perimeter
    return ceil(i / 4) * 4

def next_oneempty_fort(i: int) -> int:
    """Returns the lowest number of pinecones needed to produce a
    square fort with exactly one empty cell in the center as described
    in part 3, which has at least i pinecones in it."""
    if i < 8: # 3x3 with hollow center
        return 8
    if next_square(i) % 2 == 0: # fort length must be odd
        return next_square(next_square(i)+1) - 1
    elif i == next_square(i): # if would be a full square, go next legitimate size up
        return int((sqrt(i)+2) ** 2 - 1)
    return next_square(i) - 1


if __name__ == '__main__':
    print(f"Part 1 answer: {apply_then_combine(
        parse_outputsts(q1_p1), 
        lambda o: next_square(o) - o)}"
    )
    print(f"Part 2 answer: {apply_then_combine(
        parse_outputsts(q1_p2), 
        lambda o: next_hollow_fort(o) - o)}"
    )
    print(f"Part 3 answer: {apply_then_combine(
        parse_outputsts(q1_p3), 
        lambda o: next_oneempty_fort(o) - o)}"
    )