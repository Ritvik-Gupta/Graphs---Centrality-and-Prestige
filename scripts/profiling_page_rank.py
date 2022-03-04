import pandas as pd
from graph.algorithms.page_rank import page_rank_algorithm
from tabulate import tabulate
from utils.graph_parser import parse_file_for_graph


def main():
    print("Name :                   Ritvik Gupta")
    print("Registration Number :    19BCE0397")
    print("Experiment :             Page Rank", end="\n\n")

    graph_filename = input("Enter the Filename for a Graph in `graph_notations` :\t")
    graph = parse_file_for_graph(graph_filename)
    num_iterations = int(
        input("Enter the Number of Iterations to run the algorithm :\t")
    )

    rank_frames = dict(enumerate(page_rank_algorithm(graph, num_iterations)))
    print(tabulate(pd.DataFrame(rank_frames), headers="keys", tablefmt="fancy_grid"))

    data = []
    for (iteration, page_ranks) in rank_frames.items():
        for (node_id, rank) in page_ranks.items():
            data.append({"Iteration": iteration, "Node ID": node_id, "Page Rank": rank})
    df = pd.DataFrame(data)
    df.to_csv("docs/page_rank.csv")


if __name__ == "__main__":
    main()
