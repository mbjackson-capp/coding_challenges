from collections import Counter

from aocd import get_data


def solve() -> tuple[str, str]:
    input = get_data(year=2016, day=6).split("\n")
    msg_width = len(input[0])
    counts = {}
    for i in range(msg_width):
        counts[i] = Counter([message[i] for message in input])

    error_corrected_p1 = ""
    error_corrected_p2 = ""
    for digit_ix in sorted(counts.keys()):
        ctr = counts[digit_ix]
        most_common = {k for k, v in ctr.items() if v == max(ctr.values())}
        least_common = {k for k, v in ctr.items() if v == min(ctr.values())}
        error_corrected_p1 += most_common.pop()
        error_corrected_p2 += least_common.pop()
    return error_corrected_p1, error_corrected_p2


if __name__ == "__main__":
    p1_ans, p2_ans = solve()
    print(f"Part 1 solution: {p1_ans}")
    print(f"Part 2 solution: {p2_ans}")
