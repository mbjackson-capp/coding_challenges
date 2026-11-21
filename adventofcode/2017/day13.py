from time import sleep

from aocd import get_data


class Layer:
    """Representation of a firewall layer with a scanner in it."""

    def __init__(self, depth: int, v_range: int):
        self.depth = depth
        self.v_range = v_range

    def scanner_position_at_time(self, t: int) -> int:
        """Vertical position within range that the scanner will ENTER INTO
        by the END of picosecond t. If the packet enters that position at
        the same time, the packet will NOT be caught."""
        # e.g. for range 4, this produces [0, 1, 2, 3, 2, 1]
        mod_positions = (
            list(range(self.v_range)) + list(range(1, self.v_range - 1))[::-1]
        )
        return mod_positions[t % len(mod_positions)]

    @property
    def severity(self):
        return self.depth * self.v_range

    def __repr__(self):
        return f"Layer(d={self.depth}, r={self.v_range})"


def make_firewall(input: str) -> dict:
    firewall = {}
    for line in input.split("\n"):
        depth, v_range = [int(i) for i in line.split(": ")]
        firewall[depth] = Layer(depth, v_range)
    return firewall


def simulate_trip(fw: dict, delay: int = 0) -> tuple[bool, int]:
    t = delay
    got_caught = False
    total_severity = 0
    while True:
        pos = max(0, t - delay)
        if pos > max(fw):  # packet cleared the last firewall layer
            break
        if t >= delay and pos in fw:
            cur_fw = fw[pos]
            if cur_fw.scanner_position_at_time(t) == 0:
                got_caught = True
                total_severity += cur_fw.severity
        # TODO: should be possible to increment directly to next firewall layer time
        # can create an iterator of firewall depths (keys) and advance t using next()
        # but have to be careful about always including 0
        # scanner arrives AFTER you do, so time increments AFTER scanner check
        t += 1
    if not got_caught:
        print("You were never caught! Hooray")
    return got_caught, total_severity


def part2(fw: dict) -> int:
    delay = 0
    while True:
        if delay % 1000 == 0:
            print(f"Testing delay of {delay} picoseconds")
        got_caught, _ = simulate_trip(fw, delay=delay)
        if not got_caught:
            return delay
        delay += 1


# there should be a way to check for repetitious times and skip them
# based on scanner positions at that time
# and cache those?

if __name__ == "__main__":
    input = get_data(year=2017, day=13)
    fw = make_firewall(input)
    _, p1_ans = simulate_trip(fw)
    print(f"Part 1 answer: {p1_ans}")
    print(f"Now running Part 2... THIS COULD TAKE SEVERAL MINUTES...")
    sleep(3)
    p2_ans = part2(fw)
    print(f"Part 2 answer: {p2_ans}")
