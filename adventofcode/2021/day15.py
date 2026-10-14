import heapq

import numpy as np
from aocd import get_data

from myutils import gridify, neighbor_locs

cavern = gridify(get_data(day=15, year=2021), intify=True)


def expand(cavern):
    """Create the expanded-size map for Part 2"""
    expanded = np.concatenate([cavern + i for i in range(5)], axis=1)
    expanded = np.concatenate([expanded + i for i in range(5)], axis=0)
    expanded[expanded > 9] -= 9
    return expanded


def dijkstra_pq(cavern, start_node=(0, 0), end_node="default", part=1):
    """
    Priority queue implementation inspired by
    https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/.
    Comments on steps adapted from Wikipedia, "Dijkstra's algorithm"
    """
    if part == 2:
        cavern = expand(cavern)
    max_y, max_x = cavern.shape
    if end_node == "default":
        end_node = (max_x - 1, max_y - 1)
    # unattainably high value, since np.inf isn't usable in int-dtype array
    INF = np.sum(cavern) + 1

    # Assign to every node a tentative distance value
    distances = {}
    for x in range(max_x):
        for y in range(max_y):
            node = (x, y)
            distances[node] = 0 if node == start_node else INF

    priority_queue = [(0, start_node)]

    while len(priority_queue) > 0:
        # Select the unvisited node that is marked with the smallest tentative
        # distance; set it as the new current node to "visit" it
        curr_dist, curr_node = heapq.heappop(priority_queue)

        # Calculate tentative distances to each unvisited neighbor through
        # current node
        curr_x, curr_y = curr_node
        neighbors = [pt for pt in neighbor_locs(cavern, curr_x, curr_y)]
        for neighbor in neighbors:
            neigh_x, neigh_y = neighbor
            neigh_dist = curr_dist + cavern[neigh_x][neigh_y]
            # Compare newly calculated tentative distance to the earlier value
            # and keep the smaller of the two
            if neigh_dist < distances[neighbor]:
                distances[neighbor] = neigh_dist
                # keep track of unvisited nodes with finite tentative distance
                heapq.heappush(priority_queue, (neigh_dist, neighbor))

    return distances[end_node]


if __name__ == "__main__":
    print(f"Part 1 answer: {dijkstra_pq(cavern)}")
    print(f"Part 2 answer: {dijkstra_pq(cavern, part=2)}")
