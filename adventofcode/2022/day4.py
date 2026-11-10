import re

from aocd import get_data

from myutils import apply_then_combine

input = [re.split(r"-|,", i) for i in get_data(day=4, year=2022).split("\n")]
input = [[int(i) for i in j] for j in input]


def satisfies_p1(assignment):
    lb1, ub1, lb2, ub2 = assignment
    return (lb1 <= lb2 and ub1 >= ub2) or (lb2 <= lb1 and ub2 >= ub1)


def satisfies_p2(assignment):
    lb1, ub1, lb2, ub2 = assignment
    return (ub1 >= lb2) and (ub2 >= lb1)


print(f"Part 1 answer: {apply_then_combine(input, satisfies_p1)}")
print(f"Part 2 answer: {apply_then_combine(input, satisfies_p2)}")
