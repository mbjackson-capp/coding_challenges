import networkx as nx
from input_data import q2_p1, q2_p2, q2_p3

from myutils import apply_then_combine


def read_alloy_groups(input: str) -> list[tuple[int,int]]:
    group_strings = input.split("\n")
    groups = []
    for s in group_strings:
        rels = s.split(" ")
        groups.append(rels)
    return groups


def determine_alloy_order(group: list[str]) -> int:
    """Represent the hardness order of a group of alloys as an integer.
    Grounding insight/hope: constructing an ordered preference relation
    as a DAG with directed edges (a,b) meaning 'alloy a is harder than alloy
    b' allows for retrieving the full ordering of all alloys with toposort.
    By problem construction, this should work on any provided inputs even if 
    not all pairwise comparisons are known."""
    G = nx.DiGraph()
    for rel in group:
        alloy_a, relation, alloy_b = [char for char in rel]
        if relation == '<':
            G.add_edge(alloy_b, alloy_a)
        elif relation == '>':
            G.add_edge(alloy_a, alloy_b)
    full_order = list(nx.topological_sort(G))
    return int(''.join(full_order))


def solve(input: str) -> int:
    checksum = 0
    groups = read_alloy_groups(input)
    for group in groups:
        checksum += determine_alloy_order(group)
    return checksum


if __name__ == '__main__':
    print(f"Part 1 answer: {apply_then_combine(read_alloy_groups(q2_p1), determine_alloy_order)}")
    print(f"Part 2 answer: {apply_then_combine(read_alloy_groups(q2_p2), determine_alloy_order)}")
    print(f"Part 3 answer: {apply_then_combine(read_alloy_groups(q2_p3), determine_alloy_order)}")


