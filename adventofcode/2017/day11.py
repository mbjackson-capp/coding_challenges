from aocd import get_data


class Hex:
    """Implementation of one hex in a hexagonal coordinate tile system.
    Indebted to https://www.redblobgames.com/grids/hexagons/#coordinates-axial
    for axial coordinates implementation, which we rotate 30 degrees to the
    right to match problem statement."""

    def __init__(self, q, r):
        self.q = q
        self.r = r
        self.s = -q - r

        assert (
            self.q + self.r + self.s == 0
        ), f"Coordinates {self.q} + {self.r} + {self.s} == {self.q + self.r + self.s} != 0"

    def distance_from_origin(self):
        """Uses 'max' approach as discussed at https://www.redblobgames.com/grids/hexagons/#distances-cube"""
        return max(abs(self.q), abs(self.r), abs(self.s))

    def __repr__(self):
        return f"Hex({self.q}, {self.r}, {self.s})"


step_changes = {
    "n": (0, -1),
    "ne": (1, -1),
    "se": (1, 0),
    "s": (0, 1),
    "sw": (-1, 1),
    "nw": (-1, 0),
}


def make_hex_path(input: str) -> list[Hex]:
    cur_q = 0
    cur_r = 0
    steps = input.split(",")
    path = [Hex(0, 0)]
    for step in steps:
        new_q, new_r = step_changes[step]
        cur_q += new_q
        cur_r += new_r
        new_spot = Hex(cur_q, cur_r)
        path.append(new_spot)
    return path


def solve(input: str):
    path = make_hex_path(input)
    p1_ans = path[-1].distance_from_origin()
    p2_ans = 0
    for hex in path:
        if hex.distance_from_origin() > p2_ans:
            p2_ans = hex.distance_from_origin()
    return p1_ans, p2_ans


if __name__ == "__main__":
    input = get_data(year=2017, day=11)
    p1_ans, p2_ans = solve(input)
    print(f"Part 1 solution: {p1_ans}")
    print(f"Part 2 solution: {p2_ans}")
