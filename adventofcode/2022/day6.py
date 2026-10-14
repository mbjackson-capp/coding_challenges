from aocd import get_data


input = get_data(day=6, year=2022)

PACKET = 4
MESSAGE = 14

def find_marker(marker_size: int):
    for i in range(len(input)):
        if len(set(input[i:i+marker_size])) == marker_size:
            return i + marker_size

print(f"Part 1 answer: {find_marker(PACKET)}")
print(f"Part 2 answer: {find_marker(MESSAGE)}")

