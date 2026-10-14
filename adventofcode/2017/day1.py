from aocd import get_data

input = get_data(day=1, year=2017)


def sum_matching_digits(ahead: int = 1):
    """
    Go through a list and sum up all the numbers that match the digit a
    user-specified number of places ahead. Treats list as circular.
    """
    summed_matchers = 0
    for i, digit in enumerate(input):
        if digit == input[(i + ahead) % len(input)]:
            summed_matchers += int(digit)

    return summed_matchers


if __name__ == "__main__":
    print(f"Part 1 answer: {sum_matching_digits(1)}")
    print(f"Part 2 answer: {sum_matching_digits(len(input) // 2)}")
