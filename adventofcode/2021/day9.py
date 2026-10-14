import numpy as np
from aocd import get_data

from myutils import gridify, neighbor_locs, neighbors

seafloor = gridify(get_data(day=9, year=2021), intify=True)


def get_low_points(seafloor):
    low_points = []
    for x in range(len(seafloor)):
        for y in range(len(seafloor)):
            if seafloor[x][y] < min(neighbors(seafloor, x, y)):
                low_points.append((x, y))
    return low_points


def part1(seafloor):
    risk_score = 0
    low_points = get_low_points(seafloor)
    for point in low_points:
        x, y = point
        risk_score += 1 + seafloor[x][y]
    return risk_score


def basin_size(point, seafloor):
    """Basic recursive flood fill algorithm, using -1 to indicate filled.
    Input point is a (x, y) tuple for current coordinate on seafloor"""
    curr_x, curr_y = point
    if seafloor[curr_x][curr_y] in (9, -1):
        return 0
    else:
        seafloor[curr_x][curr_y] = -1
        return 1 + sum(
            [basin_size(pt, seafloor) for pt in neighbor_locs(seafloor, curr_x, curr_y)]
        )


def part2(seafloor):
    low_points = get_low_points(seafloor)
    basin_sizes = [basin_size(point, seafloor) for point in low_points]
    basin_sizes.sort(reverse=True)
    return np.prod(basin_sizes[0:3])


if __name__ == "__main__":
    print(f"Part 1 answer: {part1(seafloor)}")
    print(f"Part 2 answer: {part2(seafloor)}")
