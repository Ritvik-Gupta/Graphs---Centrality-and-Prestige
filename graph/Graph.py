from graph.algorithms.floyd_warshall import PathsAdjacencyMatrix
from graph.GraphNode import GraphNode


class Graph:
    def __init__(self):
        self.nodes: dict[str, GraphNode] = {}

    def add_node(self, node_id: str):
        if node_id in self.nodes:
            raise
        self.nodes[node_id] = GraphNode(node_id)

    def connect_nodes(self, a_node_id: str, b_node_id: str):
        self.nodes[a_node_id].add_neighbour(self.nodes[b_node_id])
        self.nodes[b_node_id].add_neighbour(self.nodes[a_node_id])

    def degree_centrality(self):
        normalization_factor = len(self.nodes) - 1
        for node in self.nodes.values():
            node.store["Degree Centrality"] = len(node.neighbors) / normalization_factor

    def closeness_centrality(self, paths_matrix: PathsAdjacencyMatrix):
        normalization_factor = len(self.nodes) - 1
        for node in self.nodes.values():
            paths_sum = sum(
                map(
                    lambda x: x.length(default_length=0),
                    paths_matrix[node.id].values(),
                )
            )
            try:
                node.store["Closeness Centrality"] = normalization_factor / paths_sum
            except (ZeroDivisionError):
                node.store["Closeness Centrality"] = 0

    def betweenness_centrality(self, paths_matrix: PathsAdjacencyMatrix):
        normalization_factor = ((len(self.nodes) - 1) * (len(self.nodes) - 2)) / 2
        for node in self.nodes.values():
            betweenness = 0
            for s_id in self.nodes.keys():
                if node.id == s_id:
                    continue

                for t_id in self.nodes.keys():
                    if node.id == t_id:
                        continue

                    paths = paths_matrix[s_id][t_id].paths
                    paths_having_node = filter(lambda x: node.id in x, paths)
                    if len(paths) > 0:
                        betweenness += sum(1 for _ in paths_having_node) / len(paths)

            node.store["Betweenness Centrality"] = betweenness / normalization_factor

    def degree_prestige(self):
        normalization_factor = len(self.nodes) - 1
        for node in self.nodes.values():
            node.store["Degree Prestige"] = len(node.shadows) / normalization_factor

    def proximity_prestige(self, paths_matrix: PathsAdjacencyMatrix):
        normalization_factor = len(self.nodes) - 1
        for node in self.nodes.values():
            in_path_lengths = list(
                filter(
                    lambda x: x != 0,
                    map(
                        lambda x: x[node.id].length(default_length=0),
                        paths_matrix.values(),
                    ),
                )
            )

            node_proximity = 0
            if len(in_path_lengths) != 0:
                node_proximity = len(in_path_lengths) ** 2 / sum(in_path_lengths)
            node.store["Proximity Prestige"] = node_proximity / normalization_factor
