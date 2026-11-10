import re

from aocd import get_data

from myutils import apply_then_combine


def has_three_vowels(str) -> bool:
    vowels = [char for char in str if char in ["a", "e", "i", "o", "u"]]
    return len(vowels) >= 3


def has_double_letter(str) -> bool:
    double_letters = re.findall(r"(.)\1", str)
    return bool(double_letters)


def contains_forbidden_substring(str) -> bool:
    forbidden = re.findall(r"(ab|cd|pq|xy)", str)
    return bool(forbidden)


def has_repeated_2gram(str) -> bool:
    digram = re.findall(r"(\w{2}).*(\1)", str)
    return bool(digram)


def has_aba_pattern(str) -> bool:
    aba_pattern = re.findall(r"(\w)(\w)(\1)", str)
    return bool(aba_pattern)


def is_nice(str, part=1) -> bool:
    if part == 1:
        return (
            has_three_vowels(str)
            and has_double_letter(str)
            and (not contains_forbidden_substring(str))
        )
    elif part == 2:
        return has_repeated_2gram(str) and has_aba_pattern(str)

if __name__ == '__main__':
    input = get_data(day=5, year=2015).split("\n")
    print(f"Part 1 solution: {apply_then_combine(input, lambda x: is_nice(x, part=1))}")
    print(f"Part 1 solution: {apply_then_combine(input, lambda x: is_nice(x, part=2))}")
