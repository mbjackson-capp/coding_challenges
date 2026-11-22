import re

from aocd import get_data

GENERATOR_A_FACTOR = 16807
GENERATOR_B_FACTOR = 48271
DIVISOR = 2147483647


class Generator:
    def __init__(self, starting_value, factor, submit_multiple=1):
        self.value = starting_value
        self.factor = factor
        self.submit_multiple = submit_multiple

    def update(self):
        product = self.value * self.factor
        self.value = product % DIVISOR

    def holds_proper_multiple(self) -> bool:
        return self.value % self.submit_multiple == 0


gen_a_test = Generator(65, GENERATOR_A_FACTOR)
gen_b_test = Generator(8921, GENERATOR_B_FACTOR)


def binary_16bit(n: int) -> str:
    # TODO: consider if bit level operations would be faster
    return f"{n:b}"[-16:]


def solve(
    a_start: int,
    b_start: int,
    a_multiple: int = 1,
    b_multiple: int = 1,
    pair_limit: int = 40_000_000,
) -> int:
    gen_a = Generator(a_start, GENERATOR_A_FACTOR, submit_multiple=a_multiple)
    gen_b = Generator(b_start, GENERATOR_B_FACTOR, submit_multiple=b_multiple)
    a_queue = []
    b_queue = []
    matches = 0
    pairs_judged = 0
    while pairs_judged < pair_limit:
        # would it be noticeably faster to get to 5 million valid multiples for each
        # and then submit both 5,000,000-long lists to judge at end of that process?
        gen_a.update()
        if gen_a.holds_proper_multiple():
            a_queue.append(gen_a.value)

        gen_b.update()
        if gen_b.holds_proper_multiple():
            b_queue.append(gen_b.value)

        if len(a_queue) > 0 and len(b_queue) > 0:
            pairs_judged += 1
            a_comparand = a_queue.pop(0)
            b_comparand = b_queue.pop(0)
            if binary_16bit(a_comparand) == binary_16bit(b_comparand):
                matches += 1
                print(
                    f"Match found: {a_comparand} and {b_comparand} ({pairs_judged} pairs judged, {matches} so far)"
                )
    return matches


def get_start_values(input: str) -> tuple[int, int]:
    vals = [int(i) for i in re.split(r" |\n", input) if i.isnumeric()]
    return vals


# NOTE: This is very slow: ~3-5 min for part 1 and ~1-2 hr for part 2.
# Consider running this in the background and coming back much later.
# TODO: greatly increase speed, perhaps with modular arithmetic tricks
if __name__ == "__main__":
    input = get_data(year=2017, day=15)
    a_start, b_start = get_start_values(input)
    p1_ans = solve(a_start, b_start)
    p2_ans = solve(a_start, b_start, a_multiple=4, b_multiple=8, pair_limit=5_000_000)
    print(f"All done!")
    print(f"Part 1 answer: {p1_ans}")
    print(f"Part 2 answer: {p2_ans}")
