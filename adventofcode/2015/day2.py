from aocd import get_data

from myutils import apply_then_combine


def wrapping_paper(box):
    l, w, h = box
    sides = [l * w, w * h, l * h]
    wrapping_paper = sum([2 * side for side in sides]) + min(sides)
    return wrapping_paper


def ribbon(box):
    l, w, h = box
    perimeters = [2 * (l + w), 2 * (w + h), 2 * (l + h)]
    box_ribbon = min(perimeters)
    bow = l * w * h
    return box_ribbon + bow


if __name__ == '__main__':
    input = [i.split("x") for i in get_data(day=2, year=2015).split("\n")]
    input = [[int(i) for i in box] for box in input]
    print(f"Part 1 solution: {apply_then_combine(input, wrapping_paper)}")
    print(f"Part 2 solution: {apply_then_combine(input, ribbon)}")
