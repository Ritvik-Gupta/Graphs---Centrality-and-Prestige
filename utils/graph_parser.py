import re

from graph.graph_network import GraphNetwork


# Parses a Graph in a TEXT file for a specific notation followed 
def parse_file_for_graph(graph_filename: str) -> GraphNetwork:
    with open(f"./graph_notations/{graph_filename}.txt") as file:
        graph = GraphNetwork()
        line = file.readline() # First line would contain the Node IDs

        if len(line) == 0:
            raise Exception("Empty File Found")

        node_ids = line.split()
        for node_id in node_ids:
            # Node IDs should only be AlphaNumeric
            if re.match(r"^[a-zA-Z1-9]+$", node_id) is None:
                raise Exception()
            graph.add_node(node_id)

        # For every other line below there are Links / Connections from A to B
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue

            try:
                [a_id, sep, b_id] = line.split()
            except ValueError:
                raise GraphConnectionError("Invalid Connection Format")
            else:
                match sep:
                    case "=": # Connection can be Undirected A = B
                        graph.connect_nodes(a_id, b_id)
                    case ">": # Connection can be Directed A -> B
                        graph.nodes[a_id].add_neighbour(graph.nodes[b_id])
                    case _:
                        raise GraphConnectionError("Invalid Connection Type")

        return graph


class GraphConnectionError(Exception):
    pass
