from graph.graph_network import GraphNetwork
from graph.shortest_paths import PathsAdjacencyMatrix, ShortestPaths


# An All Node Pairs Paths Finding Algorithm
# Has a Time Complexity of V^3, where V is the number of Nodes in the Network
# Algorithms utilizes heavy Dynamic Programming Calculations to compute possible 
# paths given direct Neighbors from the Initial Iteration 
def floyd_warshall_algorithm(graph: GraphNetwork) -> PathsAdjacencyMatrix:
    ids = list(graph.nodes.keys())
    num_nodes = len(graph.nodes)
    adjacency_list: PathsAdjacencyMatrix = {}

    # Compute the First Iteration Adjacency List
    for node_id in ids:
        row: dict[str, ShortestPaths] = {}
        adjacency_list[node_id] = row

        for neighbor_id in ids:
            shortest_path = ShortestPaths()
            if node_id == neighbor_id:  # A->A so empty path is required
                shortest_path.check_add([])
            elif neighbor_id in graph.nodes[node_id].out_links:  # A does go to B
                # Starting from A visit only B next to reach B
                shortest_path.check_add([neighbor_id])

            # If they are not direct neighbors then add as no paths
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
                if curr_path.length() < sum_path.length():
                    row[y] = curr_path
                else:
                    if sum_path.length() == curr_path.length():
                        sum_path.unchecked_consume(curr_path)
                    row[y] = sum_path

    return next_level_dp
