import pandas as pd
from graph.Graph import Graph
from tabulate import tabulate


def main():
    graph = Graph()

    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_node("d")
    graph.add_node("e")
    graph.add_node("f")

    graph.connect_nodes("a", "b")
    graph.connect_nodes("b", "c")
    graph.connect_nodes("c", "d")
    graph.connect_nodes("d", "e")
    graph.connect_nodes("e", "f")
    graph.connect_nodes("f", "a")

    graph.connect_nodes("a", "d")

    shortest_paths_matrix = graph.floyd_warshall_algorithm()
    pd.DataFrame(shortest_paths_matrix).to_csv("docs/shortest_paths.csv")

    graph.degree_centrality()
    graph.closeness_centrality(shortest_paths_matrix)
    graph.betweenness_centrality(shortest_paths_matrix)

    data = []
    for node in graph.nodes.values():
        data.append(
            {
                "Node ID": node.id,
                "Neighbors": list(node.neighbors.keys()),
                "Degree Centrality": node.store["Degree Centrality"],
                "Closeness Centrality": node.store["Closeness Centrality"],
                "Betweenness Centrality": node.store["Betweenness Centrality"],
            }
        )

    df = pd.DataFrame(data).set_index("Node ID")
    print(tabulate(df, headers="keys", tablefmt="fancy_grid"))
    df.to_csv("docs/centrality_measures.csv")


if __name__ == "__main__":
    main()
