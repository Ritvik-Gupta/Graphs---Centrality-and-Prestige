import re

from graph.graph import Graph


def parse_file_for_graph(filename: str) -> Graph:
    with open(filename) as file:
        graph = Graph()
        line = file.readline()

        if len(line) == 0:
            raise Exception("Empty File Found")

        node_ids = line.split()
        for node_id in node_ids:
            if re.match(r"^[a-zA-Z]+$", node_id) is None:
                raise Exception()
            graph.add_node(node_id)

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
                    case "=":
                        graph.connect_nodes(a_id, b_id)
                    case ">":
                        graph.nodes[a_id].add_neighbour(graph.nodes[b_id])
                    case _:
                        raise GraphConnectionError("Invalid Connection Type")

        return graph


class GraphConnectionError(Exception):
    pass
