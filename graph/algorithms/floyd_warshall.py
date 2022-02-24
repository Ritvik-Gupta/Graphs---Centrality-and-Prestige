from graph.shortest_paths import ShortestPaths

PathsAdjacencyMatrix = dict[str, dict[str, ShortestPaths]]


from graph.graph import Graph


def floyd_warshall_algorithm(graph: Graph):
    ids = list(graph.nodes.keys())
    num_nodes = len(graph.nodes)
    adjacency_list: PathsAdjacencyMatrix = {}

    for node_id in ids:
        row: dict[str, ShortestPaths] = {}
        adjacency_list[node_id] = row

        for neighbor_id in ids:
            shortest_path = ShortestPaths()
            if node_id == neighbor_id:
                shortest_path.check_add([])
            elif neighbor_id in graph.nodes[node_id].neighbors:
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
                if curr_path.length() < sum_path.length():
                    row[y] = curr_path
                else:
                    if sum_path.length() == curr_path.length():
                        sum_path.unchecked_consume(curr_path)
                    row[y] = sum_path

    return next_level_dp
