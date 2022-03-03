import pandas as pd
import plotly.express as px

df = pd.read_csv("docs/page_rank.csv")

fig = px.bar(
    df,
    x="Node ID",
    y=df["Page Rank"],
    color="Node ID",
    animation_frame="Iteration",
    animation_group="Node ID",
    labels={
        "x": "Unique ID for Node",
        "y": "Page Rank for the Node",
    },
    color_continuous_scale="Earth",
    template="plotly_dark",
)
fig.show()


fig = px.line(
    df,
    x="Iteration",
    y="Page Rank",
    color="Node ID",
    markers=True,
    line_shape="spline",
    labels={
        "x": "Iteration being observed",
        "y": "Page Rank for the Node",
    },
    template="plotly_dark",
)
fig.show()
