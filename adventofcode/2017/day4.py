from collections import Counter

from aocd import get_data

input = get_data(day=4, year=2017)


def parse_input(data: str) -> list[list[str]]:
    rows = data.split("\n")
    return [row.split(" ") for row in rows]


def is_all_unique(row: list[str]) -> bool:
    return len(row) == len(set(row))


def has_no_anagrams(row: list[str]) -> bool:
    ctrs_seen = []
    for word in row:
        ctr = Counter(word)
        if ctr in ctrs_seen:
            return False
        ctrs_seen.append(ctr)
    return True


def is_valid(row: list[str], part: int = 1) -> bool:
    return (is_all_unique(row) and has_no_anagrams(row)) if part == 2 else is_all_unique(row)


def part1(data: str, part: int = 1) -> int:
    rows = parse_input(data)
    valid_count = 0
    for row in rows:
        if is_valid(row, part=part):
            valid_count += 1
    return valid_count


if __name__ == "__main__":
    print(f"Part 1 answer: {part1(input)}")
    print(f"Part 2 answer: {part1(input, part=2)}")
