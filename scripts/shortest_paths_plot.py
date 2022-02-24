import pandas as pd
import plotly.express as px

df = pd.read_csv("docs/shortest_paths.csv")

df["Number of Paths"] = df["Number of Paths"].astype(int).astype(str)

max_path_size = max(filter(lambda x: x != float("inf"), df["Path Size"]))
df.loc[df["Path Size"] == float("inf"), "Path Size"] = max_path_size + 1

fig = px.scatter(
    df,
    title="Shortest Paths Grid Map",
    x="From Node",
    y="To Node",
    size="Path Size",
    color="Number of Paths",
    hover_name="Paths",
    hover_data=["Number of Paths", "Path Size"],
    labels={
        "From Node": "Starting from Node",
        "To Node": "Ending at Node",
    },
)

fig.show()
