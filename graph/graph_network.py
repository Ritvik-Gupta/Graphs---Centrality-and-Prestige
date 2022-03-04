from graph.errors import NodesWithSameID, NoSuchNodeWithID
from graph.graph_node import GraphNode
from graph.shortest_paths import PathsAdjacencyMatrix


# Class for denoting proper Graph Structure in an Adjacency List format.
# Each Node is its own entity and has out/in links to denote its Neighbor Nodes
class GraphNetwork:
    def __init__(self):
        self.nodes: dict[str, GraphNode] = {}

    def add_node(self, node_id: str):
        if node_id in self.nodes:
            raise NodesWithSameID(node_id)
        self.nodes[node_id] = GraphNode(node_id)

    # Adds an Undirected Edge between two nodes such that
    # A -> B and B -> A. Both have out and in links to each other.
    def connect_nodes(self, a_node_id: str, b_node_id: str):
        if a_node_id not in self.nodes:
            raise NoSuchNodeWithID(a_node_id)
        if b_node_id not in self.nodes:
            raise NoSuchNodeWithID(b_node_id)

        self.nodes[a_node_id].add_neighbour(self.nodes[b_node_id])
        self.nodes[b_node_id].add_neighbour(self.nodes[a_node_id])

    """
    Cd(A) = Out Links from A / Normalization Factor
    """

    def degree_centrality(self):
        normalization_factor = len(self.nodes) - 1
        for node in self.nodes.values():
            node.store["Degree Centrality"] = (
                node.num_out_links() / normalization_factor
            )

    """
    Takes the Shortest Paths Matrix computed to easily calculate
    for every Node the shortest distance to another Node.
    
    Cc(A) = Normalization Factor / Sum of Shortest Paths from A to other Nodes
    """

    def closeness_centrality(self, paths_matrix: PathsAdjacencyMatrix):
        normalization_factor = len(self.nodes) - 1
        for node in self.nodes.values():
            paths_sum = sum(
                map(
                    lambda x: x.length(default_length=0),
                    # If a Node is not reachable then assume it has 0 distance
                    paths_matrix[node.id].values(),
                )
            )

            # As Paths Sum can be 0 ( no path exists to any Node )
            try:
                node.store["Closeness Centrality"] = normalization_factor / paths_sum
            except (ZeroDivisionError):
                node.store[
                    "Closeness Centrality"
                ] = 0  # If No Path exists just assume 0

    """
    Takes the Shortest Paths Matrix computed to easily calculate
    for every Node to every other Node if the shortest path goes through a particular Node.

    Cb(A) =  Betweenness of A in every other Node Pair / Normalization Factor
    """

    def betweenness_centrality(self, paths_matrix: PathsAdjacencyMatrix):
        normalization_factor = ((len(self.nodes) - 1) * (len(self.nodes) - 2)) / 2
        for node in self.nodes.values():  # For a given Node to calculate Betweenness
            betweenness = 0
            for s_id in self.nodes.keys():  # From S Node
                if node.id == s_id:  # Cannot be the same Node
                    continue

                for t_id in self.nodes.keys():  # To T Node
                    if node.id == t_id:  # Cannot be the same Node
                        continue

                    # Get the paths possible from S to T
                    paths = paths_matrix[s_id][t_id].paths
                    # Count every path which passes through given Node
                    paths_having_node = filter(lambda x: node.id in x, paths)
                    if len(paths) > 0:  # Atleast a Path should exist
                        betweenness += sum(1 for _ in paths_having_node) / len(paths)

            node.store["Betweenness Centrality"] = betweenness / normalization_factor

    """
    Pd(A) = In Links to A / Normalization Factor
    """

    def degree_prestige(self):
        normalization_factor = len(self.nodes) - 1
        for node in self.nodes.values():
            node.store["Degree Prestige"] = len(node.in_links) / normalization_factor

    """
    Pp(A) = (Number of Incoming Paths)^2 / Sum of paths lengths incoming to A * Normalization Factor
    """

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
            # If there is No Incoming Path then assume proximity of 0
            node_proximity = 0
            if len(in_path_lengths) != 0:
                node_proximity = len(in_path_lengths) ** 2 / sum(in_path_lengths)
            node.store["Proximity Prestige"] = node_proximity / normalization_factor
