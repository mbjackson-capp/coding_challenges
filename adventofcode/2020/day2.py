import re

from aocd import get_data

from myutils import apply_then_combine

input = get_data(day=2, year=2020).split("\n")
input = [re.split(r"-|:?\s", row) for row in input]

def is_valid_p1(row) -> bool:
    first_num, second_num, letter, passwd = row
    occurrences = len(re.findall(letter, passwd))
    return (occurrences >= int(first_num)) and (occurrences <= int(second_num))

def is_valid_p2(row) -> bool:
    first_num, second_num, letter, passwd = row
    # use bitwise xor on output of two boolean statements
    return (passwd[int(first_num) - 1] == letter) ^ (passwd[int(second_num) - 1] == letter)


if __name__ == "__main__":
    print(f"Solution to part 1: {apply_then_combine(input, is_valid_p1)}")
    print(f"Solution to part 1: {apply_then_combine(input, is_valid_p2)}")
