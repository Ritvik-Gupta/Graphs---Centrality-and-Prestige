import pandas as pd
from graph.algorithms.floyd_warshall import floyd_warshall_algorithm
from graph.Graph import Graph
from tabulate import tabulate


def main():
    graph = Graph()

    graph.add_node("1")
    graph.add_node("2")
    graph.add_node("3")
    graph.add_node("4")
    graph.add_node("5")
    graph.add_node("6")

    graph.nodes["2"].add_neighbour(graph.nodes["1"])
    graph.nodes["3"].add_neighbour(graph.nodes["1"])
    graph.nodes["4"].add_neighbour(graph.nodes["3"])
    graph.nodes["5"].add_neighbour(graph.nodes["3"])
    graph.nodes["6"].add_neighbour(graph.nodes["3"])
    graph.nodes["4"].add_neighbour(graph.nodes["5"])
    graph.nodes["5"].add_neighbour(graph.nodes["6"])

    shortest_paths_matrix = floyd_warshall_algorithm(graph)
    df = pd.DataFrame(shortest_paths_matrix)
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

    print(tabulate(table, headers="keys", tablefmt="fancy_grid"))

    df = pd.DataFrame(data).set_index(["Node ID", "Metric"])
    df.to_csv("docs/graph_metrics.csv")


if __name__ == "__main__":
    main()
