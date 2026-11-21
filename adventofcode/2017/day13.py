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


L = Layer(0, 3)
L.scanner_position_at_time(0)


def test_scanner_positions():
    assert Layer(0, 3).scanner_position_at_time(2) == 2
    assert Layer(1, 1).scanner_position_at_time(2) == 0
    assert Layer(4, 4).scanner_position_at_time(4) == 1
    assert Layer(6, 4).scanner_position_at_time(6) == 1


test_input = """0: 3
1: 2
4: 4
6: 4"""


def make_firewall(input: str) -> dict:
    firewall = {}
    for line in input.split("\n"):
        depth, v_range = [int(i) for i in line.split(": ")]
        firewall[depth] = Layer(depth, v_range)
    return firewall


def whole_trip_severity(fw: dict, delay: int = 0) -> int:
    print(fw)
    t = 0
    total_severity = 0
    # your packet enters layer t at vertical coordinate 0 at picosecond t
    while t <= max(fw):
        # print(f"Picosecond {t}")
        if t in fw:
            cur_fw = fw[t]
            # scanner arrives AFTER you do
            if cur_fw.scanner_position_at_time(t) == 0:
                print(
                    f"You are caught at layer {t}! Add severity of {cur_fw} = {cur_fw.severity} to total"
                )
                total_severity += cur_fw.severity
        t += 1
    if total_severity == 0:
        print("You were never caught! Hooray")
    return total_severity


def part2(fw: dict) -> int:
    delay = 0
    while True:
        if whole_trip_severity(fw, delay=delay) == 0:
            return delay
        delay += 1


if __name__ == "__main__":
    input = get_data(year=2017, day=13)
    fw = make_firewall(input)
    print(f"Part 1 answer: {whole_trip_severity(fw)}")
