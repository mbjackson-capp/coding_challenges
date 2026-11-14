import re
from itertools import batched

import pandas as pd
from input_data import q4_p1, q4_p2, q4_p3


def get_quest_df(input: str) -> pd.DataFrame:
    input_split = input.split("\n")
    input_batched = [batched(re.split(r"=|\s", row), 2) for row in input_split]
    records = []
    for row in input_batched:
        row_dict = {}
        for pair in row:
            row_dict[pair[0]] = int(pair[1])
        records.append(row_dict)
    df = pd.DataFrame.from_records(records)
    return df


def checksum(sorted_vals: pd.Series | list[int]) -> int:
    sorted_vals = pd.Series(sorted_vals)
    # make sure ties in rank order stay tied (e.g. 1st, t-2nd, t-2nd, 4th)
    ranks = sorted_vals.rank(method="min", ascending=False).astype(int)
    cs = 0
    for z in zip(sorted_vals, ranks):
        val, rank = z
        cs += val * rank
    return cs


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


def part3(input):
    df = get_quest_df(input)
    final_rankings = {id: 0 for id in df["id"]}
    quests = df["quest"].drop_duplicates()
    for q in sorted(quests):
        quest_df = df[df["quest"] == q]
        for p in range(1, 4):
            part_df = quest_df[quest_df["part"] == p]
            # add up all times for parts up through current one
            sum_times = (
                (
                    quest_df.loc[(quest_df["part"] <= p), ["id", "time"]]
                    .groupby("id")
                    .sum()
                )
                .rename(columns={"time": "sumtime"})
                .reset_index()
            )
            part_df = part_df.merge(sum_times, on="id")
            # keep in ties as described in problem statement
            part_df["ranking"] = part_df["sumtime"].rank(method="min").astype(int)
            part_max = 50 * p
            part_df["points"] = (part_max + 1 - part_df["ranking"]).apply(
                lambda x: max(0, x)  # minimum point value for a part is 0
            )
            part_df = part_df.sort_values(by="points", ascending=False)
            ids_points = zip(part_df["id"], part_df["points"])
            for pair in ids_points:
                id, points = pair
                final_rankings[id] += points
    cs_input = sorted(final_rankings.values(), reverse=True)
    return checksum(cs_input)


if __name__ == "__main__":
    print(f"Part 1 answer: {part1(q4_p1)}")
    print(f"Part 2 answer: {part2(q4_p2)}")
    print(f"Part 3 answer: {part3(q4_p3)}")
