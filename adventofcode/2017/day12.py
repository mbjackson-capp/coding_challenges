import networkx as nx
from aocd import get_data

input = get_data(year=2017, day=12)


def parse_pipes(input: str) -> nx.Graph:
    records = input.split("\n")
    G = nx.Graph()
    for record in records:
        node_a, adjacents = record.split(" <-> ")
        node_a = int(node_a)
        adjacents = [int(i) for i in adjacents.split(", ")]
        for node_b in adjacents:
            G.add_edge(node_a, node_b)
    return G


def solve(input: str) -> int:
    G = parse_pipes(input)
    p2_ans = len(list(nx.connected_components(G)))
    for group in nx.connected_components(G):
        if 0 in group:
            p1_ans = len(group)
    return p1_ans, p2_ans


if __name__ == "__main__":
    p1_ans, p2_ans = solve(input)
    print(f"Part 1 answer: {p1_ans}")
    print(f"Part 2 answer: {p2_ans}")
