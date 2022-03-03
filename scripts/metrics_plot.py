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
    template="plotly_dark",
)
fig.show()


fig = px.bar(
    df,
    title="Graph Metrics - Centrality and Prestige Measures",
    x="Node ID",
    y="Value",
    color="Metric",
    labels={"Node ID": "Unique ID for Node", "Value": "Centrality or Prestige Metric"},
    template="plotly_dark",
)
fig.show()


df = pd.read_csv("docs/graph_metrics_table.csv")

max_proximity = max(df["Proximity Prestige"])

fig = px.scatter_polar(
    df,
    title="Graph Metrics - Centrality and Prestige Measures",
    r=1 / df["Betweenness Centrality"],
    log_r=True,
    size="Betweenness Centrality",
    theta=df["Proximity Prestige"] * 360 / max_proximity,
    color="Node ID",
    template="plotly_dark",
)
fig.show()
