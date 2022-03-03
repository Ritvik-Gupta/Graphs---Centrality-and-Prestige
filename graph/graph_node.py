from __future__ import annotations


class GraphNode:
    def __init__(self, id: str):
        self.id = id
        self.store = {}
        self.out_links: dict[str, GraphNode] = {}
        self.in_links: dict[str, GraphNode] = {}

    def add_neighbour(self, neighbour_node: GraphNode):
        self.out_links[neighbour_node.id] = neighbour_node
        neighbour_node.in_links[self.id] = self

    def num_out_links(self) -> int:
        return len(self.out_links)
