import pandas as pd
import plotly.express as px

df = pd.read_csv("docs/graph_metrics.csv")

fig = px.scatter(df, x="Node ID", y="Value", size=(df["Value"] + 1) * 5, color="Metric")
fig.show()
