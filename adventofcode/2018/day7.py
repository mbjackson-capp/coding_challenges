import networkx as nx
from aocd import get_data


def build_dag(input: str) -> nx.DiGraph:
    reqs = input.split("\n")
    DG = nx.DiGraph()
    for req in reqs:
        before, after = [
            i for i in req.split(" ") if i.isalpha() and i.isupper() and len(i) == 1
        ]
        DG.add_node(before, is_done=False, progress=0, worker=None)
        DG.add_node(after, is_done=False, progress=0, worker=None)
        DG.add_edge(before, after)
    return DG


def part1(input: str):
    DG = build_dag(input)
    # whoops, network x has it. TODO: consider hardcoding for learning purposes
    return "".join(list(nx.lexicographical_topological_sort(DG)))


ADDED_STEP_TIME = 60


def task_time(letter: str, added: int = ADDED_STEP_TIME) -> int:
    return ord(letter) - 64 + added


def is_available(n: str, DG: nx.DiGraph) -> bool:
    """An available task is an undone task with zero progress, no worker, and
    there are either no in-edges at all, or all its in-edges come from done tasks.
    (The no in-edges case can probably be handled automatically through vacuous truth)
    """
    # start with e.g. [('A', n), ('G', n), ...] and derive ['A', 'G', ...]
    origin_nodes = [i[0] for i in DG.edges if i[1] == n]
    done_origin_nodes = [i for i in origin_nodes if DG.nodes[i]["is_done"] == True]
    return (
        DG.nodes[n]["is_done"] == False
        and DG.nodes[n]["progress"] == 0
        and DG.nodes[n]["worker"] == None
        and origin_nodes == done_origin_nodes
    )


def is_finishing(n: str, DG: nx.DiGraph, added=ADDED_STEP_TIME) -> bool:
    return (
        DG.nodes[n]["is_done"] == False
        and DG.nodes[n]["worker"] is not None
        and DG.nodes[n]["progress"] == task_time(n, added=added)
    )


def part2(input: str, n_workers: int = 5, added_step_time=ADDED_STEP_TIME):
    """NOTE: This reduces to part 1 if n_workers is set to 1 and done_string
    is returned/printed"""
    DG = build_dag(input)
    t = 0
    available_workers = set(range(1, n_workers + 1))
    done_string = ""
    while any(DG.nodes[n]["is_done"] == False for n in DG.nodes):
        # assign available workers to available tasks, respecting alphabetic order
        available_tasks = sorted([n for n in DG.nodes if is_available(n, DG)])
        while len(available_workers) > 0 and available_tasks:
            n_first = available_tasks.pop(0)
            new_worker = (
                available_workers.pop()
            )  # i don't think this needs to care about worker order?
            DG.nodes[n_first]["worker"] = new_worker

        t += 1  # advance one second
        in_progress_tasks = [n for n in DG.nodes if DG.nodes[n]["worker"] is not None]
        for n in in_progress_tasks:
            DG.nodes[n]["progress"] += 1

        # consider all tasks that have reached their completion time
        finishing_tasks = [
            n for n in DG.nodes if is_finishing(n, DG, added=added_step_time)
        ]
        for n in finishing_tasks:
            # complete this task and release its worker back to available pool
            DG.nodes[n]["is_done"] = True
            available_workers.add(DG.nodes[n]["worker"])
            DG.nodes[n]["worker"] = None
            done_string += n
    return t


if __name__ == "__main__":
    input = get_data(day=7, year=2018)
    print(f"Part 1 answer: {part1(input)}")
    print(f"Part 2 answer: {part2(input)}")
