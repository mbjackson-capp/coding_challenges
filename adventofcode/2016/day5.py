from hashlib import md5

from aocd import get_data

door_id = get_data(year=2016, day=5)
print(door_id)

PASSWORD_LENGTH = 8
VALID_POSITIONS = ["0", "1", "2", "3", "4", "5", "6", "7"]


def is_interesting(hash: str) -> bool:
    if len(hash) < 6:
        return False
    return hash[0:5] == "00000"


def get_passwords() -> tuple[str, str]:
    part1_password = ""
    part2_passdict = {k: None for k in range(PASSWORD_LENGTH)}
    idx = 0
    part2_hits = 0
    while part2_hits < PASSWORD_LENGTH:
        thing_to_hash = door_id + str(idx)
        new_hash = md5(thing_to_hash.encode()).hexdigest()
        if is_interesting(new_hash):
            print(f"{new_hash} is interesting!")
            if len(part1_password) < PASSWORD_LENGTH:
                part1_password += new_hash[5]
            if new_hash[5] in VALID_POSITIONS:
                if part2_passdict[int(new_hash[5])] is None:
                    print(f"  ...and its sixth index is an unseen valid position: {new_hash[5]}")
                    part2_passdict[int(new_hash[5])] = new_hash[6]
                    part2_hits += 1
                    print(part2_passdict)
        idx += 1
    part2_password = "".join(str(part2_passdict[k]) for k in sorted(part2_passdict.keys()))
    return part1_password, part2_password


if __name__ == "__main__":
    p1_ans, p2_ans = get_passwords()
    print(f"\nPart 1 solution: {p1_ans}\nPart 2 solution: {p2_ans}")