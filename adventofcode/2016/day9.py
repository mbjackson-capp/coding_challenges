import re

from aocd import get_data


input: list[str] = get_data(year=2016, day=9)

LEFT_PAREN = "("
RIGHT_PAREN = ")"


def parse_repeat_marker(rmark: str) -> tuple[int, int]:
    if rmark[0] != LEFT_PAREN and rmark[-1] != RIGHT_PAREN and "x" not in rmark:
        raise ValueError(f"{rmark} is not a valid repeat marker!")
    section_len, repetitions = (x for x in re.split(r"\(|\)|x", rmark) if x.isnumeric())
    return int(section_len), int(repetitions)


def decompressed_len(s: str, is_part2: False) -> int:
    """you only need to preserve length of returned string, not full string"""
    # base case: it'll keep walking all the way through so just return length now
    if LEFT_PAREN not in s and RIGHT_PAREN not in s:
        return len(s)
    else:
        lds = 0
        ptr = 0
        repeat_marker = ""
        while ptr < len(s):
            char = s[ptr]
            if char == " ":  # ignore whitespace
                continue
            if char == LEFT_PAREN:
                repeat_marker = char
                ptr += 1
            elif char == RIGHT_PAREN:
                # do the ENTIRE lookahead and repetition now,
                # then move pointer in original string
                section_len, repetitions = parse_repeat_marker(repeat_marker)
                ptr += 1
                section = s[ptr : ptr + section_len]
                if is_part2:
                    # recursive step: get length of decompressed subsection
                    lds += decompressed_len(section, is_part2=True) * repetitions
                else:
                    lds += len(section) * repetitions
                repeat_marker = ""
                ptr += section_len
            elif repeat_marker:
                repeat_marker += char
                ptr += 1
            else:
                lds += 1
                ptr += 1
        return lds


if __name__ == "__main__":
    print(f"Part 1 solution: {decompressed_len(input, is_part2=False)}")
    print(f"Part 2 solution: {decompressed_len(input, is_part2=True)}")
