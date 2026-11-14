import re
from itertools import batched

import pandas as pd
from input_data import q4_p1, q4_p2


def get_quest_df(input: str) -> pd.DataFrame:
    input_split = input.split("\n")
    # TODO: make this much less janky
    input_batched = [batched(re.split(r"=|\s", row), 2) for row in input_split]
    records = []
    for row in input_batched:
        row_dict = {}
        for pair in row:
            row_dict[pair[0]] = int(pair[1])
        records.append(row_dict)
    df = pd.DataFrame.from_records(records)
    return df


def checksum(sorted_vals: pd.Series) -> int:
    # TODO: fix this so ties stay tied
    return sum((i + 1) * val for i, val in enumerate(sorted_vals))


def part1(input):
    df = get_quest_df(input)
    sorted_df = df.loc[:, ["id", "time"]].groupby("id").sum().sort_values(by="time")
    return checksum(sorted_df["time"])


def part2(input):
    df = get_quest_df(input)
    df["questpart"] = df["quest"].astype(str) + df["part"].astype(str)
    completed_parts = df.loc[:, ["id", "questpart"]].groupby("id").count()
    completed_times = df.loc[:, ["id", "time"]].groupby("id").sum()
    ans_df = pd.merge(
        completed_parts, completed_times, left_on="id", right_on="id"
    ).sort_values(by=["questpart", "time"], ascending=[False, True])
    return checksum(ans_df["time"])


if __name__ == "__main__":
    print(f"Part 1 answer: {part1(q4_p1)}")
    print(f"Part 2 answer: {part2(q4_p2)}")
    # TODO: Part 3
