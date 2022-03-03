from graph.graph_network import GraphNetwork


def _create_filtered_graph(graph: GraphNetwork) -> GraphNetwork:
    filtered_graph = GraphNetwork()

    for node in graph.nodes.values():
        if node.num_out_links() != 0:
            filtered_graph.add_node(node.id)

    for node in graph.nodes.values():
        for neighbor in node.out_links.values():
            try:
                node = filtered_graph.nodes[node.id]
                neighbor = filtered_graph.nodes[neighbor.id]
            except:
                continue
            else:
                node.add_neighbour(neighbor)

    return filtered_graph


def page_rank_algorithm(graph: GraphNetwork, num_iterations: int, damping_factor=0.85):
    graph = _create_filtered_graph(graph)
    node_ranks = {node_id: 1.0 for node_id in graph.nodes}

    yield dict(node_ranks)

    for _ in range(1, num_iterations + 1):
        next_ranks = {}
        for node_id in node_ranks:
            next_ranks[node_id] = (1 - damping_factor) + damping_factor * sum(
                map(
                    lambda neighbor: node_ranks[neighbor.id] / neighbor.num_out_links(),
                    graph.nodes[node_id].in_links.values(),
                )
            )

        node_ranks = next_ranks
        yield dict(node_ranks)
