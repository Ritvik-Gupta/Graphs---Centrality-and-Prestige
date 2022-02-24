import sys

import pandas as pd
from graph.algorithms.floyd_warshall import floyd_warshall_algorithm
from tabulate import tabulate
from utils.graph_parser import parse_file_for_graph


def main(args: list[str]):
    print("Name :                   Ritvik Gupta")
    print("Registration Number :    19BCE0397", end="\n\n")

    if len(args) == 0:
        raise FileNotFoundError("Filename for Graph not specified")

    graph = parse_file_for_graph(args[0])

    shortest_paths_matrix = floyd_warshall_algorithm(graph)

    df = pd.DataFrame(shortest_paths_matrix)
    print(tabulate(df, headers="keys", tablefmt="fancy_grid"))
    df.to_csv("docs/shortest_paths_matrix.csv")

    data = []
    for (from_node_id, shortest_paths_to) in shortest_paths_matrix.items():
        for (to_node_id, shortest_paths) in shortest_paths_to.items():
            data.append(
                {
                    "From Node": from_node_id,
                    "To Node": to_node_id,
                    "Paths": shortest_paths,
                    "Number of Paths": len(shortest_paths.paths),
                    "Path Size": shortest_paths.length(),
                }
            )

    df = pd.DataFrame(data).set_index(["From Node", "To Node"])
    df.to_csv("docs/shortest_paths.csv")

    graph.degree_centrality()
    graph.closeness_centrality(shortest_paths_matrix)
    graph.betweenness_centrality(shortest_paths_matrix)
    graph.degree_prestige()
    graph.proximity_prestige(shortest_paths_matrix)

    table = []
    data = []
    for node in graph.nodes.values():
        table.append(
            {
                "Node ID": node.id,
                "Neighbors": list(node.neighbors.keys()),
                "Degree Centrality": node.store["Degree Centrality"],
                "Closeness Centrality": node.store["Closeness Centrality"],
                "Betweenness Centrality": node.store["Betweenness Centrality"],
                "Degree Prestige": node.store["Degree Prestige"],
                "Proximity Prestige": node.store["Proximity Prestige"],
            }
        )
        for (metric, value) in node.store.items():
            data.append({"Node ID": node.id, "Metric": metric, "Value": value})

    df = pd.DataFrame(table).set_index("Node ID")
    print(tabulate(df, headers="keys", tablefmt="fancy_grid"))
    df.to_csv("docs/graph_metrics_table.csv")

    df = pd.DataFrame(data).set_index(["Node ID", "Metric"])
    df.to_csv("docs/graph_metrics.csv")


if __name__ == "__main__":
    main(sys.argv[1:])
