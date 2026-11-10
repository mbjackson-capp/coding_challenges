import re
from math import floor

from aocd import get_data

from myutils import apply_then_combine

input = get_data(day=4, year=2023).split("\n")


def split_and_intify(str):
    """Split a string of numbers at the spaces and keep only the integers."""
    splitted = re.split(r"\s+", str)
    splitted = [int(i) for i in splitted if i.isnumeric()]
    return splitted


def prepare(input):
    """
    Format each line of input data as a "scratch card", i.e. a 3-item list:
        - item 0: card ID
        - item 1: "winning numbers"
        - item 2: numbers you have
    Returns list of "scratch cards".
    """
    input = [re.sub(r"Card\s+", "", i) for i in input]
    input = [re.split(r":|\|\s+", i) for i in input]
    scratch_cards = [[int(i[0]), split_and_intify(i[1]), split_and_intify(i[2])] for i in input]
    return scratch_cards


scratch_cards = prepare(input)


def num_matches(card):
    """
    Calculate how many matches there are between the winning numbers (left
    side of the '|') and the numbers you have (right side of the '|') on a
    properly-formatted scratch card.
    """
    _, winning_nums, nums_you_have = card
    match_nums = [i for i in nums_you_have if i in winning_nums]
    return len(match_nums)


def card_points(card):
    return floor(2 ** (num_matches(card) - 1))


def part2(scratch_cards):
    # Track how many of each card there are
    ids_ordered = [i[0] for i in scratch_cards]
    LAST_CARD = ids_ordered[-1]
    card_counts = {id: 1 for id in ids_ordered}

    for id in ids_ordered:
        card = scratch_cards[id - 1]
        cards_to_copy = [
            j for j in list(range(id + 1, id + num_matches(card) + 1)) if j <= LAST_CARD
        ]
        for copy_id in cards_to_copy:
            # make one of each copy for EACH existing instance of this card
            card_counts[copy_id] += card_counts[id]
    total_points = sum(card_counts.values())
    return total_points


if __name__ == "__main__":
    print(f"Part 1 answer: {apply_then_combine(scratch_cards, card_points)}")
    print(f"Part 2 answer: {part2(scratch_cards)}")
