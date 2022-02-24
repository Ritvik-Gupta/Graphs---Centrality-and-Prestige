import pandas as pd
import plotly.express as px

df = pd.read_csv("docs/graph_metrics.csv")

fig = px.scatter(
    df,
    title="Graph Metrics - Centrality and Prestige Measures",
    x="Node ID",
    y="Value",
    log_y=True,
    size=df["Value"] + 1,
    color="Metric",
    symbol="Metric",
    labels={"Node ID": "Unique ID for Node", "Value": "Centrality or Prestige Metric"},
)
fig.show()
