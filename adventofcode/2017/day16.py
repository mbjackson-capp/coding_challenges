from aocd import get_data

SPIN = "s"
EXCHANGE = "x"
PARTNER = "p"


def generate_dancers(n: int) -> str:
    # chr(97) = 'a', chr(98) = 'b', and so on
    return "".join([chr(i + 97) for i in range(n)])


def swap(dancers: str, pos_A: int, pos_B: int) -> str:
    """Helper to DRY Exchange and Partner position swaps"""
    pos_early = min(pos_A, pos_B)
    pos_late = max(pos_A, pos_B)
    return (
        dancers[:pos_early]
        + dancers[pos_late]
        + dancers[pos_early + 1 : pos_late]
        + dancers[pos_early]
        + dancers[pos_late + 1 :]
    )


def do_dance(moves: list[str], dancers: str) -> str:
    for move in moves:
        if move[0] == SPIN:
            X = int(move[1:])
            dancers = dancers[-X:] + dancers[:-X]
        elif move[0] == EXCHANGE:
            pos_A, pos_B = [int(i) for i in move[1:].split("/")]
            dancers = swap(dancers, pos_A, pos_B)
        elif move[0] == PARTNER:
            prog_A, prog_B = move[1:].split("/")
            pos_A = dancers.index(prog_A)
            pos_B = dancers.index(prog_B)
            dancers = swap(dancers, pos_A, pos_B)
    return dancers


def part2(moves: list[str], n_dancers: int = 16) -> str:
    ONE_BILLION = 1_000_000_000
    dancers = generate_dancers(n_dancers)
    results: dict = {dancers: [0]}
    for i in range(1, ONE_BILLION + 1):
        dancers = do_dance(moves, dancers)
        if dancers not in results:
            results[dancers] = [i]
        else:
            """
            As soon as we see any arrangement a second time, we've detected a
            cycle of dancer arrangements that will repeat endlessly. (I think
            this is because the moves are cyclical so there's a cycle of arrangements
            on moves, and the set of arrangements after each full dance is just a
            selective snapshot of the arrangements after each move.)

            At that point, since we know how many dances it took to get through
            that first cycle, you can just modulus ONE_BILLION into that length
            to know what the arrangement has to be after the billionth dance.
            """
            for arrangement, v in results.items():
                if ONE_BILLION % i in v:
                    return arrangement


if __name__ == "__main__":
    dance = get_data(year=2017, day=16).split(",")
    p1_ans = do_dance(dance, generate_dancers(16))
    print(f"Part 1 answer: {p1_ans}")
    p2_ans = part2(dance, 16)
    print(f"Part 2 answer: {p2_ans}")
