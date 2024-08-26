from typing import Dict, Set, Union
import heapq


class Graph:
    def __init__(self):
        self.nodes: Set[str] = set()
        self.edges = {}

    def add_node(self, value: str):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = {}

    def add_edge(self, from_node: str, to_node: str, weight: int):
        self.add_node(from_node)
        self.add_node(to_node)
        self.edges[from_node][to_node] = weight
        self.edges[to_node][from_node] = weight


def dijkstra_shortest_path(graph: Graph, start: str) -> Dict[str, Union[int, float]]:
    distances = {node: float("inf") for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges.get(current_node, {}).items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
