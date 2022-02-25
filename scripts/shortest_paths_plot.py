import pandas as pd
import plotly.express as px

df = pd.read_csv("docs/shortest_paths.csv")

df["Number of Paths"] = df["Number of Paths"].astype(int).astype(str)

max_path_size = max(filter(lambda x: x != float("inf"), df["Path Size"]))
df.loc[df["Path Size"] == float("inf"), "Path Size"] = max_path_size + 1

fig = px.scatter_3d(
    df,
    title="Shortest Paths Grid Map",
    x="From Node",
    y="To Node",
    z="Number of Paths",
    color="Path Size",
    labels={
        "From Node": "Starting from Node",
        "To Node": "Ending at Node",
    },
    color_continuous_scale="Earth",
    template="plotly_dark",
)

fig.show()

fig = px.density_heatmap(
    df,
    title="Shortest Paths Grid Map",
    x="From Node",
    y="To Node",
    z="Path Size",
    hover_data=["Number of Paths", "Path Size"],
    labels={
        "From Node": "Starting from Node",
        "To Node": "Ending at Node",
    },
    color_continuous_scale="speed",
    template="plotly_dark",
)

fig.show()
