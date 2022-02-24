from itertools import count

from tabulate import tabulate

from graph.GraphNode import GraphNode
from graph.ShortestPaths import ShortestPaths

PathsAdjacencyMatrix = dict[str, dict[str, ShortestPaths]]


class Graph:
    def __init__(self):
        self.nodes: dict[str, GraphNode] = {}

    def add_node(self, node_id: str):
        self.nodes[node_id] = GraphNode(node_id)

    def connect_nodes(self, a_node_id: str, b_node_id: str):
        self.nodes[a_node_id].add_neighbour(self.nodes[b_node_id])
        self.nodes[b_node_id].add_neighbour(self.nodes[a_node_id])

    def degree_centrality(self):
        normalization_factor = len(self.nodes) - 1
        for node in self.nodes.values():
            node.store["Degree Centrality"] = len(node.neighbors) / normalization_factor

    def floyd_warshall_algorithm(self) -> PathsAdjacencyMatrix:
        ids = list(self.nodes.keys())
        num_nodes = len(self.nodes)
        adjacency_list: PathsAdjacencyMatrix = {}

        for node_id in ids:
            row: dict[str, ShortestPaths] = {}
            adjacency_list[node_id] = row

            for neighbor_id in ids:
                shortest_path = ShortestPaths()
                if node_id == neighbor_id:
                    shortest_path.check_add([])
                elif neighbor_id in self.nodes[node_id].neighbors:
                    shortest_path.check_add([neighbor_id])

                row[neighbor_id] = shortest_path

        curr_level_dp: PathsAdjacencyMatrix = {}
        next_level_dp = adjacency_list

        for level in map(lambda x: ids[x], range(num_nodes)):
            curr_level_dp = next_level_dp
            next_level_dp = {}

            for x in map(lambda x: ids[x], range(num_nodes)):
                row: dict[str, ShortestPaths] = {}
                next_level_dp[x] = row

                for y in map(lambda x: ids[x], range(num_nodes)):
                    curr_path = curr_level_dp[x][y]
                    sum_path = ShortestPaths.unchecked_union(
                        curr_level_dp[x][level], curr_level_dp[level][y]
                    )
                    if len(curr_path) < len(sum_path):
                        row[y] = curr_path
                    else:
                        if len(sum_path) == len(curr_path):
                            sum_path.unchecked_consume(curr_path)
                        row[y] = sum_path

        return next_level_dp

    def closeness_centrality(self, paths_matrix: PathsAdjacencyMatrix):
        normalization_factor = len(self.nodes) - 1
        for node in self.nodes.values():
            paths_sum = sum(map(lambda x: len(x), paths_matrix[node.id].values()))
            node.store["Closeness Centrality"] = normalization_factor / paths_sum

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
                    betweenness += sum(1 for _ in paths_having_node) / len(paths)

            node.store["Betweenness Centrality"] = betweenness / normalization_factor
