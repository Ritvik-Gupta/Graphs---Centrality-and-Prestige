from __future__ import annotations


class GraphNode:
    def __init__(self, id: str):
        self.id = id
        self.store = {}
        self.neighbors: dict[str, GraphNode] = {}
        self.shadow_neighbors: dict[str, GraphNode] = {}

    def add_neighbour(self, neighbour_node: GraphNode):
        self.neighbors[neighbour_node.id] = neighbour_node
        neighbour_node.shadow_neighbors[self.id] = self
