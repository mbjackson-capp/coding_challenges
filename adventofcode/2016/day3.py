import re

from aocd import get_data

from myutils import apply_then_combine

input = [
    [int(num) for num in re.findall(r"\d+", line)]
    for line in get_data(day=3, year=2016).split("\n")
]


def meets_triangle_inequality(a: int, b: int, c: int):
    return a < (b + c)


def is_valid_triangle(trio: list[str]) -> bool:
    a, b, c = trio
    return (
        meets_triangle_inequality(a, b, c)
        and meets_triangle_inequality(b, c, a)
        and meets_triangle_inequality(c, a, b)        
    )


def make_vertical(processed_input):
    reordered = (
        [i[0] for i in processed_input]
        + [i[1] for i in processed_input]
        + [i[2] for i in processed_input]
    )
    trying_this = [
        # TODO: make more pythonic with itertools
        [reordered[i], reordered[i + 1], reordered[i + 2]]
        for i in range(0, len(reordered), 3)
    ]
    return trying_this


if __name__ == "__main__":
    print(f"Part 1 solution: {apply_then_combine(input, is_valid_triangle)}")
    print(f"Part 2 solution: {apply_then_combine(make_vertical(input), is_valid_triangle)}")
