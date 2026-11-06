from math import sqrt, ceil

from input_data import q1_p1, q1_p2, q1_p3

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

def solve(outposts: str, func) -> int:
    total = 0
    outposts = [int(i) for i in outposts.split(",")]
    for o in outposts:
        total += func(o) - o
    return total

if __name__ == '__main__':
    print(f"Part 1 answer: {solve(q1_p1, next_square)}")
    print(f"Part 2 answer: {solve(q1_p2, next_hollow_fort)}")
    print(f"Part 3 answer: {solve(q1_p3, next_oneempty_fort)}")