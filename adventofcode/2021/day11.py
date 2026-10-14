import numpy as np
from aocd import get_data

from myutils import gridify, neighbor_locs

FLASH = -1


def step0_octopi():
    """Since step modifies an ndarray in-place, call part1 and part2 with this
    as its argument to start from step 0 / input state"""
    input = gridify(get_data(day=11, year=2021), intify=True)
    return input


def step(octopi):
    flashes_this_step = 0
    octopi += 1
    while octopi[octopi > 9].size > 0:
        flash_status_now = (octopi > 9).copy()
        octopi[octopi > 9] = FLASH
        for index, flashed in np.ndenumerate(flash_status_now):
            if flashed:
                x, y = index
                neighbors = neighbor_locs(octopi, x, y, include_diag=True)
                for loc in neighbors:
                    this_x, this_y = loc
                    if octopi[this_x][this_y] >= 0:
                        octopi[this_x][this_y] += 1
    flashes_this_step += len(octopi[octopi == FLASH])
    octopi[octopi == -1] = 0
    return flashes_this_step


def part1(input):
    total_flashes = 0
    for i in range(100):
        total_flashes += step(input)
    return total_flashes


def part2(input):
    step_count = 0
    while True:
        step_count += 1
        if step(input) == 100:
            return step_count


if __name__ == "__main__":
    print(f"Part 1 answer: {part1(step0_octopi())}")
    print(f"Part 2 answer: {part2(step0_octopi())}")
