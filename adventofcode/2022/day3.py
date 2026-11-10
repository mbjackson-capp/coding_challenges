import re

from aocd import get_data

from myutils import apply_then_combine

input = get_data(day=3, year=2022).split("\n")


def priority(char):
    if re.match(r"[a-z]", char):
        return ord(char) - ord("a") + 1  # range 1 through 26 for a-z
    elif re.match(r"[A-Z]", char):
        return ord(char) - ord("A") + 27  # range 27 through 52 for A-Z


def shared_item_priority(rucksack):
    halfway = len(rucksack) // 2
    left = set(rucksack[0:halfway])
    right = set(rucksack[halfway:])
    shared_item = next(iter(set.intersection(left, right)))  # extract letter  
    return priority(shared_item)  


def part2():
    badge_sum = 0
    GROUP_SIZE = 3
    curr_group = []
    for i, elf in enumerate(input):
        if i % GROUP_SIZE == 0 and i != 0:
            badge_sum += priority(badge(curr_group))
            curr_group = []
        curr_group.append(elf)
    # count last group, which otherwise wouldn't close
    badge_sum += priority(badge(curr_group))
    return badge_sum


def badge(group):
    knapsacks = [set(elf) for elf in group]
    return next(iter(set.intersection(*knapsacks)))  # extract shared letter


if __name__ == "__main__":
    print(f"Part 1 answer: {apply_then_combine(input, shared_item_priority)}")
    print(f"Part 2 answer: {part2()}")
