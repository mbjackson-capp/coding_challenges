from aocd import get_data
import numpy as np

instructions = get_data(year=2016, day=8).split("\n")

OFF = "."
ON = "#"


def make_screen(width: int=50, height: int=6) -> np.array:
    return np.full((height, width), OFF)


def execute_instruction(screen: np.array, instruction: str) -> np.array:
    instruction_parts = instruction.split(" ")
    if instruction_parts[0] == "rect":
        # turn on all pixels in a top-left rectangle
        rect_x, rect_y = instruction_parts[1].split("x")
        screen[:int(rect_y), :int(rect_x)] = ON
        return screen
    elif instruction_parts[0] == "rotate":
        _, subset, index, _, B = instruction_parts
        _, index = index.split("=")
        B = int(B)
        # you can index a np column like screen[:,2] or a row like screen[2:]
        if subset == "row":
            # shift row right by B pixels, wrapping
            old_row = screen[int(index)]
            new_row = np.concatenate((old_row[-B:], old_row[:-B]))
            screen[int(index)] = new_row
        elif subset == "column":
            # shift column down by B pixels, wrapping
            old_col = screen[:,int(index)]
            new_col = np.concatenate((old_col[-B:], old_col[:-B]))
            screen[:,int(index)] = new_col
        return screen
    raise ValueError(f"Received ill-formed instruction {instruction}")
        

def count_on_pixels(screen: np.array):
    unique, counts = np.unique(screen, return_counts=True)
    on_off_count = dict(zip(unique, counts))
    return on_off_count[ON]


def run(instructions: list[str], width: int=50, height: int=6):
    screen = make_screen(width=width, height=height)
    for instruction in instructions:
        execute_instruction(screen, instruction)
    return screen


if __name__ == '__main__':
    screen = run(instructions)
    print(f"Part 1 answer: {count_on_pixels(screen)}")
    print(f"Part 2 answer:")
    for row in screen:
        print(''.join(row))