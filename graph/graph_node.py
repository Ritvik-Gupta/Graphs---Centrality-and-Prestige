from __future__ import annotations


# Class for denoting a Graph Network's Node
class GraphNode:
    def __init__(self, id: str):
        self.id = id # with a specific unique ID
        self.store = {} # a store for any information about the node
        self.out_links: dict[str, GraphNode] = {} # Out Links are directed links to Neighbors
        self.in_links: dict[str, GraphNode] = {} # In Links are directed links towards this Node

    def add_neighbour(self, neighbour_node: GraphNode):
        # If A -> B then A has an out-link to B and B has an in-link from A 
        self.out_links[neighbour_node.id] = neighbour_node
        neighbour_node.in_links[self.id] = self

    def num_out_links(self) -> int:
        return len(self.out_links)
